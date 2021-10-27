# Ing. AVP
# 06/10/2021
# ARCHIVO DE LECTURA
import os, sys
import datetime
import time
from schainpy.controller import Project
#### NOTA###########################################
# INPUT :
# VELOCIDAD PARAMETRO :        V = 2°/seg
# MODO PULSE PAIR O MOMENTOS:  0 : Pulse Pair ,1 : Momentos
######################################################
##### PROCESAMIENTO ##################################
#####  OJO TENER EN CUENTA EL n= para el Pulse Pair ##
#####                   O EL n= nFFTPoints         ###
######################################################
######## BUSCAMOS EL numero de IPP equivalente 1°#####
######## Sea V la velocidad del Pedestal en °/seg#####
######## 1° sera Recorrido en un tiempo de  1/V ######
######## IPP del Radar 400 useg --> 60 Km ############
######## n   = 1/(V(°/seg)*IPP(Km)) , NUMERO DE IPP ##
######## n   = 1/(V*IPP) #############################
######## VELOCIDAD DEL PEDESTAL ######################
print("SETUP- RADAR METEOROLOGICO")
V       = 10
mode    = 0
#path    = '/DATA_RM/23/6v'
#path    = '/DATA_RM/TEST_INTEGRACION_2M'
path    = '/DATA_RM/WR_20_OCT'

#path_ped='/DATA_RM/TEST_PEDESTAL/P20211012-082745'
path_ped='/DATA_RM/TEST_PEDESTAL/P20211020-131248'

figpath_pp  = "/home/soporte/Pictures/TEST_PP"
figpath_mom = "/home/soporte/Pictures/TEST_MOM"
plot        = 0
integration = 1
save        = 0
if save == 1:
    if mode==0:
        path_save = '/DATA_RM/TEST_HDF5_PP_23/6v'
        path_save = '/DATA_RM/TEST_HDF5_PP'
        path_save = '/DATA_RM/TEST_HDF5_PP_100'
    else:
        path_save = '/DATA_RM/TEST_HDF5_SPEC_23_V2/6v'

print("* PATH data ADQ        :", path)
print("* Velocidad Pedestal   :",V,"°/seg")
############################ NRO Perfiles PROCESAMIENTO ###################
V=V
IPP=400*1e-6
n= int(1/(V*IPP))
print("* n - NRO Perfiles Proc:", n )
################################## MODE ###################################
print("* Modo de Operacion    :",mode)
if mode ==0:
    print("* Met. Seleccionado    : Pulse Pair")
else:
    print("* Met. Momentos        : Momentos")

################################## MODE ###################################
print("* Grabado de datos     :",save)
if save ==1:
    if mode==0:
        ope= "Pulse Pair"
    else:
        ope= "Momentos"
    print("* Path-Save Data -", ope , path_save)

print("* Integracion de datos :",integration)

time.sleep(5)
#remotefolder = "/home/wmaster/graficos"
#######################################################################
################# RANGO DE PLOTEO######################################
dBmin = '1'
dBmax = '85'
xmin = '15'
xmax = '15.25'
ymin = '0'
ymax = '600'
#######################################################################
########################FECHA##########################################
str = datetime.date.today()
today = str.strftime("%Y/%m/%d")
str2 = str - datetime.timedelta(days=1)
yesterday = str2.strftime("%Y/%m/%d")
#######################################################################
########################SIGNAL CHAIN ##################################
#######################################################################
desc = "USRP_test"
filename = "USRP_processing.xml"
controllerObj = Project()
controllerObj.setup(id = '191', name='Test_USRP', description=desc)
#######################################################################
######################## UNIDAD DE LECTURA#############################
#######################################################################
readUnitConfObj = controllerObj.addReadUnit(datatype='DigitalRFReader',
                                            path=path,
                                            startDate="2021/01/01",#today,
                                            endDate="2021/12/30",#today,
                                            startTime='00:00:00',
                                            endTime='23:59:59',
                                            delay=0,
                                            #set=0,
                                            online=0,
                                            walk=1,
                                            ippKm = 60)

opObj11 = readUnitConfObj.addOperation(name='printInfo')

procUnitConfObjA = controllerObj.addProcUnit(datatype='VoltageProc', inputId=readUnitConfObj.getId())

