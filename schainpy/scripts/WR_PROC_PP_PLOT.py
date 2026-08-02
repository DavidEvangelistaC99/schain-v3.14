import os,sys
import datetime
import time
from schainpy.controller import Project
#path='/DATA_RM/TEST_HDF5/d2021200'
#path='/DATA_RM/TEST_HDF5/d2021200'
path='/home/david/Documents/DATA/CHIRP@2025-10-07T19-57-06/param-01_AUG/SNR_PPI_EL_1.0'

path_adq=path
#path_ped='/DATA_RM/TEST_PEDESTAL/P2021200'
path_ped='/home/david/Documents/DATA/CHIRP@2025-10-07T19-57-06/position/2025-10-07T19-00-00'

figpath = '/home/david/Documents/DATA/CHIRP@2025-10-07T19-57-06/Pictures'
desc            = "Simulator Test"

controllerObj   = Project()
controllerObj.setup(id='10',name='Test Simulator',description=desc)
readUnitConfObj = controllerObj.addReadUnit(datatype='HDFReader',
                                            path=path,
                                            startDate="2025/10/07",   #"2020/01/01",#today,
                                            endDate= "2025/10/08",  #"2020/12/30",#today,
                                            startTime='00:00:00',
                                            endTime='23:59:59',
                                            t_Interval_p=0.01,
                                            n_Muestras_p=100,
                                            delay=5,
                                            #set=0,
                                            online=0,
                                            walk=0)#1

procUnitConfObjA = controllerObj.addProcUnit(datatype='ParametersProc',inputId=readUnitConfObj.getId())

opObj11 = procUnitConfObjA.addOperation(name='PedestalInformation')
opObj11.addParameter(name='path_ped', value=path_ped)
opObj11.addParameter(name='path_adq', value=path_adq)
opObj11.addParameter(name='t_Interval_p', value='0.01', format='float')
opObj11.addParameter(name='n_Muestras_p', value='100', format='float')
opObj11.addParameter(name='blocksPerfile', value='100', format='int')
opObj11.addParameter(name='f_a_p', value='25', format='int')
opObj11.addParameter(name='online', value='0', format='int')


opObj11 = procUnitConfObjA.addOperation(name='Block360')
opObj11.addParameter(name='n', value='40', format='int')

opObj11= procUnitConfObjA.addOperation(name='WeatherPlot',optype='other')
opObj11.addParameter(name='save', value=figpath)
opObj11.addParameter(name='save_period', value=1)

controllerObj.start()
#online 1 utc_adq 1617490240.48
#online 0 utc_adq 1617489815.4804
