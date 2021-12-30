# Ing. AVP
# 01/11/2021
# ARCHIVO DE LECTURA
import os, sys
import datetime
import time
from schainpy.controller import Project
print("----[Setup]-RadarMeteorologico--------")
Vel       =  6
modo_proc =  1
#-----------PATH DE DATOS-----------------------#
path      =  "/DATA_RM/10"
path_ped  =  "/DATA_RM/TEST_PEDESTAL/P20211111-173856"
print("----[OPCIONES]------------------------")
op_plot        = 0
op_integration = 0
op_save        = 0
op_plot_spec   = 0

########################SIGNAL CHAIN ##################################
desc = "USRP_test"
filename = "USRP_processing.xml"
controllerObj = Project()
controllerObj.setup(id = '191', name='Test_USRP', description=desc)
######################## UNIDAD DE LECTURA#############################
readUnitConfObj = controllerObj.addReadUnit(datatype='DigitalRFReader',
                                            path=path,
                                            startDate="2021/11/11",#today,
                                            endDate="2021/12/30",#today,
                                            startTime='17:39:25',
                                            endTime='23:59:59',
                                            delay=0,
                                            #set=0,
                                            online=0,
                                            walk=1,
                                            ippKm = 60)

opObj11 = readUnitConfObj.addOperation(name='printInfo')

procUnitConfObjA = controllerObj.addProcUnit(datatype='VoltageProc',inputId=readUnitConfObj.getId())
controllerObj.start()