if mode ==0:
    ####################### METODO PULSE PAIR ######################################################################
    opObj11 = procUnitConfObjA.addOperation(name='PulsePair', optype='other')
    opObj11.addParameter(name='n', value=int(n), format='int')#10 VOY A USAR 250 DADO  QUE LA VELOCIDAD ES 10 GRADOS
    #opObj11.addParameter(name='removeDC', value=1, format='int')
    ####################### METODO Parametros ######################################################################
    procUnitConfObjB= controllerObj.addProcUnit(datatype='ParametersProc',inputId=procUnitConfObjA.getId())
    if plot==1:
        opObj11 = procUnitConfObjB.addOperation(name='GenericRTIPlot',optype='external')
        opObj11.addParameter(name='attr_data', value='dataPP_POW')
        opObj11.addParameter(name='colormap', value='jet')
        opObj11.addParameter(name='xmin', value=xmin)
        opObj11.addParameter(name='xmax', value=xmax)
        opObj11.addParameter(name='zmin', value=dBmin)
        opObj11.addParameter(name='zmax', value=dBmax)
        opObj11.addParameter(name='save', value=figpath_pp)
        opObj11.addParameter(name='showprofile', value=0)
        opObj11.addParameter(name='save_period', value=50)

    ####################### METODO ESCRITURA #######################################################################
    if save==1:
        opObj10 = procUnitConfObjB.addOperation(name='HDFWriter')
        opObj10.addParameter(name='path',value=path_save)
        #opObj10.addParameter(name='mode',value=0)
        opObj10.addParameter(name='blocksPerFile',value='100',format='int')
        opObj10.addParameter(name='metadataList',value='utctimeInit,timeZone,paramInterval,profileIndex,channelList,heightList,flagDataAsBlock',format='list')
        opObj10.addParameter(name='dataList',value='dataPP_POW,dataPP_DOP,utctime',format='list')#,format='list'
    if integration==1:
        V=10
        blocksPerfile=360
        print("* Velocidad del Pedestal:",V)
        tmp_blocksPerfile = 100
        f_a_p= int(tmp_blocksPerfile/V)

        opObj11 = procUnitConfObjB.addOperation(name='PedestalInformation')
        opObj11.addParameter(name='path_ped', value=path_ped)
        #opObj11.addParameter(name='path_adq', value=path_adq)
        opObj11.addParameter(name='t_Interval_p', value='0.01', format='float')
        opObj11.addParameter(name='blocksPerfile', value=blocksPerfile, format='int')
        opObj11.addParameter(name='n_Muestras_p', value='100', format='float')
        opObj11.addParameter(name='f_a_p', value=f_a_p, format='int')
        opObj11.addParameter(name='online', value='0', format='int')

        opObj11 = procUnitConfObjB.addOperation(name='Block360')
        opObj11.addParameter(name='n', value='10', format='int')
        opObj11.addParameter(name='mode', value=mode, format='int')

        # este bloque funciona bien con divisores de 360 no olvidar 0 10 20 30 40 60 90 120 180

        opObj11= procUnitConfObjB.addOperation(name='WeatherPlot',optype='other')


else:
    ####################### METODO SPECTROS ######################################################################
    procUnitConfObjB = controllerObj.addProcUnit(datatype='SpectraProc', inputId=procUnitConfObjA.getId())
    procUnitConfObjB.addParameter(name='nFFTPoints', value=n, format='int')
    procUnitConfObjB.addParameter(name='nProfiles' , value=n, format='int')

    procUnitConfObjC = controllerObj.addProcUnit(datatype='ParametersProc',inputId=procUnitConfObjB.getId())
    procUnitConfObjC.addOperation(name='SpectralMoments')
    if plot==1:
        dBmin = '1'
        dBmax = '65'
        opObj11 = procUnitConfObjC.addOperation(name='PowerPlot',optype='external')
        opObj11.addParameter(name='xmin', value=xmin)
        opObj11.addParameter(name='xmax', value=xmax)
        opObj11.addParameter(name='zmin', value=dBmin)
        opObj11.addParameter(name='zmax', value=dBmax)
        opObj11.addParameter(name='save', value=figpath_mom)
        opObj11.addParameter(name='showprofile', value=0)
        opObj11.addParameter(name='save_period', value=100)

    if save==1:
        opObj10 = procUnitConfObjC.addOperation(name='HDFWriter')
        opObj10.addParameter(name='path',value=path_save)
        #opObj10.addParameter(name='mode',value=0)
        opObj10.addParameter(name='blocksPerFile',value='360',format='int')
        #opObj10.addParameter(name='metadataList',value='utctimeInit,heightList,nIncohInt,nCohInt,nProfiles,channelList',format='list')#profileIndex
        opObj10.addParameter(name='metadataList',value='utctimeInit,heightList,nIncohInt,nCohInt,nProfiles,channelList',format='list')#profileIndex
        opObj10.addParameter(name='dataList',value='data_pow,data_dop,utctime',format='list')#,format='list'

    if integration==1:
       V=10
       blocksPerfile=360
       print("* Velocidad del Pedestal:",V)
       tmp_blocksPerfile = 100
       f_a_p= int(tmp_blocksPerfile/V)

       opObj11 = procUnitConfObjC.addOperation(name='PedestalInformation')
       opObj11.addParameter(name='path_ped', value=path_ped)
       #opObj11.addParameter(name='path_adq', value=path_adq)
       opObj11.addParameter(name='t_Interval_p', value='0.01', format='float')
       opObj11.addParameter(name='blocksPerfile', value=blocksPerfile, format='int')
       opObj11.addParameter(name='n_Muestras_p', value='100', format='float')
       opObj11.addParameter(name='f_a_p', value=f_a_p, format='int')
       opObj11.addParameter(name='online', value='0', format='int')

       opObj11 = procUnitConfObjC.addOperation(name='Block360')
       opObj11.addParameter(name='n', value='10', format='int')
       opObj11.addParameter(name='mode', value=mode, format='int')

       # este bloque funciona bien con divisores de 360 no olvidar 0 10 20 30 40 60 90 120 180
       opObj11= procUnitConfObjC.addOperation(name='WeatherPlot',optype='other')
controllerObj.start()
