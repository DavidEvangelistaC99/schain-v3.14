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
path      =  "/DATA_RM/10"
path_ped  =  "/DATA_RM/TEST_PEDESTAL/P20211111-173856"
print("----[OPCIONES]------------------------")
op_plot        = 0
op_integration = 0
op_save        = 0
op_plot_spec   = 0
