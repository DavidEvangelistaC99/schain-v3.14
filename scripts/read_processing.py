###---Processing Test---###

import os, sys
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from schainpy.controller import Project

path = '/home/idi/Documents/zmq/SIN@2026-01-21T00-00-01/rawdata/'

controllerObj = Project()
# -> Project.__init__()

controllerObj.setup(id = '001', name='Test_Read_Processing', description='Processing Test')
# -> Project.setup()

#######################################################################
############################ READING UNIT #############################
#######################################################################

# Working only Read Unit
readUnitConfObj = controllerObj.addReadUnit(datatype='DigitalRFReader',
                                            path=path,
                                            startDate='2026/01/01',
                                            endDate='2026/12/31',
                                            startTime='00:00:00',
                                            endTime='23:59:59',
                                            ippKm = 60,
                                            walk=1,
                                            getByBlock = 1,
                                            nProfileBlocks = 500,
                                            )
# -> Project.addReadUnit()
# Parameters send to ReadUnitConf()
# ReadUnitConf.setup() 

controllerObj.start()
# -> Project.run()
