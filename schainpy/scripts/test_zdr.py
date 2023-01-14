import numpy,os,time
import matplotlib
import argparse
import matplotlib.pyplot as plt
from wradlib.io import read_generic_hdf5
from wradlib.util import get_wradlib_data_file
from plotting_codes import sophy_cb_tables

for name, cb_table in sophy_cb_tables:
    ncmap = matplotlib.colors.ListedColormap(cb_table, name=name)
    matplotlib.pyplot.register_cmap(cmap=ncmap)
'''
NOTA:
- python3.10
- Conda environment:
  WR_CONDA_JUN14        *  /home/soporte/anaconda3/envs/WR_CONDA_JUN14
  export WRADLIB_DATA = "/media/soporte/TOSHIBAEXT/sophy/HYO_CC4_CC64_COMB@2022-12-26T00-00-32/param-EVENTO/"
- Update de plotting_codes
'''

PARAM = {
    'S': {'var': 'power','vmin': -45, 'vmax': -15, 'cmap': 'jet', 'label': 'Power','unit': 'dBm'},
    'V': {'var': 'velocity', 'vmin': -10, 'vmax': 10 , 'cmap': 'sophy_v', 'label': 'Velocity','unit': 'm/s'},
    'Z': {'var': 'reflectivity','vmin': -20, 'vmax': 80 , 'cmap': 'sophy_z','label': 'Reflectivity','unit': 'dBZ'},
    'W': {'var': 'spectral_width',    'vmin': 0  , 'vmax': 12 , 'cmap': 'sophy_w','label': 'Spectral Width','unit': 'm/s'},
    'R': {'var':'rhoHV','vmin': 0.2,   'vmax': 1,  'cmap': 'sophy_r','label': 'RhoHV', 'unit': ' '},
    'D': {'var': 'differential_reflectivity','vmin': -9, 'vmax': 12, 'cmap': 'sophy_d','label': 'ZDR' , 'unit': 'dB'}
    }

