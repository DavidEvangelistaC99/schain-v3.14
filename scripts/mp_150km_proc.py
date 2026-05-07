#!/usr/bin/env python
import os, sys, json

from schainpy.controller import Project

desc = "EWDrifts+Imaging+Faraday Experiment"

controllerObj = Project()

controllerObj.setup(id = '191', name='test01', description=desc)
startDate = '2026/04/24'
endDate =  '2026/04/24'
startTime =  '07:00:00'
endTime =  '16:59:59'
dpath = '/home/idi/Documents/DATA/150km'
plots = '/home/idi/Documents/DATA/150km/plots'
online = 0
delay = 15
walk=0

dB_range= ['2', '18']
dB=['-20','-10']
tiempo=['7', '18']
altura_1=['0', '200.0']
altura_2=['125.0', '185.0']
velocidad=['-50', '50']
sw=[0,10]
pwr=[-55,-48]
title='150Km'
exp_code='211'

exp = '150EEJ'
mode_fit = 1
web='10.10.120.138:4444'
procUnitConfObj1 = controllerObj.addReadUnit(datatype='SpectraReader',
                                            path=dpath,
                                            startDate=startDate,
                                            endDate=endDate,
                                            startTime=startTime,
                                            endTime=endTime,
                                            delay=delay,
                                            online=online,
                                            getByBlock=1,
                                            #server="tcp://10.10.10.85:5556",
                                            walk=walk)

######################## MP #############################################

opObj11 = procUnitConfObj1.addOperation(name='SpectraPlot')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='zmin', value=dB_range[0], format='int')
opObj11.addParameter(name='zmax', value=dB_range[1], format='int')
opObj11.addParameter(name='ymin', value=altura_1[0], format='float')
opObj11.addParameter(name='ymax', value=altura_1[1], format='float')
opObj11.addParameter(name='xmin', value=velocidad[0], format='float')
opObj11.addParameter(name='xmax', value=velocidad[1], format='float')
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
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='save', value=plots, format='str')

opObj11 = procUnitConfObj1.addOperation(name='NoisePlot')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='xmin', value=tiempo[0], format='float')
opObj11.addParameter(name='xmax', value=tiempo[1], format='float')
opObj11.addParameter(name='ymin', value=dB_range[0], format='int')
opObj11.addParameter(name='ymax', value=dB_range[1], format='int')
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='save', value=plots, format='str')


procUnitConfObj2 = controllerObj.addProcUnit(datatype='ParametersProc', inputId=procUnitConfObj1.getId())

opObj11 = procUnitConfObj2.addOperation(name='SpectralMoments', optype='external')
opObj11.addParameter(name='proc_type', value=1)
opObj11.addParameter(name='exp', value=exp)
opObj11.addParameter(name='mode_fit', value=mode_fit)

opObj11 = procUnitConfObj2.addOperation(name='SpectralMomentsPlot', optype='external')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='zmin', value=dB_range[0], format='int')
opObj11.addParameter(name='zmax', value=dB_range[1], format='int')
opObj11.addParameter(name='ymin', value=altura_2[0], format='float')
opObj11.addParameter(name='ymax', value=altura_2[1], format='float')
opObj11.addParameter(name='xmin', value=velocidad[0], format='float')
opObj11.addParameter(name='xmax', value=velocidad[1], format='float')
opObj11.addParameter(name='xaxis', value='velocity', format='str')
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='save', value=plots, format='str')

opObj11 = procUnitConfObj2.addOperation(name='DopplerPlot')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='xmin', value=tiempo[0], format='float')
opObj11.addParameter(name='xmax', value=tiempo[1], format='float')
opObj11.addParameter(name='zmin', value=velocidad[0], format='int')
opObj11.addParameter(name='zmax', value=velocidad[1], format='int')
opObj11.addParameter(name='ymin', value=altura_2[0], format='float')
opObj11.addParameter(name='ymax', value=altura_2[1], format='float')
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='save', value=plots, format='str')

opObj11 = procUnitConfObj2.addOperation(name='SnrPlot', optype='external')
opObj11.addParameter(name='xmin', value=tiempo[0], format='int')
opObj11.addParameter(name='xmax', value=tiempo[1], format='int')
opObj11.addParameter(name='ymin', value=altura_2[0], format='float')
opObj11.addParameter(name='ymax', value=altura_2[1], format='float')
opObj11.addParameter(name='zmin', value=dB[0], format='int')
opObj11.addParameter(name='zmax', value=dB[1], format='int')
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='save', value=plots, format='str')

opObj11 = procUnitConfObj2.addOperation(name='JULIA_DayVelocities', optype='external')
opObj11.addParameter(name='zenith', value=[-2.452834,  2.944165], format='list')
opObj11.addParameter(name='clean', value=False,  format='bool')
opObj11.addParameter(name='amountdata', value=2,  format='float')
opObj11.addParameter(name='driftstdv_th', value=10.0,  format='float')
opObj11.addParameter(name='zonalstdv_th', value=80.0,  format='float')

titles=('150 kM SNL, 150kM Vertical Drifts, 150 kM Zonal Drifts')
opObj11 = procUnitConfObj2.addOperation(name='GenericRTIPlot', optype='other')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='colormaps', value='jet,RdBu_r,RdBu_r')
opObj11.addParameter(name='attr_data', value='data_graph')
opObj11.addParameter(name='titles', value=titles)
opObj11.addParameter(name='zfactors', value='1,1,1')
opObj11.addParameter(name='zlimits', value='(-1,1),(-20,20),(-30,30)')
opObj11.addParameter(name='cb_labels', value='dB,m/s,m/s')
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='xmin', value=tiempo[0])
opObj11.addParameter(name='xmax', value=tiempo[1])
opObj11.addParameter(name='save', value=plots, format='str')

opObj11 = procUnitConfObj2.addOperation(name='AverageDriftsPlot', optype='external')
opObj11.addParameter(name='wintitle', value=title, format='str')
opObj11.addParameter(name='xmin', value=tiempo[0], format='int')
opObj11.addParameter(name='xmax', value=tiempo[1], format='int')
opObj11.addParameter(name='zlimits', value='(-15,35),(-80,60)')
opObj11.addParameter(name='throttle', value='200')
opObj11.addParameter(name='save', value=plots, format='str')

controllerObj.start()
