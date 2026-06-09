'''
Created on Jul 3, 2014

@author: roj-idl71
'''
# SUBCHANNELS EN VEZ DE CHANNELS
# BENCHMARKS -> PROBLEMAS CON ARCHIVOS GRANDES -> INCONSTANTE EN EL TIEMPO
# ACTUALIZACION DE VERSION
# HEADERS
# MODULO DE ESCRITURA
# METADATA

import os
import time
import datetime
import numpy
import timeit
from fractions import Fraction
from time import time
from time import sleep

import schainpy.admin
from schainpy.model.data.jroheaderIO import RadarControllerHeader, SystemHeader
from schainpy.model.data.jrodata import Voltage
from schainpy.model.proc.jroproc_base import ProcessingUnit, Operation, MPDecorator

import zmq
import json

import matplotlib.pyplot as plt

import pickle
try:
    os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
    import digital_rf
except:
    pass


class DigitalRFReader(ProcessingUnit):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

        ProcessingUnit.__init__(self)

        self.dataOut = Voltage()
        self.__printInfo = True
        self.__flagDiscontinuousBlock = False
        self.__bufferIndex = 9999999
        self.__codeType = 0
        self.__ippKm = None
        self.__nCode = None
        self.__nBaud = None
        self.__code = None
        self.dtype = None
        self.oldAverage = None
        self.path = None
        self.verbose = True

    def close(self):
        print('Average of writing to digital rf format is ', self.oldAverage * 1000)
        return

    def __getCurrentSecond(self):

        return self.__thisUnixSample / self.__sample_rate

    thisSecond = property(__getCurrentSecond, "I'm the 'thisSecond' property.")

    def __setFileHeader(self):
        '''
        In this method will be initialized every parameter of dataOut object (header, no data)
        '''
        ippSeconds = 1.0 * self.__nSamples / self.__sample_rate

        if not self.getByBlock:
            nProfiles = 1.0 / ippSeconds  # Number of profiles in one second
        else:
            nProfiles = self.nProfileBlocks # Number of profiles in one block

        try:
            self.dataOut.radarControllerHeaderObj = RadarControllerHeader(
                self.__radarControllerHeader)
        except:
            self.dataOut.radarControllerHeaderObj = RadarControllerHeader(
                txA=0,
                txB=0,
                nWindows=1,
                nHeights=self.__nSamples,
                firstHeight=self.__firstHeigth,
                deltaHeight=self.__deltaHeigth,
                codeType=self.__codeType,
                nCode=self.__nCode, nBaud=self.__nBaud,
                code=self.__code)

        try:
            self.dataOut.systemHeaderObj = SystemHeader(self.__systemHeader)
        except:
            self.dataOut.systemHeaderObj = SystemHeader(nSamples=self.__nSamples,
                                                        nProfiles=nProfiles,
                                                        nChannels=len(
                                                            self.__channelList),
                                                        adcResolution=14)
        self.dataOut.type = "Voltage"

        self.dataOut.data = None

        self.dataOut.dtype = self.dtype

        # self.dataOut.nChannels = 0
        # self.dataOut.nHeights = 0

        self.dataOut.nProfiles = int(nProfiles)

        self.dataOut.heightList = self.__firstHeigth + \
            numpy.arange(self.__nSamples, dtype=numpy.float32) * \
            self.__deltaHeigth

        #self.dataOut.channelList = list(range(self.__num_subchannels))
        self.dataOut.channelList = list(range(len(self.__channelList)))

        if not self.getByBlock:

            self.dataOut.blocksize   = self.dataOut.nChannels * self.dataOut.nHeights
        else:
            self.dataOut.blocksize   = self.dataOut.nChannels * self.dataOut.nHeights*self.nProfileBlocks

        # self.dataOut.channelIndexList = None

        self.dataOut.flagNoData = True

        if not self.getByBlock:
            self.dataOut.flagDataAsBlock = False
        else:
            self.dataOut.flagDataAsBlock = True
        # Set to TRUE if the data is discontinuous
        self.dataOut.flagDiscontinuousBlock = False

        self.dataOut.utctime = None

        # timezone like jroheader, difference in minutes between UTC and localtime
        self.dataOut.timeZone = self.__timezone / 60

        self.dataOut.dstFlag = 0

        self.dataOut.errorCount = 0
        
        '''
        Use of self.fixed_metadata_dict, atributtes don't exist
        '''
        try:
            self.dataOut.nCohInt = self.fixed_metadata_dict.get(
                'nCohInt', self.nCohInt)

            # asumo que la data esta decodificada
            self.dataOut.flagDecodeData = self.fixed_metadata_dict.get(
                'flagDecodeData', self.flagDecodeData)

            # asumo que la data esta sin flip
            self.dataOut.flagDeflipData = self.fixed_metadata_dict['flagDeflipData']

            self.dataOut.flagShiftFFT = self.fixed_metadata_dict['flagShiftFFT']

            self.dataOut.useLocalTime = self.fixed_metadata_dict['useLocalTime']
        except:

            pass
        
        self.dataOut.ippSeconds = ippSeconds

        # Time interval between profiles
        # self.dataOut.timeInterval = self.dataOut.ippSeconds * self.dataOut.nCohInt

        self.dataOut.frequency = self.__frequency

        self.dataOut.realtime = self.__online

    def findDatafiles(self, path, startDate=None, endDate=None):

        if not os.path.isdir(path):
            return []

        try:
            digitalReadObj = digital_rf.DigitalRFReader(
                path, load_all_metadata=True)
        except:
            digitalReadObj = digital_rf.DigitalRFReader(path)

        channelNameList = digitalReadObj.get_channels()
        # channelNameList = ['ch0','ch1']#,'ch1']

        if not channelNameList:
            return []

        metadata_dict = digitalReadObj.get_rf_file_metadata(channelNameList[0])

        sample_rate = metadata_dict['sample_rate'][0]

        this_metadata_file = digitalReadObj.get_metadata(channelNameList[0])

        try:
            timezone = this_metadata_file['timezone'].value
        except:
            timezone = 0

        startUTCSecond, endUTCSecond = digitalReadObj.get_bounds(
            channelNameList[0]) / sample_rate - timezone

        startDatetime = datetime.datetime.utcfromtimestamp(startUTCSecond)
        endDatatime = datetime.datetime.utcfromtimestamp(endUTCSecond)

        if not startDate:
            startDate = startDatetime.date()

        if not endDate:
            endDate = endDatatime.date()

        dateList = []

        thisDatetime = startDatetime

        while(thisDatetime <= endDatatime):

            thisDate = thisDatetime.date()

            if thisDate < startDate:
                continue

            if thisDate > endDate:
                break

            dateList.append(thisDate)
            thisDatetime += datetime.timedelta(1)

        return dateList

    def setup(self, path=None,
              startDate=None,
              endDate=None,
              startTime=datetime.time(0, 0, 0),
              endTime=datetime.time(23, 59, 59),
              channelList=None,
              nSamples=None,
              online=False,
              delay=60,
              buffer_size=1024,
              ippKm=None,
              nCohInt=1,
              nCode=1,
              nBaud=1,
              flagDecodeData=False,
              code=numpy.ones((1, 1), dtype=numpy.int32),
              getByBlock=0,
              nProfileBlocks=1,
              server = False,
              verbose=True,
              **kwargs):
        '''
        In this method we should set all initial parameters.

        Inputs:
            path
            startDate
            endDate
            startTime
            endTime
            set
            expLabel
            ext
            online
            delay
        
        Methods used:
            __setFileHeader()
            
        '''

        self.path = path
        self.nCohInt = nCohInt
        self.flagDecodeData = flagDecodeData
        self.i = 0
        self.verbose        = verbose
        self.getByBlock     = getByBlock
        self.nProfileBlocks = nProfileBlocks
        self.server = server

        self.channels__ = set()

        if self.server is True:

            META_ADDR = "tcp://localhost:5556"
            DATA_ADDR = "tcp://localhost:5555"

            self.ctx = zmq.Context()
            self.meta_sock = self.ctx.socket(zmq.SUB)
            self.meta_sock.connect(META_ADDR)

            self.meta_sock.setsockopt_string(
                zmq.SUBSCRIBE,
                ""
            )

            # =========================================
            # IQ DATA SOCKET
            # =========================================

            self.data_sock = self.ctx.socket(zmq.SUB)

            self.data_sock.connect(DATA_ADDR)

            self.data_sock.setsockopt_string(
                zmq.SUBSCRIBE,
                ""
            )
            '''
            Variable used for initialize IQ data adquisition
            '''
            self.__zmq_started = False

            poller = zmq.Poller()
            poller.register(self.meta_sock, zmq.POLLIN)

            events = dict(poller.poll())

            for _ in range(1):

                topic, payload = self.meta_sock.recv_multipart()

                metadata = json.loads(
                    payload.decode()
                )

                print("\n================================")
                print("METADATA RECEIVED")
                print("================================")

                print("Topic:", topic.decode())

                print(json.dumps(
                    metadata,
                    indent=4
                ))

                channel = topic.decode()
                self.channels__.add(channel)

            print("self.channels__", self.channels__)
            print("metadata", metadata)
            print("start_sample", metadata['acquisition']['start_sample'] )
            channelNameList = list(self.channels__)
            # self.channels__ reemplaza a channelNameList en zmq

            self.__num_subchannels = 1

            self.__sample_rate = 1.0 * metadata['receiver']['samp_rate']

            self.__deltaHeigth = 1e6 * 0.15 / self.__sample_rate

            self.__frequency = 1

            self.__timezone = 1

            nSamples = int(ippKm / (1e6 * 0.15 / self.__sample_rate))

            self.__firstHeigth = 0

            codeType = 0

            self.__ippKm = None

            startUTCSecond = None
            endUTCSecond = None

            '''
            New variable for timezone fix
            '''
            timezone = datetime.timedelta(seconds=self.__timezone)

            if startDate:
                startDatetime = datetime.datetime.combine(startDate, startTime)
                startUTCSecond = (
                    startDatetime - datetime.datetime(1970, 1, 1)).total_seconds() # + self.__timezone

            if endDate:
                endDatetime = datetime.datetime.combine(endDate, endTime)
                endUTCSecond = (endDatetime - datetime.datetime(1970,
                                                                1, 1)).total_seconds() # + self.__timezone
            
            '''
            Calculate start_index like this for now
            '''

            try:
                 self.digitalReadObj = digital_rf.DigitalRFReader(
                     path, load_all_metadata=True)
            except:
                self.digitalReadObj = digital_rf.DigitalRFReader(path)

            start_index, _ = self.digitalReadObj.get_bounds(
                channelNameList[0])

            # start_index = metadata['digital_rf']['start_sample']
            
            self.profileIndex = 0
            self.i = 0
            self.__delay = delay

            self.__codeType = codeType
            self.__nCode = nCode
            self.__nBaud = nBaud
            self.__code = code

            self.__datapath = path
            self.__online = online
            
            self.__channelNameList = list(self.channels__)
            self.__channelList = list(range(len(channelNameList)))

            #self.__channelBoundList = channelBoundList

            self.__nSamples = nSamples

            if self.getByBlock:
                nSamples = nSamples*nProfileBlocks

            # This variable is used as a block
            self.__samples_to_read = int(nSamples)
            self.__nChannels = len(list(self.channels__))

            self.__startUTCSecond = startUTCSecond
            self.__endUTCSecond = endUTCSecond

            self.__timeInterval = 1.0 * self.__samples_to_read / \
                self.__sample_rate  # Time interval
            
            '''
            Plus samplestoread in () method
            '''
            start_index = metadata['acquisition']['start_sample']
            self.__thisUnixSample = int(start_index) - self.__samples_to_read 

            print("self.__thisUnixSample")
            print(self.__thisUnixSample)
            
            self.__data_buffer    = numpy.zeros((int(self.__nChannels), self.__samples_to_read), dtype=numpy.complex64)
            
            self.__setFileHeader()
            
            print("[Reading] Digital RF Data was found from %s to %s " % (
            datetime.datetime.utcfromtimestamp(
                self.__startUTCSecond),# - self.__timezone),
            datetime.datetime.utcfromtimestamp(
                self.__endUTCSecond),# - self.__timezone)
            ))

            print("[Reading] Starting process from %s to %s" % (datetime.datetime.utcfromtimestamp(startUTCSecond - self.__timezone),
                                                                datetime.datetime.utcfromtimestamp(
                endUTCSecond - self.__timezone)
            ))
            self.oldAverage = None
            self.count = 0
            self.executionTime = 0

            self.dataOut.nCohInt = nCohInt

            self.isConfig = True


        else:

            if online:
                print('Waiting for RF data..')
                sleep(40)
            
            if not os.path.isdir(path):
                raise ValueError("[Reading] Directory %s does not exist" % path)

            '''
            Create digitalReadObj object from DigitalRF library. 
            '''
            try:
                self.digitalReadObj = digital_rf.DigitalRFReader(
                    path, load_all_metadata=True)
            except:
                self.digitalReadObj = digital_rf.DigitalRFReader(path)


            channelNameList = self.digitalReadObj.get_channels()
            # channelNameList = ['ch0','ch1']

            if not channelNameList:
                raise ValueError("[Reading] Directory %s does not have any files" % path)

            if not channelList:
                channelList = list(range(len(channelNameList)))

            '''
            Reading metadata 
            '''
            top_properties = self.digitalReadObj.get_properties(channelNameList[channelList[0]])
            
            self.__num_subchannels = top_properties['num_subchannels']

            self.__sample_rate = 1.0 * \
                top_properties['sample_rate_numerator'] / \
                top_properties['sample_rate_denominator']
            
            '''
            __deltaHeight is in km
            '''
            self.__deltaHeigth = 1e6 * 0.15 / self.__sample_rate

            this_metadata_file = self.digitalReadObj.get_digital_metadata(
                channelNameList[channelList[0]])

            metadata_bounds = this_metadata_file.get_bounds()

            self.fixed_metadata_dict = this_metadata_file.read(
                metadata_bounds[0])[metadata_bounds[0]]
            
            try:
                self.__processingHeader = self.fixed_metadata_dict['processingHeader']
                self.__radarControllerHeader = self.fixed_metadata_dict['radarControllerHeader']
                # radarControllerHeader doesn't exist 
                self.__systemHeader = self.fixed_metadata_dict['systemHeader']
                self.dtype = pickle.loads(self.fixed_metadata_dict['dtype'])
            except:
                pass

            self.__frequency = None

            self.__frequency = self.fixed_metadata_dict.get('frequency', 1)

            self.__timezone = self.fixed_metadata_dict.get('timezone', 18000)

            try:
                nSamples = self.fixed_metadata_dict['nSamples']
            except:
                nSamples = None

            self.__firstHeigth = 0

            try:
                codeType = self.__radarControllerHeader['codeType']
            except:
                codeType = 0

            try:
                if codeType:
                    nCode = self.__radarControllerHeader['nCode']
                    nBaud = self.__radarControllerHeader['nBaud']
                    code = self.__radarControllerHeader['code']
            except:
                pass

            if not ippKm:
                try:
                    # seconds to km
                    ippKm = self.__radarControllerHeader['ipp']
                except:
                    ippKm = None
            

            self.__ippKm = ippKm
            startUTCSecond = None
            endUTCSecond = None

            '''
            New variable for timezone fix
            '''
            timezone = datetime.timedelta(seconds=self.__timezone)  # normalmente 18000

            '''
            Calculate time seconds
            '''
            if startDate:
                startDatetime = datetime.datetime.combine(startDate, startTime)
                startUTCSecond = (
                    startDatetime - datetime.datetime(1970, 1, 1)).total_seconds() # + self.__timezone

            if endDate:
                endDatetime = datetime.datetime.combine(endDate, endTime)
                endUTCSecond = (endDatetime - datetime.datetime(1970,
                                                                1, 1)).total_seconds() # + self.__timezone

            '''
            Number of samples 
            '''
            start_index, end_index = self.digitalReadObj.get_bounds(
                channelNameList[channelList[0]])
            
            print(start_index)
            print(end_index)
        
            if start_index==None or end_index==None:
                print("Check error No data,  start_index: ",start_index,",end_index: ",end_index)

            if not startUTCSecond:
                startUTCSecond = start_index / self.__sample_rate

            if start_index > startUTCSecond * self.__sample_rate:
                startUTCSecond = start_index / self.__sample_rate

            if not endUTCSecond:
                endUTCSecond = end_index / self.__sample_rate

            if end_index < endUTCSecond * self.__sample_rate:
                endUTCSecond = end_index / self.__sample_rate
            if not nSamples:
                if not ippKm:
                    raise ValueError("[Reading] nSamples or ippKm should be defined")
                # IPP is a parameters defined in setup "DigitalRFReader" from Project
                nSamples = int(ippKm / (1e6 * 0.15 / self.__sample_rate))
            channelBoundList = []
            channelNameListFiltered = []

            for thisIndexChannel in channelList:
                thisChannelName = channelNameList[thisIndexChannel]
                start_index, end_index = self.digitalReadObj.get_bounds(
                    thisChannelName)
                channelBoundList.append((start_index, end_index))
                channelNameListFiltered.append(thisChannelName)
            
            '''
            channelBoundList = [(4448887260000000, 4448889222499999), 
                                (4448887265000000, 4448889210000000)]
            channelNameListFiltered = ['ch0', 'ch1']
            '''

            self.profileIndex = 0
            self.i = 0
            self.__delay = delay

            self.__codeType = codeType
            self.__nCode = nCode
            self.__nBaud = nBaud
            self.__code = code

            self.__datapath = path
            self.__online = online
            self.__channelList = channelList
            self.__channelNameList = channelNameListFiltered
            self.__channelBoundList = channelBoundList
            self.__nSamples = nSamples

            if self.getByBlock:
                nSamples = nSamples*nProfileBlocks

            '''
            Samples to read
            '''
            self.__samples_to_read = int(nSamples)
            self.__nChannels = len(self.__channelList)

            self.__startUTCSecond = startUTCSecond
            self.__endUTCSecond = endUTCSecond

            self.__timeInterval = 1.0 * self.__samples_to_read / \
                self.__sample_rate  # Time interval

            if online:
                # self.__thisUnixSample = int(endUTCSecond*self.__sample_rate - 4*self.__samples_to_read)
                startUTCSecond = numpy.floor(endUTCSecond)

            '''
            Read cursor 
            '''
            # por que en el otro metodo lo primero q se hace es sumar samplestoread
            self.__thisUnixSample = int(startUTCSecond * self.__sample_rate) - self.__samples_to_read

            print("self.__thisUnixSample")
            print(self.__thisUnixSample)

            #self.__data_buffer = numpy.zeros(
            #    (self.__num_subchannels, self.__samples_to_read), dtype=numpy.complex)
            self.__data_buffer    = numpy.zeros((int(len(channelList)), self.__samples_to_read), dtype=numpy.complex64)
            self.__setFileHeader()
            self.isConfig = True

            print("[Reading] Digital RF Data was found from %s to %s " % (
                datetime.datetime.utcfromtimestamp(
                    self.__startUTCSecond),# - self.__timezone),
                datetime.datetime.utcfromtimestamp(
                    self.__endUTCSecond),# - self.__timezone)
            ))

            print("[Reading] Starting process from %s to %s" % (datetime.datetime.utcfromtimestamp(startUTCSecond - self.__timezone),
                                                                datetime.datetime.utcfromtimestamp(
                endUTCSecond - self.__timezone)
            ))
            self.oldAverage = None
            self.count = 0
            self.executionTime = 0
        
        # =========================================
        # BUFFER
        # =========================================

        self.buffer___ = numpy.array([], dtype=numpy.complex64)

        print("[Reading] Receiving IQ ...")

    def __reload(self):
        #         print
        #         print "%s not in range [%s, %s]" %(
        #                                           datetime.datetime.utcfromtimestamp(self.thisSecond - self.__timezone),
        #                                           datetime.datetime.utcfromtimestamp(self.__startUTCSecond - self.__timezone),
        #                                           datetime.datetime.utcfromtimestamp(self.__endUTCSecond - self.__timezone)
        #                                           )
        print("[Reading] reloading metadata ...")

        try:
            self.digitalReadObj.reload(complete_update=True)
        except:
            self.digitalReadObj = digital_rf.DigitalRFReader(self.path) 

        start_index, end_index = self.digitalReadObj.get_bounds(
            self.__channelNameList[self.__channelList[0]])

        if start_index > self.__startUTCSecond * self.__sample_rate:
            self.__startUTCSecond = 1.0 * start_index / self.__sample_rate

        if end_index > self.__endUTCSecond * self.__sample_rate:
            self.__endUTCSecond = 1.0 * end_index / self.__sample_rate
            print()
            print("[Reading] New timerange found [%s, %s] " % (
                datetime.datetime.utcfromtimestamp(
                    self.__startUTCSecond - self.__timezone),
                datetime.datetime.utcfromtimestamp(
                    self.__endUTCSecond - self.__timezone)
            ))

            return True

        return False

    def timeit(self, toExecute):
        t0 = time.time()
        toExecute()
        self.executionTime = time.time() - t0
        if self.oldAverage is None:
            self.oldAverage = self.executionTime
        self.oldAverage = (self.executionTime + self.count * 
                           self.oldAverage) / (self.count + 1.0)
        self.count = self.count + 1.0
        return

    def __readNextBlock(self, seconds=30, volt_scale=1):
        '''
        NOTA: APLICACION RADAR METEOROLOGICO
        VALORES OBTENIDOS CON LA USRP, volt_scale = 1,conexion directa al Ch Rx.

        MAXIMO
        9886  -> 0.980 Voltiospp
        4939  -> 0.480 Voltiospp
        14825 -> 1.440 Voltiospp
        18129 -> 1.940 Voltiospp
        Para llevar al valor correspondiente de Voltaje, debemos dividir por 20000
        y obtenemos la Amplitud correspondiente de entrada IQ.
        volt_scale = (1/20000.0)
        '''

        # Set the next data
        self.__flagDiscontinuousBlock = False
        self.__thisUnixSample += self.__samples_to_read
        
        if self.__thisUnixSample + 2 * self.__samples_to_read > self.__endUTCSecond * self.__sample_rate:
            print ("[Reading] There are no more data into selected time-range")
            if self.__online:
                sleep(3)
                self.__reload()
            else:
                return False

            if self.__thisUnixSample + 2 * self.__samples_to_read > self.__endUTCSecond * self.__sample_rate:
                return False
                self.__thisUnixSample -= self.__samples_to_read

        indexChannel = 0

        dataOk = False
        
        for thisChannelName in self.__channelNameList:  # TODO VARIOS CHANNELS?
            for indexSubchannel in range(self.__num_subchannels):
                try:
                    t0 = time()
                    result = self.digitalReadObj.read_vector_c81d(self.__thisUnixSample,
                                                                  self.__samples_to_read,
                                                                  thisChannelName, sub_channel=indexSubchannel)
                    self.executionTime = time() - t0
                    if self.oldAverage is None:
                        self.oldAverage = self.executionTime
                    self.oldAverage = (
                        self.executionTime + self.count * self.oldAverage) / (self.count + 1.0)
                    self.count = self.count + 1.0

                except IOError as e:
                    # read next profile
                    self.__flagDiscontinuousBlock = True
                    print("[Reading] %s" % datetime.datetime.utcfromtimestamp(self.thisSecond - self.__timezone), e)
                    bot = 0
                    while(self.__flagDiscontinuousBlock):
                        bot +=1
                        self.__thisUnixSample += self.__samples_to_read
                        try:
                            result = result = self.digitalReadObj.read_vector_c81d(self.__thisUnixSample,self.__samples_to_read,thisChannelName, sub_channel=indexSubchannel)
                            self.__flagDiscontinuousBlock=False
                            print("Searching.. N°: ",bot,"Success",self.__thisUnixSample)
                        except:
                            print("Searching...N°: ",bot,"Fail", self.__thisUnixSample)
                    if self.__flagDiscontinuousBlock==True:
                        break
                    else:
                        print("New data index found...",self.__thisUnixSample)
                    

                if result.shape[0] != self.__samples_to_read:
                    self.__flagDiscontinuousBlock = True
                    print("[Reading] %s: Too few samples were found, just %d/%d  samples" % (datetime.datetime.utcfromtimestamp(self.thisSecond - self.__timezone),
                                                                                             result.shape[0],
                                                                                             self.__samples_to_read))
                    break
                
                #self.__data_buffer[indexSubchannel, :] = result * volt_scale
                self.__data_buffer[indexChannel, :] = result
                self.__data_buffer[indexChannel, :] *= volt_scale
                indexChannel += 1

                dataOk = True

        self.__utctime = self.__thisUnixSample / self.__sample_rate

        if not dataOk:
            return False

        if self.verbose:
            print("[Reading] %s: %d samples <> %f sec" % (datetime.datetime.utcfromtimestamp(self.thisSecond - self.__timezone),
                                                      self.__samples_to_read,
                                                      self.__timeInterval))

        self.__bufferIndex = 0

        return True

    def __isBufferEmpty(self):
        return self.__bufferIndex > self.__samples_to_read - self.__nSamples  # 40960 - 40
    
    def getDataZmq(self):
        '''
        Method to used ZMQ data transmission
        '''
        
        self.dataOut.flagNoData = True
        self.__flagDiscontinuousBlock = False

        '''
        Initialize data adquisition
        '''

        self.__zmq_started = True

        if not self.__zmq_started:

            CTRL_ADDR = "tcp://localhost:6000"

            self.ctrl_sock = self.ctx.socket(zmq.REQ)

            self.ctrl_sock.connect(CTRL_ADDR)

            print("[CTRL] Sending READY")

            self.ctrl_sock.send(b"READY")

            reply = self.ctrl_sock.recv()

            print("[CTRL] TX reply:", reply.decode())

            # Give PUB/SUB time to stabilize
            sleep(1)

            self.__zmq_started = True

        # -------------------------------------
        # RECEIVE ZMQ DATA
        # -------------------------------------

        msg = self.data_sock.recv()

        # iq = numpy.frombuffer(msg, dtype=numpy.complex64)

        # iq = numpy.frombuffer(msg, dtype=[('r','<i2'), ('i','<i2')])

        tmp = numpy.frombuffer(msg, dtype='<i2')
        tmp = tmp.reshape(-1, 2)

        iq = (tmp[:,0] + 1j*tmp[:,1]).astype(numpy.complex64)

        #print(iq)
        #print(len(iq))
        
        # sleep(40)
        #plt.plot(numpy.abs(iq.flatten()))
        #plt.show()
        
        
        # -------------------------------------
        # APPEND TO BUFFER
        # -------------------------------------

        self.buffer___ = numpy.concatenate((self.buffer___, iq))
        
        # -------------------------------------
        # PROCESS COMPLETE BLOCKS
        # -------------------------------------

        if len(self.buffer___) >= self.__samples_to_read:

            # EXACT BLOCK
            iq_block = self.buffer___[:self.__samples_to_read]

            # REMOVE USED SAMPLES
            self.buffer___ = self.buffer___[self.__samples_to_read:]

            # ---------------------------------
            # PROCESS BLOCK
            # ---------------------------------

            print("len de iq_block", len(iq_block))

            #iq_block = numpy.roll(iq_block, 500)

            # encontrar primer índice donde se cumple condición
            mask = numpy.abs(iq_block) > 50

            if numpy.any(mask):
                idx = numpy.argmax(mask)   # primer True
                iq_block = numpy.roll(iq_block, -idx)
            else:
                print("WARNING: no values > 50 found")

            #plt.plot(numpy.abs(iq_block))
            #plt.show()
            
            iq_block = iq_block.reshape(1, -1)
            iq_block = iq_block.reshape((self.__nChannels, self.nProfileBlocks, int(self.__samples_to_read/self.nProfileBlocks)))

            print("iq_block shape", iq_block.shape)

            self.dataOut.nProfileBlocks = self.nProfileBlocks
            self.dataOut.data = iq_block

            # plt.plot(numpy.abs(iq_block.flatten()))
            # plt.show()

            #print(iq_block.shape)

            # for j in range(500):

            #    t = [i for i in range(len(iq_block[0,j,:]))]
            #    plt.plot(t,iq_block[0,j,:])

            #    plt.plot(numpy.abs(iq_block.flatten()))
            #    plt.show()

            self.dataOut.utctime = ( self.__thisUnixSample + self.__bufferIndex) / self.__sample_rate
            self.profileIndex  += self.__samples_to_read
            self.__bufferIndex += self.__samples_to_read
            self.__thisUnixSample += self.__samples_to_read
            self.dataOut.flagDiscontinuousBlock = self.__flagDiscontinuousBlock
            self.dataOut.flagNoData = False
        
        return True

        

    def getData(self, seconds=30, nTries=5):
        '''
            This method gets the data from files and put the data into the dataOut object

            In addition, increase el the buffer counter in one.

            Return:
                data    :    retorna un perfil de voltages (alturas * canales) copiados desde el
                            buffer. Si no hay mas archivos a leer retorna None.

            Affected:
                self.dataOut
                self.profileIndex
                self.flagDiscontinuousBlock
                self.flagIsNewBlock
        '''
        # print("getdata")
        err_counter = 0
        self.dataOut.flagNoData = True

        if self.__isBufferEmpty():

            self.__flagDiscontinuousBlock = False

            while True:
                
                if self.__readNextBlock():
                    break
                if self.__thisUnixSample > self.__endUTCSecond * self.__sample_rate:
                    raise schainpy.admin.SchainError('Error')
                    return

                if self.__flagDiscontinuousBlock:
                    raise schainpy.admin.SchainError('discontinuous block found')
                    return

                if not self.__online:
                    raise schainpy.admin.SchainError('Online?')
                    return

                err_counter += 1
                if err_counter > nTries:
                    raise schainpy.admin.SchainError('Max retrys reach')
                    return

                print('[Reading] waiting %d seconds to read a new block' % seconds)
                time.sleep(seconds)
            
            if not self.getByBlock:

                self.dataOut.data = self.__data_buffer[:, self.__bufferIndex:self.__bufferIndex + self.__nSamples]
                self.dataOut.utctime = ( self.__thisUnixSample + self.__bufferIndex) / self.__sample_rate
                self.dataOut.flagNoData = False
                self.dataOut.flagDiscontinuousBlock = self.__flagDiscontinuousBlock
                self.dataOut.profileIndex = self.profileIndex

                self.__bufferIndex += self.__nSamples
                self.profileIndex  += 1

                if self.profileIndex == self.dataOut.nProfiles:
                    self.profileIndex = 0
            else:
                # ojo debo anadir el readNextBLock y el  __isBufferEmpty(
                self.dataOut.flagNoData             = False
                buffer = self.__data_buffer[:,self.__bufferIndex:self.__bufferIndex + self.__samples_to_read]
                print(buffer.shape)
                buffer = buffer.reshape((self.__nChannels, self.nProfileBlocks, int(self.__samples_to_read/self.nProfileBlocks)))

                print(buffer.shape)
                self.dataOut.nProfileBlocks = self.nProfileBlocks
                self.dataOut.data = buffer
                self.dataOut.utctime = ( self.__thisUnixSample + self.__bufferIndex) / self.__sample_rate
                self.profileIndex  += self.__samples_to_read
                self.__bufferIndex += self.__samples_to_read
                self.dataOut.flagDiscontinuousBlock = self.__flagDiscontinuousBlock
            return True

    def printInfo(self):
        '''
        '''
        if self.__printInfo == False:
            return

        # self.systemHeaderObj.printInfo()
        # self.radarControllerHeaderObj.printInfo()

        self.__printInfo = False

    def printNumberOfBlock(self):
        '''
        '''
        return
        # print self.profileIndex

    def run(self, **kwargs):
        '''
        This method will be called many times so here you should put all your code
        '''
        
        if not self.isConfig:
            self.setup(**kwargs)
        # self.i = self.i+1
        
        if self.server is True:
            self.getDataZmq()
        else:
            self.getData(seconds=self.__delay)
        
        return