class Readsophy():
    def __init__(self):
        self.list_file = None
        self.grado     = None
        self.variable  = None
        self.save      = None
        self.range     = None
    def setup(self, path_file,mode,grado,range,variable,save):
        self.path_file = path_file
        self.mode      = mode
        self.range     = range
        self.grado     = grado
        self.variable  = variable
        self.save      = save
        self.list_file = self.read_files(path_file=self.path_file,mode=self.mode,grado=self.grado, variable=self.variable)
        print("self.list_file",self.list_file)

    def read_files(self,path_file,mode=None,grado=None, variable=None):
        if mode =='PPI':
           filter= "_E"+str(grado)+".0_"+variable
        else:
           filter= "_A"+str(grado)+".0_"+variable
        print("Filter     :",filter)
        validFilelist = []
        fileList= os.listdir(path_file)
        for thisFile in fileList:
            #print(thisFile)
            if  not os.path.splitext(thisFile)[0][-7:] in filter:
                print("s_:",os.path.splitext(thisFile)[0][-7:])
                continue
            validFilelist.append(thisFile)
            validFilelist.sort()
        return validFilelist

    def readAttributes(self,obj,variable):
        var    = PARAM[variable]['var']
        unit   = PARAM[variable]['unit']
        cmap   = PARAM[variable]['cmap']
        vmin   = PARAM[variable]['vmin']
        vmax   = PARAM[variable]['vmax']
        label  = PARAM[variable]['label']
        var_    = 'Data/'+var+'/H'
        data_arr   = numpy.array(obj[var_]['data']) # data
        utc_time   = numpy.array(obj['Data/time']['data'])
        data_azi   = numpy.array(obj['Metadata/azimuth']['data']) # th
        data_ele   = numpy.array(obj["Metadata/elevation"]['data'])
        heightList = numpy.array(obj["Metadata/range"]['data']) # r
        return data_arr, utc_time, data_azi,data_ele, heightList,unit,cmap,vmin,vmax,label

    def selectHeights(self,heightList,minHei,maxHei):

        if minHei and maxHei:
            if (minHei < heightList[0]):
                minHei = heightList[0]
            if (maxHei > heightList[-1]):
                maxHei = heightList[-1]
            minIndex = 0
            maxIndex = 0
            heights = heightList

            inda = numpy.where(heights >= minHei)
            indb = numpy.where(heights <= maxHei)

            try:
                minIndex = inda[0][0]
            except:
                minIndex = 0

            try:
                maxIndex = indb[0][-1]
            except:
                maxIndex = len(heights)

            new_heightList= self.selectHeightsByIndex(heightList=heightList,minIndex=minIndex, maxIndex=maxIndex)

        return new_heightList, minIndex,maxIndex

    def selectHeightsByIndex(self,heightList,minIndex, maxIndex):

        if (minIndex < 0) or (minIndex > maxIndex):
            raise ValueError("Height index range (%d,%d) is not valid" % (minIndex, maxIndex))

        if (maxIndex >= len(heightList)):
            maxIndex = len(heightList)

        new_h = heightList[minIndex:maxIndex]
        return new_h

    def run(self):
        count     = 0
        len_files = len(self.list_file)
        for thisFile in self.list_file:
            count= count +1
            print("Count :", count)
            fullpathfile = self.path_file + thisFile
            filename   = get_wradlib_data_file(fullpathfile)
            test_hdf5  = read_generic_hdf5(filename)
            # LECTURA
            data_arr, utc_time, data_azi,data_ele, heightList,unit,cmap,vmin,vmax,label = self.readAttributes(obj= test_hdf5,variable=self.variable)
            len_X= data_arr.shape[0]
            x=numpy.linspace(1,len_X,len_X)
            print("Data array:", data_arr.shape)
            print('data_azi',data_azi.shape)
            print('data_ele',data_ele.shape)
            if self.range==0:
                self.range == heightList[-1]
            new_heightList,minIndex,maxIndex = self.selectHeights(heightList,0.01,self.range)
            y= new_heightList
            # TIEMPO
            utc_time[0] = utc_time[0]+60*60*5
            my_time    = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(utc_time[0]))
            time_save  = time.strftime('%Y%m%d_%H%M%S',time.localtime(utc_time[0]))

            data_arr= data_arr[:,minIndex:maxIndex].transpose()
            z=data_arr
            profile = numpy.mean(z,1)
            print("x",profile.shape,profile)
            #print("y",y.shape,y)
            if count ==1:
               fig = plt.figure(figsize=(8,6))
               plt.plot(z,y)
               title = 'Sophy Plot '+label+"-"+ my_time+" "+self.mode+" "+self.grado
               t = plt.title(title, fontsize=12,y=1.05)
               '''
               plt.pcolormesh(x,y,z,cmap =cmap, vmin = vmin, vmax = vmax)
               title = 'Sophy Plot'+label+"-"+ my_time+" "+self.mode+" "+self.grado
               t = plt.title(title, fontsize=12,y=1.05)
               cbar = plt.colorbar()
               cbar.set_label(label+'[' + unit + ']')
               '''
            else:
               plt.plot(z,y)
               title = 'Sophy Plot '+label+"-"+ my_time+" "+self.mode+" "+self.grado
               t = plt.title(title, fontsize=12,y=1.05)
               '''
               plt.pcolormesh(x,y,z, cmap =cmap, vmin = vmin, vmax = vmax)
               title = 'Sophy Plot'+label+"-"+ my_time+" "+self.mode+" "+self.grado
               t = plt.title(title, fontsize=12,y=1.05)
               cbar = plt.colorbar()
               cbar.set_label(label+'[' + unit + ']')
               '''
            plt.xlim(-5,5)
            plt.ylim(0,self.range+1)
            '''
            if self.save == 1:
                if count ==1:
                    filename     = "SOPHY"+"_"+time_save+"_"+self.mode+"_"+self.grado+"_"+self.variable+str(self.range)+".png"
                    dir =self.variable+"_"+self.mode+self.grado+"CH0/"
                    filesavepath = os.path.join(self.path_file,dir)
                    try:
                      os.mkdir(filesavepath)
                    except:
                      pass
                else:
                    filename     = "SOPHY"+"_"+time_save+"_"+"E."+self.grado+"_"+self.variable+str(self.range)+".png"
                plt.savefig(filesavepath+filename)
            '''
            plt.pause(3)
            plt.clf()
            if  count == len_files:
                plt.close()
        plt.show()


def main(args):
    grado      = args.grado
    parameters = args.parameters
    save       = args.save
    range      = args.range
    mode       = args.mode
    obj        = Readsophy()
    print("MODE     :", mode)
    if  not mode =='PPI' and not mode =='RHI':
        print("Error - Choose Mode RHI or PPI")
        return None
    for param in parameters:
        print("Parameters : ", param)
        if mode =='PPI':
           PATH = "/media/soporte/TOSHIBAEXT/sophy/HYO_CC4_CC64_COMB@2022-12-26T00-00-32/param-EVENTO/"+str(param)+"_PPI_EL_"+str(grado)+".0/"
        else:
           PATH = "/media/soporte/TOSHIBAEXT/sophy/HYO_CC4_CC64_COMB@2022-12-26T00-00-32/param-EVENTO/"+str(param)+"_RHI_AZ_"+str(grado)+".0/"
        print("Path       : ",PATH)
        obj.setup(path_file =PATH,mode=mode,grado = grado,range=range, variable=param,save=int(save))
        print("SETUP OK")
        obj.run()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Script to process SOPHy data.')
    parser.add_argument('--parameters', nargs='*', default=['S'],
                        help='Variables to process: P, Z, V ,W,D')
    parser.add_argument('--grado', default=2,
                        help='Angle in Elev to plot')
    parser.add_argument('--mode',default='PPI',
                        help='MODE PPI or RHI')
    parser.add_argument('--save', default=0,
                        help='Save plot')
    parser.add_argument('--range', default=0, type=float,
                        help='Max range to plot')
    args = parser.parse_args()

    main(args)
