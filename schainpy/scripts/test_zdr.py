import numpy,os,time
import matplotlib
import argparse
import matplotlib.pyplot as plt
from wradlib.io import read_generic_hdf5
from wradlib.util import get_wradlib_data_file
from plotting_codes import sophy_cb_tables
from scipy import stats

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
    def setup(self, path_file,mode,grado,range,r_min,variable,save):
        self.path_file = path_file
        self.mode      = mode
        self.range     = range
        self.grado     = grado
        self.r_min     = r_min
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

    def plot_PPI_RHI(self,count,x,y,z,cmap,my_time,vmin,vmax,label,unit,mode,grado):
        if count==1:
           fig = plt.figure(figsize=(8,6))
           plt.pcolormesh(x,y,z,cmap =cmap, vmin = vmin, vmax = vmax)
           title = 'Sophy Plot'+label+"-"+ my_time+" "+mode+" "+grado
           t = plt.title(title, fontsize=12,y=1.05)
           cbar = plt.colorbar()
           cbar.set_label(label+'[' + unit + ']')
        else:
           plt.pcolormesh(x,y,z, cmap =cmap, vmin = vmin, vmax = vmax)
           title = 'Sophy Plot'+label+"-"+ my_time+" "+mode+" "+grado
           t = plt.title(title, fontsize=12,y=1.05)
           cbar = plt.colorbar()
           cbar.set_label(label+'[' + unit + ']')

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
            #SELECCION DE ALTURAS
            if self.range==0:
                self.range == heightList[-1]
            if self.r_min==0:
                self.r_min = 0.01
            new_heightList,minIndex,maxIndex = self.selectHeights(heightList,self.r_min,self.range)
            # TIEMPO
            utc_time[0] = utc_time[0]+60*60*5
            my_time    = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(utc_time[0]))
            time_save  = time.strftime('%Y%m%d_%H%M%S',time.localtime(utc_time[0]))
            data_arr= data_arr[:,minIndex:maxIndex].transpose()
            # VARIABLES
            x=numpy.linspace(1,len_X,len_X)
            y= new_heightList
            z=data_arr
            profile = numpy.mean(z,1)
            # Seleccion del arreglo
            '''
            len_Z= z.shape[1]
            min_CC=numpy.zeros(len_Z)
            min_index_CC = numpy.zeros(len_Z)
            for i in range(len_Z):
                tmp=numpy.nanmin(z[:,i])
                tmp_index = numpy.nanargmin((z[:,i]))

                if  tmp <0.6:
                    tmp_index= numpy.nan
                    value = numpy.nan
                else:
                    value= new_heightList[tmp_index]
                min_CC[i] =value
            moda_,count_m_ = stats.mode(min_CC)
            print(moda_)
            for i in range(len_Z):
                if min_CC[i]>moda_[0]+0.15 or min_CC[i]<moda_[0]-0.15:
                    min_CC[i]=numpy.nan

            min_index_CC=min_CC/0.06
            #print(min_CC.shape,min_CC)
            print("LONGITUD",min_index_CC.shape)
            '''
            len_Z= z.shape[1]
            min_CC = numpy.zeros(len_Z)
            min_CC = numpy.load("index.npy")
            bb     = numpy.zeros(len_Z)

            for i in range(len_Z):
                if min_CC[i]==numpy.nan:
                    bb[i]=numpy.nan
                try:
                    bb[i]=z[int(min_CC[i]*0.06)][i]
                except:
                    bb[i]=numpy.nan
            print("bb",bb)
            print("bb _ prom_ZDR",numpy.nanmean(bb))
            if count ==1:
               #arr_ = min_index_CC
               '''
               fig = plt.figure(figsize=(8,6))

               plt.plot(z,y)
               title = 'Sophy Plot '+label+"-"+ my_time+" "+self.mode+" "+self.grado
               t = plt.title(title, fontsize=12,y=1.05)
               '''
               self.plot_PPI_RHI(count=count,x=x,y=y,z=z-1.2,cmap=cmap,my_time=my_time,vmin=vmin,vmax=vmax,label =label,unit=unit, mode=self.mode,grado=self.grado)
               #plt.plot(x,min_CC[0:len_X]*0.06,'yo')
               #cota_min = 0
               #cota_max= len_X
            else:
               #cota_min= cota_min+len_X
               #cota_max= cota_min+len_X
               #arr_ = numpy.append(arr_,min_index_CC)
               self.plot_PPI_RHI(count=count,x=x,y=y,z=z-1.2,cmap=cmap,my_time=my_time,vmin=vmin,vmax=vmax,label =label,unit=unit, mode=self.mode,grado=self.grado)
               #plt.plot(x,min_CC[cota_min:cota_max]*0.06,'yo')
               '''
               plt.plot(z,y)
               title = 'Sophy Plot '+label+"-"+ my_time+" "+self.mode+" "+self.grado
               t = plt.title(title, fontsize=12,y=1.05)
               '''
            print("Y",len_X)
            #plt.xlim(-5,5)
            #plt.ylim(0,self.range+1)
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
                #numpy.save("/home/soporte/WRJAN2023/schain/schainpy/scripts/index.npy",arr_)
                plt.close()
        plt.show()


def main(args):
    grado      = args.grado
    parameters = args.parameters
    r_min      = args.r_min
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
        obj.setup(path_file =PATH,mode=mode,grado = grado,range=range,r_min=r_min, variable=param,save=int(save))
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
    parser.add_argument('--r_min', default=0, type=float,
                        help='Min range to plot')
    args = parser.parse_args()

    main(args)