@MPDecorator
class DigitalRFWriter(Operation):
    '''
    classdocs
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        Operation.__init__(self, **kwargs)
        self.metadata_dict = {}
        self.dataOut = None
        self.dtype = None
        self.oldAverage = 0

    def setHeader(self):

        self.metadata_dict['frequency'] = self.dataOut.frequency
        self.metadata_dict['timezone'] = self.dataOut.timeZone
        self.metadata_dict['dtype'] = pickle.dumps(self.dataOut.dtype)
        self.metadata_dict['nProfiles'] = self.dataOut.nProfiles
        self.metadata_dict['heightList'] = self.dataOut.heightList
        self.metadata_dict['channelList'] = self.dataOut.channelList
        self.metadata_dict['flagDecodeData'] = self.dataOut.flagDecodeData
        self.metadata_dict['flagDeflipData'] = self.dataOut.flagDeflipData
        self.metadata_dict['flagShiftFFT'] = self.dataOut.flagShiftFFT
        self.metadata_dict['useLocalTime'] = self.dataOut.useLocalTime
        self.metadata_dict['nCohInt'] = self.dataOut.nCohInt
        self.metadata_dict['type'] = self.dataOut.type
        self.metadata_dict['flagDataAsBlock'] = getattr(
            self.dataOut, 'flagDataAsBlock', None)  # chequear

    def setup(self, dataOut, path, frequency, fileCadence, dirCadence, metadataCadence, set=0, metadataFile='metadata', ext='.h5'):
        '''
        In this method we should set all initial parameters.
        Input:
            dataOut: Input data will also be outputa data
        '''
        self.setHeader()
        self.__ippSeconds = dataOut.ippSeconds
        self.__deltaH = dataOut.getDeltaH()
        self.__sample_rate = 1e6 * 0.15 / self.__deltaH
        self.__dtype = dataOut.dtype
        if len(dataOut.dtype) == 2:
            self.__dtype = dataOut.dtype[0]
        self.__nSamples = dataOut.systemHeaderObj.nSamples
        self.__nProfiles = dataOut.nProfiles

        if self.dataOut.type != 'Voltage':
            raise 'Digital RF cannot be used with this data type'
            self.arr_data = numpy.ones((1, dataOut.nFFTPoints * len(
                self.dataOut.channelList)), dtype=[('r', self.__dtype), ('i', self.__dtype)])
        else:
            self.arr_data = numpy.ones((self.__nSamples, len(
                self.dataOut.channelList)), dtype=[('r', self.__dtype), ('i', self.__dtype)])

        file_cadence_millisecs = 1000

        sample_rate_fraction = Fraction(self.__sample_rate).limit_denominator()
        sample_rate_numerator = int(sample_rate_fraction.numerator)
        sample_rate_denominator = int(sample_rate_fraction.denominator)
        start_global_index = dataOut.utctime * self.__sample_rate

        uuid = 'prueba'
        compression_level = 0
        checksum = False
        is_complex = True
        num_subchannels = len(dataOut.channelList)
        is_continuous = True
        marching_periods = False

        self.digitalWriteObj = digital_rf.DigitalRFWriter(path, self.__dtype, dirCadence,
                                                          fileCadence, start_global_index,
                                                          sample_rate_numerator, sample_rate_denominator, uuid, compression_level, checksum,
                                                          is_complex, num_subchannels, is_continuous, marching_periods)
        metadata_dir = os.path.join(path, 'metadata')
        os.system('mkdir %s' % (metadata_dir))
        self.digitalMetadataWriteObj = digital_rf.DigitalMetadataWriter(metadata_dir, dirCadence, 1,  # 236, file_cadence_millisecs / 1000
                                                                        sample_rate_numerator, sample_rate_denominator,
                                                                        metadataFile)
        self.isConfig = True
        self.currentSample = 0
        self.oldAverage = 0
        self.count = 0
        return

    def writeMetadata(self):
        start_idx = self.__sample_rate * self.dataOut.utctime

        self.metadata_dict['processingHeader'] = self.dataOut.processingHeaderObj.getAsDict(
        )
        self.metadata_dict['radarControllerHeader'] = self.dataOut.radarControllerHeaderObj.getAsDict(
        )
        self.metadata_dict['systemHeader'] = self.dataOut.systemHeaderObj.getAsDict(
        )
        self.digitalMetadataWriteObj.write(start_idx, self.metadata_dict)
        return

    def timeit(self, toExecute):
        t0 = time()
        toExecute()
        self.executionTime = time() - t0
        if self.oldAverage is None:
            self.oldAverage = self.executionTime
        self.oldAverage = (self.executionTime + self.count * 
                           self.oldAverage) / (self.count + 1.0)
        self.count = self.count + 1.0
        return

    def writeData(self):
        if self.dataOut.type != 'Voltage':
            raise 'Digital RF cannot be used with this data type'
            for channel in self.dataOut.channelList:
                for i in range(self.dataOut.nFFTPoints):
                    self.arr_data[1][channel * self.dataOut.nFFTPoints + 
                                     i]['r'] = self.dataOut.data[channel][i].real
                    self.arr_data[1][channel * self.dataOut.nFFTPoints + 
                                     i]['i'] = self.dataOut.data[channel][i].imag
        else:
            for i in range(self.dataOut.systemHeaderObj.nSamples):
                for channel in self.dataOut.channelList:
                    self.arr_data[i][channel]['r'] = self.dataOut.data[channel][i].real
                    self.arr_data[i][channel]['i'] = self.dataOut.data[channel][i].imag

        def f(): return self.digitalWriteObj.rf_write(self.arr_data)
        self.timeit(f)

        return

    def run(self, dataOut, frequency=49.92e6, path=None, fileCadence=1000, dirCadence=36000, metadataCadence=1, **kwargs):
        '''
        This method will be called many times so here you should put all your code
        Inputs:
            dataOut: object with the data
        '''
        # print dataOut.__dict__
        self.dataOut = dataOut
        if not self.isConfig:
            self.setup(dataOut, path, frequency, fileCadence,
                       dirCadence, metadataCadence, **kwargs)
            self.writeMetadata()

        self.writeData()

        # # self.currentSample += 1
        # if self.dataOut.flagDataAsBlock or self.currentSample == 1:
        # self.writeMetadata()
        # # if self.currentSample == self.__nProfiles: self.currentSample = 0

        return dataOut  # en la version 2.7 no aparece este return

    def close(self):
        print('[Writing] - Closing files ')
        print('Average of writing to digital rf format is ', self.oldAverage * 1000)
        try:
            self.digitalWriteObj.close()
        except:
            pass
