import os,sys,json
import datetime
import time
from schainpy.controller import Project
'''
NOTA:
Este script de prueba.
- Unidad del lectura 'HDFReader'.
- Unidad de procesamiento ParametersProc
- Operacion SpectralMomentsPlot

'''
path       = '/home/soporte/Downloads/RAWDATA'
figpath    = '/home/soporte/Downloads/IMAGE'
desc       = "Simulator Test"
desc_data  =  {
                'Data': {
                    'data_pow': 'Data/data_pow/channel00',
                    'data_dop': 'Data/data_dop/channel00',
                    'utctime':'Data/utctime'
                },
                'Metadata': {
                    'heightList':'Metadata/heightList',
                    'nIncohInt' :'Metadata/nIncohInt',
                    'nCohInt' :'Metadata/nCohInt',
                    'nProfiles' :'Metadata/nProfiles',
                    'channelList' :'Metadata/channelList'
                 }
               }

controllerObj   = Project()

controllerObj.setup(id='10',name='Test Simulator',description=desc)

readUnitConfObj = controllerObj.addReadUnit(datatype='HDFReader',
                                            path=path,
                                            startDate="2021/01/01",   #"2020/01/01",#today,
                                            endDate= "2021/12/01",  #"2020/12/30",#today,
                                            startTime='00:00:00',
                                            endTime='23:59:59',
                                            delay=0,
                                            #set=0,
                                            online=0,
                                            walk=1,
                                            description= json.dumps(desc_data))#1

procUnitConfObjA = controllerObj.addProcUnit(datatype='ParametersProc',inputId=readUnitConfObj.getId())
'''
opObj11 = procUnitConfObjA.addOperation(name='DopplerPlot',optype='external')
#opObj11.addParameter(name='xmin', value=0)
#opObj11.addParameter(name='xmax', value=23)
opObj11.addParameter(name='save', value=figpath)
opObj11.addParameter(name='showprofile', value=0)
opObj11.addParameter(name='save_period', value=10)
'''
controllerObj.start()
