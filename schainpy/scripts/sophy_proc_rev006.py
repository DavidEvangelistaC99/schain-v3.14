#!/usr/bin/env python
import matplotlib.pyplot as pl
import matplotlib
import wradlib
import numpy
import warnings
import argparse
from wradlib.io import read_generic_hdf5
from wradlib.util import get_wradlib_data_file
from plotting_codes import sophy_cb_tables
import os,time

for name, cb_table in sophy_cb_tables:
    ncmap = matplotlib.colors.ListedColormap(cb_table, name=name)
    matplotlib.pyplot.register_cmap(cmap=ncmap)
#LINUX bash: export WRADLIB_DATA=/path/to/wradlib-data
warnings.filterwarnings('ignore')
PARAM = {
    'S': {'var': 'dataPP_POWER','vmin': -45, 'vmax': -15, 'cmap': 'jet', 'label': 'Power','unit': 'dBm'},
    'V': {'var': 'velRadial_V', 'vmin': -10, 'vmax': 10 , 'cmap': 'sophy_v', 'label': 'Velocity','unit': 'm/s'},
    'Z': {'var': 'Zdb',         'vmin': -30, 'vmax': 80 , 'cmap': 'sophy_r','label': 'Reflectivity','unit': 'dBZ'},
    'W': {'var': 'Sigmav_W',    'vmin': 0  , 'vmax': 12 , 'cmap': 'sophy_w','label': 'Spectral Width','unit': 'hz'}
    }
class Readsophy():
    def __init__(self):
        self.list_file = None
        self.grado     = None
        self.variable  = None
        self.save      = None

    def read_files(self,path_file,grado=None, variable=None):
        filter= "_E"+str(grado)+".0_"+variable
        validFilelist = []
        fileList= os.listdir(path_file)
        for thisFile in fileList:
            if (os.path.splitext(thisFile)[0][-7:] != filter):
                #print("s_:",os.path.splitext(thisFile)[0][-7:])
                continue
            validFilelist.append(thisFile)
            validFilelist.sort()
        return validFilelist

    def setup(self, path_file,grado,variable,save):
        self.path_file = path_file
        self.grado     = grado
        self.variable  = variable
        self.save      = save
        self.list_file = self.read_files(path_file=self.path_file,grado=self.grado, variable=self.variable)

    def run(self):
        count= 0
        len_files = len(self.list_file)

        for thisFile in self.list_file:
            count = count +1
            fullpathfile = self.path_file + thisFile
            filename   = get_wradlib_data_file(fullpathfile)
            test_hdf5  = read_generic_hdf5(filename)

            var    = PARAM[self.variable]['var']
            unit   = PARAM[self.variable]['unit']
            cmap   = PARAM[self.variable]['cmap']
            vmin   = PARAM[self.variable]['vmin']
            vmax   = PARAM[self.variable]['vmax']
            label  = PARAM[self.variable]['label']
            var_    = 'Data/'+var+'/channel00'
            data_arr   = numpy.array(test_hdf5[var_]['data']) # data
            utc_time   = numpy.array(test_hdf5['Data/utctime']['data'])
            data_azi   = numpy.array(test_hdf5['Metadata/data_azi']['data']) # th
            data_ele   = numpy.array(test_hdf5["Metadata/data_ele"]['data'])
            heightList = numpy.array(test_hdf5["Metadata/heightList"]['data']) # r
            my_time    = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(utc_time[0]))
            time_save  = time.strftime('%Y%m%d_%H%M%S',time.localtime(utc_time[0]))

            # PLOT DATA WITH ANNOTATION
            if count ==1:
                fig = pl.figure(figsize=(10,8))
                cgax, pm = wradlib.vis.plot_ppi(data_arr,r=heightList,az=data_azi,rf=1e3,fig=fig, ax=111,proj='cg',cmap=cmap,vmin=vmin, vmax=vmax)
                caax  = cgax.parasites[0]
                title = 'Simple PPI'+"-"+ my_time
                t = pl.title(title, fontsize=12,y=1.05)
                cbar = pl.gcf().colorbar(pm, pad=0.075)
                pl.text(1.0, 1.05, 'azimuth', transform=caax.transAxes, va='bottom',ha='right')
                cbar.set_label(label+'[' + unit + ']')
                gh = cgax.get_grid_helper()
            else:
                cgax, pm = wradlib.vis.plot_ppi(data_arr,r=heightList,az=data_azi,rf=1e3,fig=fig, ax=111,proj='cg',cmap=cmap,vmin=vmin, vmax=vmax)
                caax  = cgax.parasites[0]
                title = 'Simple PPI'+"-"+my_time
                t = pl.title(title, fontsize=12,y=1.05)
                cbar = pl.gcf().colorbar(pm, pad=0.075)
                pl.text(1.0, 1.05, 'azimuth', transform=caax.transAxes, va='bottom',ha='right')
                cbar.set_label(label+'[' + unit + ']')
                gh = cgax.get_grid_helper()
            if self.save == 1:
                if count ==1:
                    filename     = "SOPHY"+"_"+time_save+"_"+"E."+self.grado+"_"+self.variable+".png"
                    dir =self.variable+"_"+"E."+self.grado+"CH0/"
                    filesavepath = os.path.join(self.path_file,dir)
                    os.mkdir(filesavepath)
                else:
                    filename     = "SOPHY"+"_"+time_save+"_"+"E."+self.grado+"_"+self.variable+".png"
                pl.savefig(filesavepath+filename)

            pl.pause(2)
            pl.clf()
        if count==len_files:
            pl.close()
        pl.show()

PATH = "/home/soporte/Documents/EVENTO/HYO_PM@2022-06-09T15-05-12/paramC0_FD_PL_R15.0km/2022-06-09T18-00-00/"

def main(args):
    grado      = args.grado
    parameters = args.parameters
    save       = args.save
    obj        = Readsophy()
    for param in parameters:
        obj.setup(path_file = PATH,grado = grado, variable=param,save=int(save))
        obj.run()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Script to process SOPHy data.')
    parser.add_argument('--parameters', nargs='*', default=['S'],
                        help='Variables to process: P, Z, V ,W')
    parser.add_argument('--grado', default=2,
                        help='Angle in Elev to plot')
    parser.add_argument('--save', default=0,
                        help='Save plot')
    args = parser.parse_args()

    main(args)


'''
def read_and_overview(filename):
    """Read HDF5 using read_generic_hdf5 and print upper level dictionary keys
    """
    test = read_generic_hdf5(filename)
    print("\nPrint keys for file %s" % os.path.basename(filename))
    for key in test.keys():
        print("\t%s" % key)
    return test

file__ = "/home/soporte/Documents/EVENTO/HYO_PM@2022-06-09T15-05-12/paramC0_FD_PL_R15.0km/2022-06-09T18-00-00/SOPHY_20220609_180229_E2.0_Z.hdf5"


filename = get_wradlib_data_file(file__)

print("filename:\n",filename )

test= read_and_overview(filename)
# ANADIR INFORMACION
# informacion de los pulsos de TX
# informacion de los ruidos
# informacion de los SNR ¿?
# Aumentar la amplitud de la USRP
'''
