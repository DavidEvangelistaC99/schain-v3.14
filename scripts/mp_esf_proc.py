#!/usr/bin/env python
import os, sys, json
from datetime import datetime, timedelta

from schainpy.controller import Project

desc = "ESF Experiment"

controllerObj = Project()

controllerObj.setup(id = '191', name='test01', description=desc)

startDate = '2026/04/25'
endDate = '2026/04/26'
startTime = '18:00:00'
endTime = '06:59:00'
online=0
walk=1
path = '/home/idi/Documents/DATA/ESF'
plots='/home/idi/Documents/DATA/ESF/plots'
channels=[0,1]
altura_1=[90,1468.5]
delay=60
tiempo=['18','31']
dB=['-2','20']
dB_range=['2','18']
title='ESF'

startDBS = '2023/10/05'
d1 = datetime.strptime(startDBS, '%Y/%m/%d')
d2 = datetime.strptime(startDate, '%Y/%m/%d')
mode=1 if d2 >= d1 else 0
mode_fit = 0 # 1: one gaussian adjustment, 0: None gaussian adjustment
dbs_sel=1
exp='ESF_EW'

procUnitConfObj1 = controllerObj.addReadUnit(datatype='SpectraReader',
                                            path=path,
                                            startDate=startDate,
                                            endDate=endDate,
                                            startTime=startTime,
                                            endTime=endTime,
                                            delay=delay,
                                            online=online,
                                            getByBlock=0,
                                            #server="tcp://10.10.10.85:5556",
                                            walk=walk)

######################## MP #############################################

n = '3'
opObj11 = procUnitConfObj1.addOperation(name='IncohInt')
opObj11.addParameter(name='n', value= n, format='float')                # 6 seconds by spc

opObj11 = procUnitConfObj1.addOperation(name='SpectraPlot')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='zmin', value=dB_range[0], format='int')
opObj11.addParameter(name='zmax', value=dB_range[1], format='int')
opObj11.addParameter(name='ymin', value=altura_1[0], format='float')
opObj11.addParameter(name='ymax', value=altura_1[1], format='float')
opObj11.addParameter(name='xaxis', value='velocity', format='str')
opObj11.addParameter(name='showprofile', value=1, format='int')
opObj11.addParameter(name='save', value=plots, format='str')


opObj11 = procUnitConfObj1.addOperation(name='RTIPlot')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='xmin', value=tiempo[0], format='float')
opObj11.addParameter(name='xmax', value=tiempo[1], format='float')
opObj11.addParameter(name='ymin', value=altura_1[0], format='float')
opObj11.addParameter(name='ymax', value=altura_1[1], format='float')
opObj11.addParameter(name='zmin', value=dB_range[0], format='int')
opObj11.addParameter(name='zmax', value=dB_range[1], format='int')
opObj11.addParameter(name='showprofile', value='1', format='int')
opObj11.addParameter(name='throttle', value='100')
opObj11.addParameter(name='save', value=plots, format='str')


opObj11 = procUnitConfObj1.addOperation(name='NoisePlot')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='xmin', value=tiempo[0], format='float')
opObj11.addParameter(name='xmax', value=tiempo[1], format='float')
opObj11.addParameter(name='throttle', value='100')
opObj11.addParameter(name='save', value=plots, format='str')


procUnitConfObj2 = controllerObj.addProcUnit(datatype='ParametersProc', inputId=procUnitConfObj1.getId())

opObj11 = procUnitConfObj2.addOperation(name='SpectralMoments', optype='external')
opObj11.addParameter(name='proc_type', value=1)    # Last spectral moments routine
opObj11.addParameter(name='mode_fit', value=mode_fit)
opObj11.addParameter(name='exp', value=exp)

opObj11 = procUnitConfObj2.addOperation(name='SnrPlot', optype='external')
opObj11.addParameter(name='xmin', value=tiempo[0], format='int')
opObj11.addParameter(name='xmax', value=tiempo[1], format='int')
opObj11.addParameter(name='ymin', value=altura_1[0], format='float')
opObj11.addParameter(name='ymax', value=altura_1[1], format='float')
opObj11.addParameter(name='zmin', value=dB[0], format='int')
opObj11.addParameter(name='zmax', value=dB[1], format='int')
opObj11.addParameter(name='throttle', value='100')
opObj11.addParameter(name='save', value=plots, format='str')


opObj11 = procUnitConfObj2.addOperation(name='JULIA_NightVelocities', optype='other')
opObj11.addParameter(name='zenith', value=[-2.452834,  2.944165], format='list')
opObj11.addParameter(name='zenithCorrection', value='0.0', format='float')
opObj11.addParameter(name='mymode', value=mode,  format='int')
opObj11.addParameter(name='dbs_sel', value=dbs_sel,  format='int')
opObj11.addParameter(name='jset', value=3,  format='int')
opObj11.addParameter(name='clean', value=True,  format='bool')

titles=('SNR0, SNR1, DOPPLER0, DOPPLER1')
opObj11 = procUnitConfObj2.addOperation(name='GenericRTIPlot', optype='other')
opObj11.addParameter(name='colormaps', value='jet,jet,RdBu_r,RdBu_r')
opObj11.addParameter(name='attr_data', value='data_output')
opObj11.addParameter(name='wintitle', value=title)
opObj11.addParameter(name='titles', value=titles)
opObj11.addParameter(name='zfactors', value='1,1,1,1')
opObj11.addParameter(name='zlimits', value='(-4,6),(-4,6),(-150,150),(-150,150)')
opObj11.addParameter(name='cb_labels', value='dB,dB,m/s,m/s')
opObj11.addParameter(name='xmin', value=tiempo[0])
opObj11.addParameter(name='xmax', value=tiempo[1])
opObj11.addParameter(name='ymin', value=altura_1[0])
opObj11.addParameter(name='ymax', value=altura_1[1])    
opObj11.addParameter(name='throttle', value='100')
opObj11.addParameter(name='save', value=plots, format='str')

controllerObj.start()
