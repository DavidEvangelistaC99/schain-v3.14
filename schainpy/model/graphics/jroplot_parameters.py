import os
import datetime
import numpy
from mpl_toolkits.axisartist.grid_finder import FixedLocator, DictFormatter

from schainpy.model.graphics.jroplot_base import Plot, plt
from schainpy.model.graphics.jroplot_spectra import SpectraPlot, RTIPlot, CoherencePlot, SpectraCutPlot
from schainpy.utils import log
# libreria wradlib
import wradlib as wrl

EARTH_RADIUS = 6.3710e3


def ll2xy(lat1, lon1, lat2, lon2):

    p = 0.017453292519943295
    a = 0.5 - numpy.cos((lat2 - lat1) * p)/2 + numpy.cos(lat1 * p) * \
        numpy.cos(lat2 * p) * (1 - numpy.cos((lon2 - lon1) * p)) / 2
    r = 12742 * numpy.arcsin(numpy.sqrt(a))
    theta = numpy.arctan2(numpy.sin((lon2-lon1)*p)*numpy.cos(lat2*p), numpy.cos(lat1*p)
                          * numpy.sin(lat2*p)-numpy.sin(lat1*p)*numpy.cos(lat2*p)*numpy.cos((lon2-lon1)*p))
    theta = -theta + numpy.pi/2
    return r*numpy.cos(theta), r*numpy.sin(theta)


def km2deg(km):
    '''
    Convert distance in km to degrees
    '''

    return numpy.rad2deg(km/EARTH_RADIUS)



class SpectralMomentsPlot(SpectraPlot):
    '''
    Plot for Spectral Moments
    '''
    CODE = 'spc_moments'
    # colormap = 'jet'
    # plot_type = 'pcolor'

class DobleGaussianPlot(SpectraPlot):
    '''
    Plot for Double Gaussian Plot
    '''
    CODE = 'gaussian_fit'
    # colormap = 'jet'
    # plot_type = 'pcolor'

class DoubleGaussianSpectraCutPlot(SpectraCutPlot):
    '''
    Plot SpectraCut with Double Gaussian Fit
    '''
    CODE = 'cut_gaussian_fit'

class SnrPlot(RTIPlot):
    '''
    Plot for SNR Data
    '''

    CODE = 'snr'
    colormap = 'jet'

    def update(self, dataOut):

        data = {
            'snr': 10*numpy.log10(dataOut.data_snr)
        }

        return data, {}

class DopplerPlot(RTIPlot):
    '''
    Plot for DOPPLER Data (1st moment)
    '''

    CODE = 'dop'
    colormap = 'jet'

    def update(self, dataOut):

        data = {
            'dop': 10*numpy.log10(dataOut.data_dop)
        }

        return data, {}

class PowerPlot(RTIPlot):
    '''
    Plot for Power Data (0 moment)
    '''

    CODE = 'pow'
    colormap = 'jet'

    def update(self, dataOut):
        data = {
            'pow': 10*numpy.log10(dataOut.data_pow/dataOut.normFactor)
        }
        return data, {}

class SpectralWidthPlot(RTIPlot):
    '''
    Plot for Spectral Width Data (2nd moment)
    '''

    CODE = 'width'
    colormap = 'jet'

    def update(self, dataOut):

        data = {
            'width': dataOut.data_width
        }

        return data, {}

class SkyMapPlot(Plot):
    '''
    Plot for meteors detection data
    '''

    CODE = 'param'

    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.width = 7.2
        self.height = 7.2
        self.nplots = 1
        self.xlabel = 'Zonal Zenith Angle (deg)'
        self.ylabel = 'Meridional Zenith Angle (deg)'
        self.polar = True
        self.ymin = -180
        self.ymax = 180
        self.colorbar = False

    def plot(self):

        arrayParameters = numpy.concatenate(self.data['param'])
        error = arrayParameters[:, -1]
        indValid = numpy.where(error == 0)[0]
        finalMeteor = arrayParameters[indValid, :]
        finalAzimuth = finalMeteor[:, 3]
        finalZenith = finalMeteor[:, 4]

        x = finalAzimuth * numpy.pi / 180
        y = finalZenith

        ax = self.axes[0]

        if ax.firsttime:
            ax.plot = ax.plot(x, y, 'bo', markersize=5)[0]
        else:
            ax.plot.set_data(x, y)

        dt1 = self.getDateTime(self.data.min_time).strftime('%y/%m/%d %H:%M:%S')
        dt2 = self.getDateTime(self.data.max_time).strftime('%y/%m/%d %H:%M:%S')
        title = 'Meteor Detection Sky Map\n %s - %s \n Number of events: %5.0f\n' % (dt1,
                                                                                     dt2,
                                                                                     len(x))
        self.titles[0] = title


class GenericRTIPlot(Plot):
    '''
    Plot for data_xxxx object
    '''

    CODE = 'param'
    colormap = 'viridis'
    plot_type = 'pcolorbuffer'

    def setup(self):
        self.xaxis = 'time'
        self.ncols = 1
        self.nrows = self.data.shape('param')[0]
        self.nplots = self.nrows
        self.plots_adjust.update({'hspace':0.8, 'left': 0.1, 'bottom': 0.08, 'right':0.95, 'top': 0.95})

        if not self.xlabel:
            self.xlabel = 'Time'

        self.ylabel = 'Range [km]'
        if not self.titles:
            self.titles = ['Param {}'.format(x) for x in range(self.nrows)]

    def update(self, dataOut):

        data = {
            'param' : numpy.concatenate([getattr(dataOut, attr) for attr in self.attr_data], axis=0)
        }

        meta = {}

        return data, meta

    def plot(self):
        # self.data.normalize_heights()
        self.x = self.data.times
        self.y = self.data.yrange
        self.z = self.data['param']
        self.z = 10*numpy.log10(self.z)
        self.z = numpy.ma.masked_invalid(self.z)

        if self.decimation is None:
            x, y, z = self.fill_gaps(self.x, self.y, self.z)
        else:
            x, y, z = self.fill_gaps(*self.decimate())

        for n, ax in enumerate(self.axes):

            self.zmax = self.zmax if self.zmax is not None else numpy.max(
                self.z[n])
            self.zmin = self.zmin if self.zmin is not None else numpy.min(
                self.z[n])

            if ax.firsttime:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]

                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )
            else:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.collections.remove(ax.collections[0])
                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )


class PolarMapPlot(Plot):
    '''
    Plot for weather radar
    '''

    CODE = 'param'
    colormap = 'seismic'

    def setup(self):
        self.ncols = 1
        self.nrows = 1
        self.width = 9
        self.height = 8
        self.mode = self.data.meta['mode']
        if self.channels is not None:
            self.nplots = len(self.channels)
            self.nrows = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.nrows = self.nplots
            self.channels = list(range(self.nplots))
        if self.mode == 'E':
            self.xlabel = 'Longitude'
            self.ylabel = 'Latitude'
        else:
            self.xlabel = 'Range (km)'
            self.ylabel = 'Height (km)'
        self.bgcolor = 'white'
        self.cb_labels = self.data.meta['units']
        self.lat = self.data.meta['latitude']
        self.lon = self.data.meta['longitude']
        self.xmin, self.xmax = float(
            km2deg(self.xmin) + self.lon), float(km2deg(self.xmax) + self.lon)
        self.ymin, self.ymax = float(
            km2deg(self.ymin) + self.lat), float(km2deg(self.ymax) + self.lat)
        #  self.polar = True

    def plot(self):

        for n, ax in enumerate(self.axes):
            data = self.data['param'][self.channels[n]]

            zeniths = numpy.linspace(
                0, self.data.meta['max_range'], data.shape[1])
            if self.mode == 'E':
                azimuths = -numpy.radians(self.data.yrange)+numpy.pi/2
                r, theta = numpy.meshgrid(zeniths, azimuths)
                x, y = r*numpy.cos(theta)*numpy.cos(numpy.radians(self.data.meta['elevation'])), r*numpy.sin(
                    theta)*numpy.cos(numpy.radians(self.data.meta['elevation']))
                x = km2deg(x) + self.lon
                y = km2deg(y) + self.lat
            else:
                azimuths = numpy.radians(self.data.yrange)
                r, theta = numpy.meshgrid(zeniths, azimuths)
                x, y = r*numpy.cos(theta), r*numpy.sin(theta)
            self.y = zeniths

            if ax.firsttime:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.plt = ax.pcolormesh(  # r, theta, numpy.ma.array(data, mask=numpy.isnan(data)),
                    x, y, numpy.ma.array(data, mask=numpy.isnan(data)),
                    vmin=self.zmin,
                    vmax=self.zmax,
                    cmap=self.cmaps[n])
            else:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.collections.remove(ax.collections[0])
                ax.plt = ax.pcolormesh(  # r, theta, numpy.ma.array(data, mask=numpy.isnan(data)),
                    x, y, numpy.ma.array(data, mask=numpy.isnan(data)),
                    vmin=self.zmin,
                    vmax=self.zmax,
                    cmap=self.cmaps[n])

            if self.mode == 'A':
                continue

            # plot district names
            f = open('/data/workspace/schain_scripts/distrito.csv')
            for line in f:
                label, lon, lat = [s.strip() for s in line.split(',') if s]
                lat = float(lat)
                lon = float(lon)
                # ax.plot(lon, lat, '.b', ms=2)
                ax.text(lon, lat, label.decode('utf8'), ha='center',
                        va='bottom', size='8', color='black')

            # plot limites
            limites = []
            tmp = []
            for line in open('/data/workspace/schain_scripts/lima.csv'):
                if '#' in line:
                    if tmp:
                        limites.append(tmp)
                    tmp = []
                    continue
                values = line.strip().split(',')
                tmp.append((float(values[0]), float(values[1])))
            for points in limites:
                ax.add_patch(
                    Polygon(points, ec='k', fc='none', ls='--', lw=0.5))

            # plot Cuencas
            for cuenca in ('rimac', 'lurin', 'mala', 'chillon', 'chilca', 'chancay-huaral'):
                f = open('/data/workspace/schain_scripts/{}.csv'.format(cuenca))
                values = [line.strip().split(',') for line in f]
                points = [(float(s[0]), float(s[1])) for s in values]
                ax.add_patch(Polygon(points, ec='b', fc='none'))

            # plot grid
            for r in (15, 30, 45, 60):
                ax.add_artist(plt.Circle((self.lon, self.lat),
                                         km2deg(r), color='0.6', fill=False, lw=0.2))
                ax.text(
                    self.lon + (km2deg(r))*numpy.cos(60*numpy.pi/180),
                    self.lat + (km2deg(r))*numpy.sin(60*numpy.pi/180),
                    '{}km'.format(r),
                    ha='center', va='bottom', size='8', color='0.6', weight='heavy')

        if self.mode == 'E':
            title = 'El={}$^\circ$'.format(self.data.meta['elevation'])
            label = 'E{:02d}'.format(int(self.data.meta['elevation']))
        else:
            title = 'Az={}$^\circ$'.format(self.data.meta['azimuth'])
            label = 'A{:02d}'.format(int(self.data.meta['azimuth']))

        self.save_labels = ['{}-{}'.format(lbl, label) for lbl in self.labels]
        self.titles = ['{} {}'.format(
            self.data.parameters[x], title) for x in self.channels]

class WeatherPlot(Plot):
    CODE = 'weather'
    plot_name = 'weather'
    plot_type = 'ppistyle'
    buffering = False

    def setup(self):
        self.ncols = 1
        self.nrows = 1
        self.width   =8
        self.height  =8
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        self.colorbar=False
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_azi   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.08})
        self.flag    =0
        self.indicador= 0
        self.last_data_azi = None
        self.val_mean      = None

    def update(self, dataOut):

        data = {}
        meta = {}
        if hasattr(dataOut, 'dataPP_POWER'):
            factor = 1
        if hasattr(dataOut, 'nFFTPoints'):
            factor = dataOut.normFactor
        #print("DIME EL SHAPE PORFAVOR",dataOut.data_360.shape)
        data['weather'] = 10*numpy.log10(dataOut.data_360[1]/(factor))
        data['azi']     = dataOut.data_azi
        data['ele']     = dataOut.data_ele
        return data, meta

    def get2List(self,angulos):
        list1=[]
        list2=[]
        for i in reversed(range(len(angulos))):
            diff_ = angulos[i]-angulos[i-1]
            if diff_ >1.5:
                list1.append(i-1)
                list2.append(diff_)
        return list(reversed(list1)),list(reversed(list2))

    def fixData360(self,list_,ang_):
        if list_[0]==-1:
            vec = numpy.where(ang_<ang_[0])
            ang_[vec] = ang_[vec]+360
            return ang_
        return ang_

    def fixData360HL(self,angulos):
        vec = numpy.where(angulos>=360)
        angulos[vec]=angulos[vec]-360
        return angulos

    def search_pos(self,pos,list_):
        for i in range(len(list_)):
            if pos == list_[i]:
                return True,i
        i=None
        return False,i

    def fixDataComp(self,ang_,list1_,list2_):
        size  = len(ang_)
        size2 = 0
        for i in range(len(list2_)):
            size2=size2+round(list2_[i])-1
        new_size= size+size2
        ang_new = numpy.zeros(new_size)
        ang_new2 = numpy.zeros(new_size)

        tmp = 0
        c   = 0
        for i in range(len(ang_)):
            ang_new[tmp +c] = ang_[i]
            ang_new2[tmp+c] = ang_[i]
            condition , value = self.search_pos(i,list1_)
            if condition:
                pos = tmp + c + 1
                for k in range(round(list2_[value])-1):
                    ang_new[pos+k]  = ang_new[pos+k-1]+1
                    ang_new2[pos+k] = numpy.nan
                tmp = pos +k
                c   = 0
            c=c+1
        return ang_new,ang_new2

    def globalCheckPED(self,angulos):
        l1,l2 = self.get2List(angulos)
        if len(l1)>0:
            angulos2 = self.fixData360(list_=l1,ang_=angulos)
            l1,l2 = self.get2List(angulos2)

            ang1_,ang2_ = self.fixDataComp(ang_=angulos2,list1_=l1,list2_=l2)
            ang1_ = self.fixData360HL(ang1_)
            ang2_ = self.fixData360HL(ang2_)
        else:
            ang1_= angulos
            ang2_= angulos
        return ang1_,ang2_

    def analizeDATA(self,data_azi):
        list1 = []
        list2 = []
        dat   = data_azi
        for i in reversed(range(1,len(dat))):
            if dat[i]>dat[i-1]:
                diff = int(dat[i])-int(dat[i-1])
            else:
                diff = 360+int(dat[i])-int(dat[i-1])
            if diff > 1:
                list1.append(i-1)
                list2.append(diff-1)
        return list1,list2

    def fixDATANEW(self,data_azi,data_weather):
        list1,list2 = self.analizeDATA(data_azi)
        if len(list1)== 0:
            return data_azi,data_weather
        else:
            resize = 0
            for i in range(len(list2)):
                resize=  resize + list2[i]
            new_data_azi = numpy.resize(data_azi,resize)
            new_data_weather= numpy.resize(date_weather,resize)

            for i in range(len(list2)):
                j=0
                position=list1[i]+1
                for j in range(list2[i]):
                    new_data_azi[position+j]=new_data_azi[position+j-1]+1
        return new_data_azi

    def fixDATA(self,data_azi):
        data=data_azi
        for i in range(len(data)):
            if numpy.isnan(data[i]):
               data[i]=data[i-1]+1
        return data

    def replaceNAN(self,data_weather,data_azi,val):
        data= data_azi
        data_T= data_weather
        if data.shape[0]> data_T.shape[0]:
            data_N = numpy.ones( [data.shape[0],data_T.shape[1]])
            c      = 0
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                    data_N[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
                else:
                    data_N[i,:]=data_T[c,:]
                    c=c+1
            return data_N
        else:
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                   data_T[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
            return data_T

    def const_ploteo(self,data_weather,data_azi,step,res):
        if self.ini==0:
            #-------
            n     = (360/res)-len(data_azi)
            #--------------------- new -------------------------
            data_azi_new ,data_azi_old= self.globalCheckPED(data_azi)
            #------------------------
            start = data_azi_new[-1] + res
            end   = data_azi_new[0]  - res
            #------ new
            self.last_data_azi = end
            if start>end:
                end        = end + 360
            azi_vacia = numpy.linspace(start,end,int(n))
            azi_vacia = numpy.where(azi_vacia>360,azi_vacia-360,azi_vacia)
            data_azi  = numpy.hstack((data_azi_new,azi_vacia))
            # RADAR
            val_mean         = numpy.mean(data_weather[:,-1])
            self.val_mean    = val_mean
            data_weather_cmp = numpy.ones([(360-data_weather.shape[0]),data_weather.shape[1]])*val_mean
            data_weather     = self.replaceNAN(data_weather=data_weather,data_azi=data_azi_old,val=self.val_mean)
            data_weather     = numpy.vstack((data_weather,data_weather_cmp))
        else:
            # azimuth
            flag=0
            start_azi = self.res_azi[0]
            #-----------new------------
            data_azi ,data_azi_old= self.globalCheckPED(data_azi)
            data_weather = self.replaceNAN(data_weather=data_weather,data_azi=data_azi_old,val=self.val_mean)
            #--------------------------
            start = data_azi[0]
            end   = data_azi[-1]
            self.last_data_azi= end
            if start< start_azi:
                start = start +360
            if end <start_azi:
                end  = end +360

            pos_ini = int((start-start_azi)/res)
            len_azi = len(data_azi)
            if (360-pos_ini)<len_azi:
                if pos_ini+1==360:
                    pos_ini=0
                else:
                    flag=1
                    dif= 360-pos_ini
                    comp= len_azi-dif
            #-----------------
            if flag==0:
                # AZIMUTH
                self.res_azi[pos_ini:pos_ini+len_azi] = data_azi
                # RADAR
                self.res_weather[pos_ini:pos_ini+len_azi,:] = data_weather
            else:
                # AZIMUTH
                self.res_azi[pos_ini:pos_ini+dif] = data_azi[0:dif]
                self.res_azi[0:comp]              = data_azi[dif:]
                # RADAR
                self.res_weather[pos_ini:pos_ini+dif,:] = data_weather[0:dif,:]
                self.res_weather[0:comp,:]              = data_weather[dif:,:]
                flag=0
            data_azi                                    = self.res_azi
            data_weather                                = self.res_weather

        return data_weather,data_azi

    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        data         = self.data[-1]
        r            = self.data.yrange
        delta_height = r[1]-r[0]
        r_mask       = numpy.where(r>=0)[0]
        r            = numpy.arange(len(r_mask))*delta_height
        self.y       = 2*r
        # RADAR
        #data_weather = data['weather']
        # PEDESTAL
        #data_azi  = data['azi']
        res          = 1
        # STEP
        step         = (360/(res*data['weather'].shape[0]))

        self.res_weather, self.res_azi = self.const_ploteo(data_weather=data['weather'][:,r_mask],data_azi=data['azi'],step=step,res=res)
        self.res_ele = numpy.mean(data['ele'])
        #################    PLOTEO           ###################
        for i,ax in enumerate(self.axes):
            self.zmin = self.zmin if self.zmin else 20
            self.zmax = self.zmax if self.zmax else 80
            if ax.firsttime:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.res_weather,r=r,az=self.res_azi,fig=self.figures[0], proj='cg', vmin=self.zmin, vmax=self.zmax)
            else:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.res_weather,r=r,az=self.res_azi,fig=self.figures[0], proj='cg', vmin=self.zmin, vmax=self.zmax)
        caax = cgax.parasites[0]
        paax = cgax.parasites[1]
        cbar = plt.gcf().colorbar(pm, pad=0.075)
        caax.set_xlabel('x_range [km]')
        caax.set_ylabel('y_range [km]')
        plt.text(1.0, 1.05, 'Azimuth '+str(thisDatetime)+"  Step   "+str(self.ini)+ " EL: "+str(round(self.res_ele, 1)), transform=caax.transAxes, va='bottom',ha='right')

        self.ini= self.ini+1


class WeatherRHIPlot(Plot):
    CODE = 'weather'
    plot_name = 'weather'
    plot_type = 'rhistyle'
    buffering = False
    data_ele_tmp = None

    def setup(self):
        print("********************")
        print("********************")
        print("********************")
        print("SETUP WEATHER PLOT")
        self.ncols = 1
        self.nrows = 1
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        if self.channels is not None:
            self.nplots = len(self.channels)
            self.nrows = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.nrows = self.nplots
            self.channels = list(range(self.nplots))
        print("channels",self.channels)
        print("que saldra", self.data.shape(self.CODE)[0])
        self.titles = ['{} Channel {}'.format(self.CODE.upper(), x) for x in range(self.nrows)]
        print("self.titles",self.titles)
        self.colorbar=False
        self.width   =12
        self.height  =8
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_ele   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.08})
        self.flag    =0
        self.indicador= 0
        self.last_data_ele = None
        self.val_mean      = None

    def update(self, dataOut):

        data = {}
        meta = {}
        if hasattr(dataOut, 'dataPP_POWER'):
            factor = 1
        if hasattr(dataOut, 'nFFTPoints'):
            factor = dataOut.normFactor
        print("dataOut",dataOut.data_360.shape)
        #
        data['weather'] = 10*numpy.log10(dataOut.data_360/(factor))
        #
        #data['weather'] = 10*numpy.log10(dataOut.data_360[1]/(factor))
        data['azi']     = dataOut.data_azi
        data['ele']     = dataOut.data_ele
        #print("UPDATE")
        #print("data[weather]",data['weather'].shape)
        #print("data[azi]",data['azi'])
        return data, meta

    def get2List(self,angulos):
        list1=[]
        list2=[]
        for i in reversed(range(len(angulos))):
            if not i==0:#el caso de i=0 evalula el primero de la lista con el ultimo y no es relevante
                diff_ = angulos[i]-angulos[i-1]
                if abs(diff_) >1.5:
                    list1.append(i-1)
                    list2.append(diff_)
        return list(reversed(list1)),list(reversed(list2))

    def fixData90(self,list_,ang_):
        if list_[0]==-1:
            vec = numpy.where(ang_<ang_[0])
            ang_[vec] = ang_[vec]+90
            return ang_
        return ang_

    def fixData90HL(self,angulos):
        vec = numpy.where(angulos>=90)
        angulos[vec]=angulos[vec]-90
        return angulos


    def search_pos(self,pos,list_):
        for i in range(len(list_)):
            if pos == list_[i]:
                return True,i
        i=None
        return False,i

    def fixDataComp(self,ang_,list1_,list2_,tipo_case):
        size  = len(ang_)
        size2 = 0
        for i in range(len(list2_)):
            size2=size2+round(abs(list2_[i]))-1
        new_size= size+size2
        ang_new = numpy.zeros(new_size)
        ang_new2 = numpy.zeros(new_size)

        tmp = 0
        c   = 0
        for i in range(len(ang_)):
            ang_new[tmp +c] = ang_[i]
            ang_new2[tmp+c] = ang_[i]
            condition , value = self.search_pos(i,list1_)
            if condition:
                pos = tmp + c + 1
                for k in range(round(abs(list2_[value]))-1):
                    if tipo_case==0 or tipo_case==3:#subida
                        ang_new[pos+k]  = ang_new[pos+k-1]+1
                        ang_new2[pos+k] = numpy.nan
                    elif tipo_case==1 or tipo_case==2:#bajada
                        ang_new[pos+k]  = ang_new[pos+k-1]-1
                        ang_new2[pos+k] = numpy.nan

                tmp = pos +k
                c   = 0
            c=c+1
        return ang_new,ang_new2

    def globalCheckPED(self,angulos,tipo_case):
        l1,l2 = self.get2List(angulos)
        ##print("l1",l1)
        ##print("l2",l2)
        if len(l1)>0:
            #angulos2 = self.fixData90(list_=l1,ang_=angulos)
            #l1,l2 = self.get2List(angulos2)
            ang1_,ang2_ = self.fixDataComp(ang_=angulos,list1_=l1,list2_=l2,tipo_case=tipo_case)
            #ang1_ = self.fixData90HL(ang1_)
            #ang2_ = self.fixData90HL(ang2_)
        else:
            ang1_= angulos
            ang2_= angulos
        return ang1_,ang2_


    def replaceNAN(self,data_weather,data_ele,val):
        data= data_ele
        data_T= data_weather
        if data.shape[0]> data_T.shape[0]:
            data_N = numpy.ones( [data.shape[0],data_T.shape[1]])
            c      = 0
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                    data_N[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
                else:
                    data_N[i,:]=data_T[c,:]
                    c=c+1
            return data_N
        else:
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                   data_T[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
            return data_T

    def check_case(self,data_ele,ang_max,ang_min):
        start  = data_ele[0]
        end    = data_ele[-1]
        number = (end-start)
        len_ang=len(data_ele)
        print("start",start)
        print("end",end)
        print("number",number)

        print("len_ang",len_ang)

        #exit(1)

        if start<end and (round(abs(number)+1)>=len_ang or (numpy.argmin(data_ele)==0)):#caso subida
            return 0
        #elif start>end and (round(abs(number)+1)>=len_ang or(numpy.argmax(data_ele)==0)):#caso bajada
        #    return 1
        elif round(abs(number)+1)>=len_ang and (start>end or(numpy.argmax(data_ele)==0)):#caso bajada
            return 1
        elif round(abs(number)+1)<len_ang and data_ele[-2]>data_ele[-1]:# caso BAJADA CAMBIO ANG MAX
            return 2
        elif round(abs(number)+1)<len_ang and data_ele[-2]<data_ele[-1] :# caso SUBIDA CAMBIO ANG MIN
            return 3


    def const_ploteo(self,val_ch,data_weather,data_ele,step,res,ang_max,ang_min):
        ang_max= ang_max
        ang_min= ang_min
        data_weather=data_weather
        val_ch=val_ch
        ##print("*********************DATA WEATHER**************************************")
        ##print(data_weather)
        if self.ini==0:
            '''
            print("**********************************************")
            print("**********************************************")
            print("***************ini**************")
            print("**********************************************")
            print("**********************************************")
            '''
            #print("data_ele",data_ele)
            #----------------------------------------------------------
            tipo_case = self.check_case(data_ele,ang_max,ang_min)
            print("check_case",tipo_case)
            #exit(1)
            #--------------------- new -------------------------
            data_ele_new ,data_ele_old= self.globalCheckPED(data_ele,tipo_case)

            #-------------------------CAMBIOS RHI---------------------------------
            start= ang_min
            end  = ang_max
            n= (ang_max-ang_min)/res
            #------ new
            self.start_data_ele = data_ele_new[0]
            self.end_data_ele  = data_ele_new[-1]
            if tipo_case==0  or tipo_case==3: # SUBIDA
                n1= round(self.start_data_ele)- start
                n2= end - round(self.end_data_ele)
                print(self.start_data_ele)
                print(self.end_data_ele)
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,self.start_data_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    print("ele1_nan",ele1_nan.shape)
                    print("data_ele_old",data_ele_old.shape)
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_old))
                if n2>0:
                    ele2= numpy.linspace(self.end_data_ele+1,end,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    print("ele2_nan",ele2_nan.shape)
                    print("data_ele_old",data_ele_old.shape)
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

            if tipo_case==1  or tipo_case==2: # BAJADA
                data_ele_new       = data_ele_new[::-1] #  reversa
                data_ele_old   = data_ele_old[::-1]# reversa
                data_weather   = data_weather[::-1,:]# reversa
                vec= numpy.where(data_ele_new<ang_max)
                data_ele_new = data_ele_new[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]
                vec2= numpy.where(0<data_ele_new)
                data_ele_new = data_ele_new[vec2]
                data_ele_old = data_ele_old[vec2]
                data_weather  = data_weather[vec2[0]]
                self.start_data_ele = data_ele_new[0]
                self.end_data_ele  = data_ele_new[-1]

                n1= round(self.start_data_ele)- start
                n2= end - round(self.end_data_ele)-1
                print(self.start_data_ele)
                print(self.end_data_ele)
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,self.start_data_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_old))
                if n2>0:
                    ele2= numpy.linspace(self.end_data_ele+1,end,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))
            # RADAR
            # NOTA data_ele y data_weather es la variable que retorna
            val_mean         = numpy.mean(data_weather[:,-1])
            self.val_mean    = val_mean
            data_weather     = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
            self.data_ele_tmp[val_ch]= data_ele_old
        else:
            #print("**********************************************")
            #print("****************VARIABLE**********************")
            #-------------------------CAMBIOS RHI---------------------------------
            #---------------------------------------------------------------------
            ##print("INPUT data_ele",data_ele)
            flag=0
            start_ele = self.res_ele[0]
            tipo_case = self.check_case(data_ele,ang_max,ang_min)
            #print("TIPO DE DATA",tipo_case)
            #-----------new------------
            data_ele ,data_ele_old = self.globalCheckPED(data_ele,tipo_case)
            data_weather           = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)

            #-------------------------------NEW RHI ITERATIVO-------------------------

            if tipo_case==0 : # SUBIDA
                vec = numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]

                vec2 = numpy.where(0<data_ele)
                data_ele= data_ele[vec2]
                data_ele_old= data_ele_old[vec2]
                ##print(data_ele_new)
                data_weather= data_weather[vec2[0]]

                new_i_ele  = int(round(data_ele[0]))
                new_f_ele  = int(round(data_ele[-1]))
                #print(new_i_ele)
                #print(new_f_ele)
                #print(data_ele,len(data_ele))
                #print(data_ele_old,len(data_ele_old))
                if new_i_ele< 2:
                    self.data_ele_tmp[val_ch] = numpy.ones(ang_max-ang_min)*numpy.nan
                    self.res_weather[val_ch]  = self.replaceNAN(data_weather=self.res_weather[val_ch],data_ele=self.data_ele_tmp[val_ch],val=self.val_mean)
                self.data_ele_tmp[val_ch][new_i_ele:new_i_ele+len(data_ele)]=data_ele_old
                self.res_ele[new_i_ele:new_i_ele+len(data_ele)]= data_ele
                self.res_weather[val_ch][new_i_ele:new_i_ele+len(data_ele),:]= data_weather
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]

            elif tipo_case==1 : #BAJADA
                data_ele       = data_ele[::-1] #  reversa
                data_ele_old   = data_ele_old[::-1]# reversa
                data_weather   = data_weather[::-1,:]# reversa
                vec= numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]
                vec2= numpy.where(0<data_ele)
                data_ele = data_ele[vec2]
                data_ele_old = data_ele_old[vec2]
                data_weather  = data_weather[vec2[0]]


                new_i_ele  = int(round(data_ele[0]))
                new_f_ele  = int(round(data_ele[-1]))
                #print(data_ele)
                #print(ang_max)
                #print(data_ele_old)
                if new_i_ele <= 1:
                    new_i_ele = 1
                if round(data_ele[-1])>=ang_max-1:
                    self.data_ele_tmp[val_ch] = numpy.ones(ang_max-ang_min)*numpy.nan
                    self.res_weather[val_ch]  = self.replaceNAN(data_weather=self.res_weather[val_ch],data_ele=self.data_ele_tmp[val_ch],val=self.val_mean)
                self.data_ele_tmp[val_ch][new_i_ele-1:new_i_ele+len(data_ele)-1]=data_ele_old
                self.res_ele[new_i_ele-1:new_i_ele+len(data_ele)-1]= data_ele
                self.res_weather[val_ch][new_i_ele-1:new_i_ele+len(data_ele)-1,:]= data_weather
                data_ele     = self.res_ele
                data_weather = self.res_weather[val_ch]

            elif tipo_case==2:  #bajada
                vec = numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_weather= data_weather[vec[0]]

                len_vec = len(vec)
                data_ele_new     = data_ele[::-1] #  reversa
                data_weather =  data_weather[::-1,:]
                new_i_ele  = int(data_ele_new[0])
                new_f_ele  = int(data_ele_new[-1])

                n1= new_i_ele- ang_min
                n2= ang_max - new_f_ele-1
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
                if n2>0:
                    ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

                self.data_ele_tmp[val_ch] = data_ele_old
                self.res_ele      = data_ele
                self.res_weather[val_ch]  = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]

            elif tipo_case==3:#subida
                vec = numpy.where(0<data_ele)
                data_ele= data_ele[vec]
                data_ele_new = data_ele
                data_ele_old= data_ele_old[vec]
                data_weather= data_weather[vec[0]]
                pos_ini = numpy.argmin(data_ele)
                if pos_ini>0:
                    len_vec= len(data_ele)
                    vec3  = numpy.linspace(pos_ini,len_vec-1,len_vec-pos_ini).astype(int)
                    #print(vec3)
                    data_ele= data_ele[vec3]
                    data_ele_new = data_ele
                    data_ele_old= data_ele_old[vec3]
                    data_weather= data_weather[vec3]

                new_i_ele  = int(data_ele_new[0])
                new_f_ele  = int(data_ele_new[-1])
                n1= new_i_ele- ang_min
                n2= ang_max - new_f_ele-1
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
                if n2>0:
                    ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

                self.data_ele_tmp[val_ch] = data_ele_old
                self.res_ele      = data_ele
                self.res_weather[val_ch]  = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]
        #print("self.data_ele_tmp",self.data_ele_tmp)
        return data_weather,data_ele


    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        data         = self.data[-1]
        r            = self.data.yrange
        delta_height = r[1]-r[0]
        r_mask       = numpy.where(r>=0)[0]
        ##print("delta_height",delta_height)
        #print("r_mask",r_mask,len(r_mask))
        r            = numpy.arange(len(r_mask))*delta_height
        self.y       = 2*r
        res          = 1
        ###print("data['weather'].shape[0]",data['weather'].shape[0])
        ang_max = self.ang_max
        ang_min = self.ang_min
        var_ang      =ang_max -  ang_min
        step         = (int(var_ang)/(res*data['weather'].shape[0]))
        ###print("step",step)
        #--------------------------------------------------------
        ##print('weather',data['weather'].shape)
        ##print('ele',data['ele'].shape)

        ###self.res_weather, self.res_ele = self.const_ploteo(data_weather=data['weather'][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min)
        ###self.res_azi                   = numpy.mean(data['azi'])
        ###print("self.res_ele",self.res_ele)
        plt.clf()
        subplots = [121, 122]
        cg={'angular_spacing': 20.}
        if self.ini==0:
            self.data_ele_tmp = numpy.ones([self.nplots,int(var_ang)])*numpy.nan
            self.res_weather= numpy.ones([self.nplots,int(var_ang),len(r_mask)])*numpy.nan
            print("SHAPE",self.data_ele_tmp.shape)

        for i,ax in enumerate(self.axes):
            self.res_weather[i], self.res_ele = self.const_ploteo(val_ch=i, data_weather=data['weather'][i][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min)
            self.res_azi                   = numpy.mean(data['azi'])
            if i==0:
                print("*****************************************************************************to plot**************************",self.res_weather[i].shape)
            self.zmin = self.zmin if self.zmin else 20
            self.zmax = self.zmax if self.zmax else 80
            if ax.firsttime:
                #plt.clf()
                cgax, pm = wrl.vis.plot_rhi(self.res_weather[i],r=r,th=self.res_ele,ax=subplots[i], proj=cg,vmin=self.zmin, vmax=self.zmax)
                #fig=self.figures[0]
            else:
                #plt.clf()
                if i==0:
                    print(self.res_weather[i])
                    print(self.res_ele)
                cgax, pm = wrl.vis.plot_rhi(self.res_weather[i],r=r,th=self.res_ele,ax=subplots[i], proj=cg,vmin=self.zmin, vmax=self.zmax)
            caax = cgax.parasites[0]
            paax = cgax.parasites[1]
            cbar = plt.gcf().colorbar(pm, pad=0.075)
            caax.set_xlabel('x_range [km]')
            caax.set_ylabel('y_range [km]')
            plt.text(1.0, 1.05, 'Elevacion '+str(thisDatetime)+"  Step   "+str(self.ini)+ " Azi: "+str(round(self.res_azi,2)), transform=caax.transAxes, va='bottom',ha='right')
        print("***************************self.ini****************************",self.ini)
        self.ini= self.ini+1

class WeatherRHI_vRF2_Plot(Plot):
    CODE = 'weather'
    plot_name = 'weather'
    plot_type = 'rhistyle'
    buffering = False
    data_ele_tmp = None

    def setup(self):
        print("********************")
        print("********************")
        print("********************")
        print("SETUP WEATHER PLOT")
        self.ncols = 1
        self.nrows = 1
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        if self.channels is not None:
            self.nplots = len(self.channels)
            self.nrows = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.nrows = self.nplots
            self.channels = list(range(self.nplots))
        print("channels",self.channels)
        print("que saldra", self.data.shape(self.CODE)[0])
        self.titles = ['{} Channel {}'.format(self.CODE.upper(), x) for x in range(self.nrows)]
        print("self.titles",self.titles)
        self.colorbar=False
        self.width   =8
        self.height  =8
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_ele   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.08})
        self.flag    =0
        self.indicador= 0
        self.last_data_ele = None
        self.val_mean      = None

    def update(self, dataOut):

        data = {}
        meta = {}
        if hasattr(dataOut, 'dataPP_POWER'):
            factor = 1
        if hasattr(dataOut, 'nFFTPoints'):
            factor = dataOut.normFactor
        print("dataOut",dataOut.data_360.shape)
        #
        data['weather'] = 10*numpy.log10(dataOut.data_360/(factor))
        #
        #data['weather'] = 10*numpy.log10(dataOut.data_360[1]/(factor))
        data['azi']     = dataOut.data_azi
        data['ele']     = dataOut.data_ele
        data['case_flag']     = dataOut.case_flag
        #print("UPDATE")
        #print("data[weather]",data['weather'].shape)
        #print("data[azi]",data['azi'])
        return data, meta

    def get2List(self,angulos):
        list1=[]
        list2=[]
        for i in reversed(range(len(angulos))):
            if not i==0:#el caso de i=0 evalula el primero de la lista con el ultimo y no es relevante
                diff_ = angulos[i]-angulos[i-1]
                if abs(diff_) >1.5:
                    list1.append(i-1)
                    list2.append(diff_)
        return list(reversed(list1)),list(reversed(list2))

    def fixData90(self,list_,ang_):
        if list_[0]==-1:
            vec = numpy.where(ang_<ang_[0])
            ang_[vec] = ang_[vec]+90
            return ang_
        return ang_

    def fixData90HL(self,angulos):
        vec = numpy.where(angulos>=90)
        angulos[vec]=angulos[vec]-90
        return angulos


    def search_pos(self,pos,list_):
        for i in range(len(list_)):
            if pos == list_[i]:
                return True,i
        i=None
        return False,i

    def fixDataComp(self,ang_,list1_,list2_,tipo_case):
        size  = len(ang_)
        size2 = 0
        for i in range(len(list2_)):
            size2=size2+round(abs(list2_[i]))-1
        new_size= size+size2
        ang_new = numpy.zeros(new_size)
        ang_new2 = numpy.zeros(new_size)

        tmp = 0
        c   = 0
        for i in range(len(ang_)):
            ang_new[tmp +c] = ang_[i]
            ang_new2[tmp+c] = ang_[i]
            condition , value = self.search_pos(i,list1_)
            if condition:
                pos = tmp + c + 1
                for k in range(round(abs(list2_[value]))-1):
                    if tipo_case==0 or tipo_case==3:#subida
                        ang_new[pos+k]  = ang_new[pos+k-1]+1
                        ang_new2[pos+k] = numpy.nan
                    elif tipo_case==1 or tipo_case==2:#bajada
                        ang_new[pos+k]  = ang_new[pos+k-1]-1
                        ang_new2[pos+k] = numpy.nan

                tmp = pos +k
                c   = 0
            c=c+1
        return ang_new,ang_new2

    def globalCheckPED(self,angulos,tipo_case):
        l1,l2 = self.get2List(angulos)
        ##print("l1",l1)
        ##print("l2",l2)
        if len(l1)>0:
            #angulos2 = self.fixData90(list_=l1,ang_=angulos)
            #l1,l2 = self.get2List(angulos2)
            ang1_,ang2_ = self.fixDataComp(ang_=angulos,list1_=l1,list2_=l2,tipo_case=tipo_case)
            #ang1_ = self.fixData90HL(ang1_)
            #ang2_ = self.fixData90HL(ang2_)
        else:
            ang1_= angulos
            ang2_= angulos
        return ang1_,ang2_


    def replaceNAN(self,data_weather,data_ele,val):
        data= data_ele
        data_T= data_weather
        if data.shape[0]> data_T.shape[0]:
            data_N = numpy.ones( [data.shape[0],data_T.shape[1]])
            c      = 0
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                    data_N[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
                else:
                    data_N[i,:]=data_T[c,:]
                    c=c+1
            return data_N
        else:
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                   data_T[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
            return data_T

    def check_case(self,data_ele,ang_max,ang_min):
        start  = data_ele[0]
        end    = data_ele[-1]
        number = (end-start)
        len_ang=len(data_ele)
        print("start",start)
        print("end",end)
        print("number",number)

        print("len_ang",len_ang)

        #exit(1)

        if start<end and (round(abs(number)+1)>=len_ang or (numpy.argmin(data_ele)==0)):#caso subida
            return 0
        #elif start>end and (round(abs(number)+1)>=len_ang or(numpy.argmax(data_ele)==0)):#caso bajada
        #    return 1
        elif round(abs(number)+1)>=len_ang and (start>end or(numpy.argmax(data_ele)==0)):#caso bajada
            return 1
        elif round(abs(number)+1)<len_ang and data_ele[-2]>data_ele[-1]:# caso BAJADA CAMBIO ANG MAX
            return 2
        elif round(abs(number)+1)<len_ang and data_ele[-2]<data_ele[-1] :# caso SUBIDA CAMBIO ANG MIN
            return 3


    def const_ploteo(self,val_ch,data_weather,data_ele,step,res,ang_max,ang_min,case_flag):
        ang_max= ang_max
        ang_min= ang_min
        data_weather=data_weather
        val_ch=val_ch
        ##print("*********************DATA WEATHER**************************************")
        ##print(data_weather)
        if self.ini==0:
            '''
            print("**********************************************")
            print("**********************************************")
            print("***************ini**************")
            print("**********************************************")
            print("**********************************************")
            '''
            #print("data_ele",data_ele)
            #----------------------------------------------------------
            tipo_case = case_flag[-1]
            #tipo_case = self.check_case(data_ele,ang_max,ang_min)
            print("check_case",tipo_case)
            #exit(1)
            #--------------------- new -------------------------
            data_ele_new ,data_ele_old= self.globalCheckPED(data_ele,tipo_case)

            #-------------------------CAMBIOS RHI---------------------------------
            start= ang_min
            end  = ang_max
            n= (ang_max-ang_min)/res
            #------ new
            self.start_data_ele = data_ele_new[0]
            self.end_data_ele  = data_ele_new[-1]
            if tipo_case==0  or tipo_case==3: # SUBIDA
                n1= round(self.start_data_ele)- start
                n2= end - round(self.end_data_ele)
                print(self.start_data_ele)
                print(self.end_data_ele)
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,self.start_data_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    print("ele1_nan",ele1_nan.shape)
                    print("data_ele_old",data_ele_old.shape)
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_old))
                if n2>0:
                    ele2= numpy.linspace(self.end_data_ele+1,end,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    print("ele2_nan",ele2_nan.shape)
                    print("data_ele_old",data_ele_old.shape)
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

            if tipo_case==1  or tipo_case==2: # BAJADA
                data_ele_new       = data_ele_new[::-1] #  reversa
                data_ele_old   = data_ele_old[::-1]# reversa
                data_weather   = data_weather[::-1,:]# reversa
                vec= numpy.where(data_ele_new<ang_max)
                data_ele_new = data_ele_new[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]
                vec2= numpy.where(0<data_ele_new)
                data_ele_new = data_ele_new[vec2]
                data_ele_old = data_ele_old[vec2]
                data_weather  = data_weather[vec2[0]]
                self.start_data_ele = data_ele_new[0]
                self.end_data_ele  = data_ele_new[-1]

                n1= round(self.start_data_ele)- start
                n2= end - round(self.end_data_ele)-1
                print(self.start_data_ele)
                print(self.end_data_ele)
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,self.start_data_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_old))
                if n2>0:
                    ele2= numpy.linspace(self.end_data_ele+1,end,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))
            # RADAR
            # NOTA data_ele y data_weather es la variable que retorna
            val_mean         = numpy.mean(data_weather[:,-1])
            self.val_mean    = val_mean
            data_weather     = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
            print("eleold",data_ele_old)
            print(self.data_ele_tmp[val_ch])
            print(data_ele_old.shape[0])
            print(self.data_ele_tmp[val_ch].shape[0])
            if (data_ele_old.shape[0]==91 or self.data_ele_tmp[val_ch].shape[0]==91):
                import sys
                print("EXIT",self.ini)

                sys.exit(1)
            self.data_ele_tmp[val_ch]= data_ele_old
        else:
            #print("**********************************************")
            #print("****************VARIABLE**********************")
            #-------------------------CAMBIOS RHI---------------------------------
            #---------------------------------------------------------------------
            ##print("INPUT data_ele",data_ele)
            flag=0
            start_ele = self.res_ele[0]
            #tipo_case = self.check_case(data_ele,ang_max,ang_min)
            tipo_case = case_flag[-1]
            #print("TIPO DE DATA",tipo_case)
            #-----------new------------
            data_ele ,data_ele_old = self.globalCheckPED(data_ele,tipo_case)
            data_weather           = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)

            #-------------------------------NEW RHI ITERATIVO-------------------------

            if tipo_case==0 : # SUBIDA
                vec = numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]

                vec2 = numpy.where(0<data_ele)
                data_ele= data_ele[vec2]
                data_ele_old= data_ele_old[vec2]
                ##print(data_ele_new)
                data_weather= data_weather[vec2[0]]

                new_i_ele  = int(round(data_ele[0]))
                new_f_ele  = int(round(data_ele[-1]))
                #print(new_i_ele)
                #print(new_f_ele)
                #print(data_ele,len(data_ele))
                #print(data_ele_old,len(data_ele_old))
                if new_i_ele< 2:
                    self.data_ele_tmp[val_ch] = numpy.ones(ang_max-ang_min)*numpy.nan
                    self.res_weather[val_ch]  = self.replaceNAN(data_weather=self.res_weather[val_ch],data_ele=self.data_ele_tmp[val_ch],val=self.val_mean)
                self.data_ele_tmp[val_ch][new_i_ele:new_i_ele+len(data_ele)]=data_ele_old
                self.res_ele[new_i_ele:new_i_ele+len(data_ele)]= data_ele
                self.res_weather[val_ch][new_i_ele:new_i_ele+len(data_ele),:]= data_weather
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]

            elif tipo_case==1 : #BAJADA
                data_ele       = data_ele[::-1] #  reversa
                data_ele_old   = data_ele_old[::-1]# reversa
                data_weather   = data_weather[::-1,:]# reversa
                vec= numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]
                vec2= numpy.where(0<data_ele)
                data_ele = data_ele[vec2]
                data_ele_old = data_ele_old[vec2]
                data_weather  = data_weather[vec2[0]]


                new_i_ele  = int(round(data_ele[0]))
                new_f_ele  = int(round(data_ele[-1]))
                #print(data_ele)
                #print(ang_max)
                #print(data_ele_old)
                if new_i_ele <= 1:
                    new_i_ele = 1
                if round(data_ele[-1])>=ang_max-1:
                    self.data_ele_tmp[val_ch] = numpy.ones(ang_max-ang_min)*numpy.nan
                    self.res_weather[val_ch]  = self.replaceNAN(data_weather=self.res_weather[val_ch],data_ele=self.data_ele_tmp[val_ch],val=self.val_mean)
                self.data_ele_tmp[val_ch][new_i_ele-1:new_i_ele+len(data_ele)-1]=data_ele_old
                self.res_ele[new_i_ele-1:new_i_ele+len(data_ele)-1]= data_ele
                self.res_weather[val_ch][new_i_ele-1:new_i_ele+len(data_ele)-1,:]= data_weather
                data_ele     = self.res_ele
                data_weather = self.res_weather[val_ch]

            elif tipo_case==2:  #bajada
                vec = numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_weather= data_weather[vec[0]]

                len_vec = len(vec)
                data_ele_new     = data_ele[::-1] #  reversa
                data_weather =  data_weather[::-1,:]
                new_i_ele  = int(data_ele_new[0])
                new_f_ele  = int(data_ele_new[-1])

                n1= new_i_ele- ang_min
                n2= ang_max - new_f_ele-1
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
                if n2>0:
                    ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

                self.data_ele_tmp[val_ch] = data_ele_old
                self.res_ele      = data_ele
                self.res_weather[val_ch]  = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]

            elif tipo_case==3:#subida
                vec = numpy.where(0<data_ele)
                data_ele= data_ele[vec]
                data_ele_new = data_ele
                data_ele_old= data_ele_old[vec]
                data_weather= data_weather[vec[0]]
                pos_ini = numpy.argmin(data_ele)
                if pos_ini>0:
                    len_vec= len(data_ele)
                    vec3  = numpy.linspace(pos_ini,len_vec-1,len_vec-pos_ini).astype(int)
                    #print(vec3)
                    data_ele= data_ele[vec3]
                    data_ele_new = data_ele
                    data_ele_old= data_ele_old[vec3]
                    data_weather= data_weather[vec3]

                new_i_ele  = int(data_ele_new[0])
                new_f_ele  = int(data_ele_new[-1])
                n1= new_i_ele- ang_min
                n2= ang_max - new_f_ele-1
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
                if n2>0:
                    ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

                self.data_ele_tmp[val_ch] = data_ele_old
                self.res_ele      = data_ele
                self.res_weather[val_ch]  = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]
        #print("self.data_ele_tmp",self.data_ele_tmp)
        return data_weather,data_ele


    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        data         = self.data[-1]
        r            = self.data.yrange
        delta_height = r[1]-r[0]
        r_mask       = numpy.where(r>=0)[0]
        ##print("delta_height",delta_height)
        #print("r_mask",r_mask,len(r_mask))
        r            = numpy.arange(len(r_mask))*delta_height
        self.y       = 2*r
        res          = 1
        ###print("data['weather'].shape[0]",data['weather'].shape[0])
        ang_max = self.ang_max
        ang_min = self.ang_min
        var_ang      =ang_max -  ang_min
        step         = (int(var_ang)/(res*data['weather'].shape[0]))
        ###print("step",step)
        #--------------------------------------------------------
        ##print('weather',data['weather'].shape)
        ##print('ele',data['ele'].shape)

        ###self.res_weather, self.res_ele = self.const_ploteo(data_weather=data['weather'][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min)
        ###self.res_azi                   = numpy.mean(data['azi'])
        ###print("self.res_ele",self.res_ele)
        plt.clf()
        subplots = [121, 122]
        try:
            if self.data[-2]['ele'].max()<data['ele'].max():
                self.ini=0
        except:
            pass
        if self.ini==0:
            self.data_ele_tmp = numpy.ones([self.nplots,int(var_ang)])*numpy.nan
            self.res_weather= numpy.ones([self.nplots,int(var_ang),len(r_mask)])*numpy.nan
            print("SHAPE",self.data_ele_tmp.shape)

        for i,ax in enumerate(self.axes):
            self.res_weather[i], self.res_ele = self.const_ploteo(val_ch=i, data_weather=data['weather'][i][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min,case_flag=self.data['case_flag'])
            self.res_azi                   = numpy.mean(data['azi'])

            if ax.firsttime:
                #plt.clf()
                print("Frist Plot")
                cgax, pm = wrl.vis.plot_rhi(self.res_weather[i],r=r,th=self.res_ele,ax=subplots[i], proj='cg',vmin=20, vmax=80)
                #fig=self.figures[0]
            else:
                #plt.clf()
                print("ELSE PLOT")
                cgax, pm = wrl.vis.plot_rhi(self.res_weather[i],r=r,th=self.res_ele,ax=subplots[i], proj='cg',vmin=20, vmax=80)
            caax = cgax.parasites[0]
            paax = cgax.parasites[1]
            cbar = plt.gcf().colorbar(pm, pad=0.075)
            caax.set_xlabel('x_range [km]')
            caax.set_ylabel('y_range [km]')
            plt.text(1.0, 1.05, 'Elevacion '+str(thisDatetime)+"  Step   "+str(self.ini)+ " Azi: "+str(round(self.res_azi,2)), transform=caax.transAxes, va='bottom',ha='right')
        print("***************************self.ini****************************",self.ini)
        self.ini= self.ini+1

class WeatherRHI_vRF_Plot(Plot):
    CODE = 'weather'
    plot_name = 'weather'
    plot_type = 'rhistyle'
    buffering = False
    data_ele_tmp = None

    def setup(self):
        print("********************")
        print("********************")
        print("********************")
        print("SETUP WEATHER PLOT")
        self.ncols = 1
        self.nrows = 1
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        if self.channels is not None:
            self.nplots = len(self.channels)
            self.nrows = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.nrows = self.nplots
            self.channels = list(range(self.nplots))
        print("channels",self.channels)
        print("que saldra", self.data.shape(self.CODE)[0])
        self.titles = ['{} Channel {}'.format(self.CODE.upper(), x) for x in range(self.nrows)]
        print("self.titles",self.titles)
        self.colorbar=False
        self.width   =8
        self.height  =8
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_ele   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.08})
        self.flag    =0
        self.indicador= 0
        self.last_data_ele = None
        self.val_mean      = None

    def update(self, dataOut):

        data = {}
        meta = {}
        if hasattr(dataOut, 'dataPP_POWER'):
            factor = 1
        if hasattr(dataOut, 'nFFTPoints'):
            factor = dataOut.normFactor
        print("dataOut",dataOut.data_360.shape)
        #
        data['weather'] = 10*numpy.log10(dataOut.data_360/(factor))
        #
        #data['weather'] = 10*numpy.log10(dataOut.data_360[1]/(factor))
        data['azi']     = dataOut.data_azi
        data['ele']     = dataOut.data_ele
        data['case_flag']     = dataOut.case_flag
        #print("UPDATE")
        #print("data[weather]",data['weather'].shape)
        #print("data[azi]",data['azi'])
        return data, meta

    def get2List(self,angulos):
        list1=[]
        list2=[]
        #print(angulos)
        #exit(1)
        for i in reversed(range(len(angulos))):
            if not i==0:#el caso de i=0 evalula el primero de la lista con el ultimo y no es relevante
                diff_ = angulos[i]-angulos[i-1]
                if abs(diff_) >1.5:
                    list1.append(i-1)
                    list2.append(diff_)
        return list(reversed(list1)),list(reversed(list2))

    def fixData90(self,list_,ang_):
        if list_[0]==-1:
            vec = numpy.where(ang_<ang_[0])
            ang_[vec] = ang_[vec]+90
            return ang_
        return ang_

    def fixData90HL(self,angulos):
        vec = numpy.where(angulos>=90)
        angulos[vec]=angulos[vec]-90
        return angulos


    def search_pos(self,pos,list_):
        for i in range(len(list_)):
            if pos == list_[i]:
                return True,i
        i=None
        return False,i

    def fixDataComp(self,ang_,list1_,list2_,tipo_case):
        size  = len(ang_)
        size2 = 0
        for i in range(len(list2_)):
            size2=size2+round(abs(list2_[i]))-1
        new_size= size+size2
        ang_new = numpy.zeros(new_size)
        ang_new2 = numpy.zeros(new_size)

        tmp = 0
        c   = 0
        for i in range(len(ang_)):
            ang_new[tmp +c] = ang_[i]
            ang_new2[tmp+c] = ang_[i]
            condition , value = self.search_pos(i,list1_)
            if condition:
                pos = tmp + c + 1
                for k in range(round(abs(list2_[value]))-1):
                    if tipo_case==0 or tipo_case==3:#subida
                        ang_new[pos+k]  = ang_new[pos+k-1]+1
                        ang_new2[pos+k] = numpy.nan
                    elif tipo_case==1 or tipo_case==2:#bajada
                        ang_new[pos+k]  = ang_new[pos+k-1]-1
                        ang_new2[pos+k] = numpy.nan

                tmp = pos +k
                c   = 0
            c=c+1
        return ang_new,ang_new2

    def globalCheckPED(self,angulos,tipo_case):
        l1,l2 = self.get2List(angulos)
        print("l1",l1)
        print("l2",l2)
        if len(l1)>0:
            #angulos2 = self.fixData90(list_=l1,ang_=angulos)
            #l1,l2 = self.get2List(angulos2)
            ang1_,ang2_ = self.fixDataComp(ang_=angulos,list1_=l1,list2_=l2,tipo_case=tipo_case)
            #ang1_ = self.fixData90HL(ang1_)
            #ang2_ = self.fixData90HL(ang2_)
        else:
            ang1_= angulos
            ang2_= angulos
        return ang1_,ang2_


    def replaceNAN(self,data_weather,data_ele,val):
        data= data_ele
        data_T= data_weather
        #print(data.shape[0])
        #print(data_T.shape[0])
        #exit(1)
        if data.shape[0]> data_T.shape[0]:
            data_N = numpy.ones( [data.shape[0],data_T.shape[1]])
            c      = 0
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                    data_N[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
                else:
                    data_N[i,:]=data_T[c,:]
                    c=c+1
            return data_N
        else:
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                   data_T[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
            return data_T


    def const_ploteo(self,val_ch,data_weather,data_ele,step,res,ang_max,ang_min,case_flag):
        ang_max= ang_max
        ang_min= ang_min
        data_weather=data_weather
        val_ch=val_ch
        ##print("*********************DATA WEATHER**************************************")
        ##print(data_weather)

        '''
        print("**********************************************")
        print("**********************************************")
        print("***************ini**************")
        print("**********************************************")
        print("**********************************************")
        '''
        #print("data_ele",data_ele)
        #----------------------------------------------------------

        #exit(1)
        tipo_case = case_flag[-1]
        print("tipo_case",tipo_case)
        #--------------------- new -------------------------
        data_ele_new ,data_ele_old= self.globalCheckPED(data_ele,tipo_case)

        #-------------------------CAMBIOS RHI---------------------------------

        vec = numpy.where(data_ele<ang_max)
        data_ele = data_ele[vec]
        data_weather= data_weather[vec[0]]

        len_vec = len(vec)
        data_ele_new     = data_ele[::-1] #  reversa
        data_weather =  data_weather[::-1,:]
        new_i_ele  = int(data_ele_new[0])
        new_f_ele  = int(data_ele_new[-1])

        n1= new_i_ele- ang_min
        n2= ang_max - new_f_ele-1
        if n1>0:
            ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
            ele1_nan= numpy.ones(n1)*numpy.nan
            data_ele = numpy.hstack((ele1,data_ele_new))
            data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
        if n2>0:
            ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
            ele2_nan= numpy.ones(n2)*numpy.nan
            data_ele = numpy.hstack((data_ele,ele2))
            data_ele_old = numpy.hstack((data_ele_old,ele2_nan))


        print("ele shape",data_ele.shape)
        print(data_ele)

        #print("self.data_ele_tmp",self.data_ele_tmp)
        val_mean         = numpy.mean(data_weather[:,-1])
        self.val_mean    = val_mean
        data_weather     = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
        self.data_ele_tmp[val_ch]= data_ele_old


        print("data_weather shape",data_weather.shape)
        print(data_weather)
        #exit(1)
        return data_weather,data_ele


    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        data         = self.data[-1]
        r            = self.data.yrange
        delta_height = r[1]-r[0]
        r_mask       = numpy.where(r>=0)[0]
        ##print("delta_height",delta_height)
        #print("r_mask",r_mask,len(r_mask))
        r            = numpy.arange(len(r_mask))*delta_height
        self.y       = 2*r
        res          = 1
        ###print("data['weather'].shape[0]",data['weather'].shape[0])
        ang_max = self.ang_max
        ang_min = self.ang_min
        var_ang      =ang_max -  ang_min
        step         = (int(var_ang)/(res*data['weather'].shape[0]))
        ###print("step",step)
        #--------------------------------------------------------
        ##print('weather',data['weather'].shape)
        ##print('ele',data['ele'].shape)

        ###self.res_weather, self.res_ele = self.const_ploteo(data_weather=data['weather'][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min)
        ###self.res_azi                   = numpy.mean(data['azi'])
        ###print("self.res_ele",self.res_ele)
        plt.clf()
        subplots = [121, 122]
        if self.ini==0:
            self.data_ele_tmp = numpy.ones([self.nplots,int(var_ang)])*numpy.nan
            self.res_weather= numpy.ones([self.nplots,int(var_ang),len(r_mask)])*numpy.nan
            print("SHAPE",self.data_ele_tmp.shape)

        for i,ax in enumerate(self.axes):
            self.res_weather[i], self.res_ele = self.const_ploteo(val_ch=i, data_weather=data['weather'][i][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min,case_flag=self.data['case_flag'])
            self.res_azi                   = numpy.mean(data['azi'])

            print(self.res_ele)
            #exit(1)
            if ax.firsttime:
                #plt.clf()
                cgax, pm = wrl.vis.plot_rhi(self.res_weather[i],r=r,th=self.res_ele,ax=subplots[i], proj='cg',vmin=20, vmax=80)
                #fig=self.figures[0]
            else:

                #plt.clf()
                cgax, pm = wrl.vis.plot_rhi(self.res_weather[i],r=r,th=self.res_ele,ax=subplots[i], proj='cg',vmin=20, vmax=80)
            caax = cgax.parasites[0]
            paax = cgax.parasites[1]
            cbar = plt.gcf().colorbar(pm, pad=0.075)
            caax.set_xlabel('x_range [km]')
            caax.set_ylabel('y_range [km]')
            plt.text(1.0, 1.05, 'Elevacion '+str(thisDatetime)+"  Step   "+str(self.ini)+ " Azi: "+str(round(self.res_azi,2)), transform=caax.transAxes, va='bottom',ha='right')
        print("***************************self.ini****************************",self.ini)
        self.ini= self.ini+1

class WeatherRHI_vRF3_Plot(Plot):
    CODE = 'weather'
    plot_name = 'weather'
    plot_type = 'rhistyle'
    buffering = False
    data_ele_tmp = None

    def setup(self):
        print("********************")
        print("********************")
        print("********************")
        print("SETUP WEATHER PLOT")
        self.ncols = 1
        self.nrows = 1
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        if self.channels is not None:
            self.nplots = len(self.channels)
            self.nrows = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.nrows = self.nplots
            self.channels = list(range(self.nplots))
        print("channels",self.channels)
        print("que saldra", self.data.shape(self.CODE)[0])
        self.titles = ['{} Channel {}'.format(self.CODE.upper(), x) for x in range(self.nrows)]
        print("self.titles",self.titles)
        self.colorbar=False
        self.width   =8
        self.height  =8
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_ele   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.08})
        self.flag    =0
        self.indicador= 0
        self.last_data_ele = None
        self.val_mean      = None

    def update(self, dataOut):

        data = {}
        meta = {}
        if hasattr(dataOut, 'dataPP_POWER'):
            factor = 1
        if hasattr(dataOut, 'nFFTPoints'):
            factor = dataOut.normFactor
        print("dataOut",dataOut.data_360.shape)
        #
        data['weather'] = 10*numpy.log10(dataOut.data_360/(factor))
        #
        #data['weather'] = 10*numpy.log10(dataOut.data_360[1]/(factor))
        data['azi']     = dataOut.data_azi
        data['ele']     = dataOut.data_ele
        #data['case_flag']     = dataOut.case_flag
        #print("UPDATE")
        #print("data[weather]",data['weather'].shape)
        #print("data[azi]",data['azi'])
        return data, meta

    def get2List(self,angulos):
        list1=[]
        list2=[]
        for i in reversed(range(len(angulos))):
            if not i==0:#el caso de i=0 evalula el primero de la lista con el ultimo y no es relevante
                diff_ = angulos[i]-angulos[i-1]
                if abs(diff_) >1.5:
                    list1.append(i-1)
                    list2.append(diff_)
        return list(reversed(list1)),list(reversed(list2))

    def fixData90(self,list_,ang_):
        if list_[0]==-1:
            vec = numpy.where(ang_<ang_[0])
            ang_[vec] = ang_[vec]+90
            return ang_
        return ang_

    def fixData90HL(self,angulos):
        vec = numpy.where(angulos>=90)
        angulos[vec]=angulos[vec]-90
        return angulos


    def search_pos(self,pos,list_):
        for i in range(len(list_)):
            if pos == list_[i]:
                return True,i
        i=None
        return False,i

    def fixDataComp(self,ang_,list1_,list2_,tipo_case):
        size  = len(ang_)
        size2 = 0
        for i in range(len(list2_)):
            size2=size2+round(abs(list2_[i]))-1
        new_size= size+size2
        ang_new = numpy.zeros(new_size)
        ang_new2 = numpy.zeros(new_size)

        tmp = 0
        c   = 0
        for i in range(len(ang_)):
            ang_new[tmp +c] = ang_[i]
            ang_new2[tmp+c] = ang_[i]
            condition , value = self.search_pos(i,list1_)
            if condition:
                pos = tmp + c + 1
                for k in range(round(abs(list2_[value]))-1):
                    if tipo_case==0 or tipo_case==3:#subida
                        ang_new[pos+k]  = ang_new[pos+k-1]+1
                        ang_new2[pos+k] = numpy.nan
                    elif tipo_case==1 or tipo_case==2:#bajada
                        ang_new[pos+k]  = ang_new[pos+k-1]-1
                        ang_new2[pos+k] = numpy.nan

                tmp = pos +k
                c   = 0
            c=c+1
        return ang_new,ang_new2

    def globalCheckPED(self,angulos,tipo_case):
        l1,l2 = self.get2List(angulos)
        ##print("l1",l1)
        ##print("l2",l2)
        if len(l1)>0:
            #angulos2 = self.fixData90(list_=l1,ang_=angulos)
            #l1,l2 = self.get2List(angulos2)
            ang1_,ang2_ = self.fixDataComp(ang_=angulos,list1_=l1,list2_=l2,tipo_case=tipo_case)
            #ang1_ = self.fixData90HL(ang1_)
            #ang2_ = self.fixData90HL(ang2_)
        else:
            ang1_= angulos
            ang2_= angulos
        return ang1_,ang2_


    def replaceNAN(self,data_weather,data_ele,val):
        data= data_ele
        data_T= data_weather

        if data.shape[0]> data_T.shape[0]:
            print("IF")
            data_N = numpy.ones( [data.shape[0],data_T.shape[1]])
            c      = 0
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                    data_N[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
                else:
                    data_N[i,:]=data_T[c,:]
                    c=c+1
            return data_N
        else:
            print("else")
            for i in range(len(data)):
                if numpy.isnan(data[i]):
                   data_T[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
            return data_T

    def check_case(self,data_ele,ang_max,ang_min):
        start  = data_ele[0]
        end    = data_ele[-1]
        number = (end-start)
        len_ang=len(data_ele)
        print("start",start)
        print("end",end)
        print("number",number)

        print("len_ang",len_ang)

        #exit(1)

        if start<end and (round(abs(number)+1)>=len_ang or (numpy.argmin(data_ele)==0)):#caso subida
            return 0
        #elif start>end and (round(abs(number)+1)>=len_ang or(numpy.argmax(data_ele)==0)):#caso bajada
        #    return 1
        elif round(abs(number)+1)>=len_ang and (start>end or(numpy.argmax(data_ele)==0)):#caso bajada
            return 1
        elif round(abs(number)+1)<len_ang and data_ele[-2]>data_ele[-1]:# caso BAJADA CAMBIO ANG MAX
            return 2
        elif round(abs(number)+1)<len_ang and data_ele[-2]<data_ele[-1] :# caso SUBIDA CAMBIO ANG MIN
            return 3


    def const_ploteo(self,val_ch,data_weather,data_ele,step,res,ang_max,ang_min,case_flag):
        ang_max= ang_max
        ang_min= ang_min
        data_weather=data_weather
        val_ch=val_ch
        ##print("*********************DATA WEATHER**************************************")
        ##print(data_weather)
        if self.ini==0:

            #--------------------- new -------------------------
            data_ele_new ,data_ele_old= self.globalCheckPED(data_ele,tipo_case)

            #-------------------------CAMBIOS RHI---------------------------------
            start= ang_min
            end  = ang_max
            n= (ang_max-ang_min)/res
            #------ new
            self.start_data_ele = data_ele_new[0]
            self.end_data_ele  = data_ele_new[-1]
            if tipo_case==0  or tipo_case==3: # SUBIDA
                n1= round(self.start_data_ele)- start
                n2= end - round(self.end_data_ele)
                print(self.start_data_ele)
                print(self.end_data_ele)
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,self.start_data_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    print("ele1_nan",ele1_nan.shape)
                    print("data_ele_old",data_ele_old.shape)
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_old))
                if n2>0:
                    ele2= numpy.linspace(self.end_data_ele+1,end,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    print("ele2_nan",ele2_nan.shape)
                    print("data_ele_old",data_ele_old.shape)
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

            if tipo_case==1  or tipo_case==2: # BAJADA
                data_ele_new       = data_ele_new[::-1] #  reversa
                data_ele_old   = data_ele_old[::-1]# reversa
                data_weather   = data_weather[::-1,:]# reversa
                vec= numpy.where(data_ele_new<ang_max)
                data_ele_new = data_ele_new[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]
                vec2= numpy.where(0<data_ele_new)
                data_ele_new = data_ele_new[vec2]
                data_ele_old = data_ele_old[vec2]
                data_weather  = data_weather[vec2[0]]
                self.start_data_ele = data_ele_new[0]
                self.end_data_ele  = data_ele_new[-1]

                n1= round(self.start_data_ele)- start
                n2= end - round(self.end_data_ele)-1
                print(self.start_data_ele)
                print(self.end_data_ele)
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,self.start_data_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_old))
                if n2>0:
                    ele2= numpy.linspace(self.end_data_ele+1,end,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))
            # RADAR
            # NOTA data_ele y data_weather es la variable que retorna
            val_mean         = numpy.mean(data_weather[:,-1])
            self.val_mean    = val_mean
            data_weather     = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
            print("eleold",data_ele_old)
            print(self.data_ele_tmp[val_ch])
            print(data_ele_old.shape[0])
            print(self.data_ele_tmp[val_ch].shape[0])
            if (data_ele_old.shape[0]==91 or self.data_ele_tmp[val_ch].shape[0]==91):
                import sys
                print("EXIT",self.ini)

                sys.exit(1)
            self.data_ele_tmp[val_ch]= data_ele_old
        else:
            #print("**********************************************")
            #print("****************VARIABLE**********************")
            #-------------------------CAMBIOS RHI---------------------------------
            #---------------------------------------------------------------------
            ##print("INPUT data_ele",data_ele)
            flag=0
            start_ele = self.res_ele[0]
            #tipo_case = self.check_case(data_ele,ang_max,ang_min)
            tipo_case = case_flag[-1]
            #print("TIPO DE DATA",tipo_case)
            #-----------new------------
            data_ele ,data_ele_old = self.globalCheckPED(data_ele,tipo_case)
            data_weather           = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)

            #-------------------------------NEW RHI ITERATIVO-------------------------

            if tipo_case==0 : # SUBIDA
                vec = numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]

                vec2 = numpy.where(0<data_ele)
                data_ele= data_ele[vec2]
                data_ele_old= data_ele_old[vec2]
                ##print(data_ele_new)
                data_weather= data_weather[vec2[0]]

                new_i_ele  = int(round(data_ele[0]))
                new_f_ele  = int(round(data_ele[-1]))
                #print(new_i_ele)
                #print(new_f_ele)
                #print(data_ele,len(data_ele))
                #print(data_ele_old,len(data_ele_old))
                if new_i_ele< 2:
                    self.data_ele_tmp[val_ch] = numpy.ones(ang_max-ang_min)*numpy.nan
                    self.res_weather[val_ch]  = self.replaceNAN(data_weather=self.res_weather[val_ch],data_ele=self.data_ele_tmp[val_ch],val=self.val_mean)
                self.data_ele_tmp[val_ch][new_i_ele:new_i_ele+len(data_ele)]=data_ele_old
                self.res_ele[new_i_ele:new_i_ele+len(data_ele)]= data_ele
                self.res_weather[val_ch][new_i_ele:new_i_ele+len(data_ele),:]= data_weather
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]

            elif tipo_case==1 : #BAJADA
                data_ele       = data_ele[::-1] #  reversa
                data_ele_old   = data_ele_old[::-1]# reversa
                data_weather   = data_weather[::-1,:]# reversa
                vec= numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_ele_old = data_ele_old[vec]
                data_weather  = data_weather[vec[0]]
                vec2= numpy.where(0<data_ele)
                data_ele = data_ele[vec2]
                data_ele_old = data_ele_old[vec2]
                data_weather  = data_weather[vec2[0]]


                new_i_ele  = int(round(data_ele[0]))
                new_f_ele  = int(round(data_ele[-1]))
                #print(data_ele)
                #print(ang_max)
                #print(data_ele_old)
                if new_i_ele <= 1:
                    new_i_ele = 1
                if round(data_ele[-1])>=ang_max-1:
                    self.data_ele_tmp[val_ch] = numpy.ones(ang_max-ang_min)*numpy.nan
                    self.res_weather[val_ch]  = self.replaceNAN(data_weather=self.res_weather[val_ch],data_ele=self.data_ele_tmp[val_ch],val=self.val_mean)
                self.data_ele_tmp[val_ch][new_i_ele-1:new_i_ele+len(data_ele)-1]=data_ele_old
                self.res_ele[new_i_ele-1:new_i_ele+len(data_ele)-1]= data_ele
                self.res_weather[val_ch][new_i_ele-1:new_i_ele+len(data_ele)-1,:]= data_weather
                data_ele     = self.res_ele
                data_weather = self.res_weather[val_ch]

            elif tipo_case==2:  #bajada
                vec = numpy.where(data_ele<ang_max)
                data_ele = data_ele[vec]
                data_weather= data_weather[vec[0]]

                len_vec = len(vec)
                data_ele_new     = data_ele[::-1] #  reversa
                data_weather =  data_weather[::-1,:]
                new_i_ele  = int(data_ele_new[0])
                new_f_ele  = int(data_ele_new[-1])

                n1= new_i_ele- ang_min
                n2= ang_max - new_f_ele-1
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
                if n2>0:
                    ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

                self.data_ele_tmp[val_ch] = data_ele_old
                self.res_ele      = data_ele
                self.res_weather[val_ch]  = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]

            elif tipo_case==3:#subida
                vec = numpy.where(0<data_ele)
                data_ele= data_ele[vec]
                data_ele_new = data_ele
                data_ele_old= data_ele_old[vec]
                data_weather= data_weather[vec[0]]
                pos_ini = numpy.argmin(data_ele)
                if pos_ini>0:
                    len_vec= len(data_ele)
                    vec3  = numpy.linspace(pos_ini,len_vec-1,len_vec-pos_ini).astype(int)
                    #print(vec3)
                    data_ele= data_ele[vec3]
                    data_ele_new = data_ele
                    data_ele_old= data_ele_old[vec3]
                    data_weather= data_weather[vec3]

                new_i_ele  = int(data_ele_new[0])
                new_f_ele  = int(data_ele_new[-1])
                n1= new_i_ele- ang_min
                n2= ang_max - new_f_ele-1
                if n1>0:
                    ele1= numpy.linspace(ang_min+1,new_i_ele-1,n1)
                    ele1_nan= numpy.ones(n1)*numpy.nan
                    data_ele = numpy.hstack((ele1,data_ele_new))
                    data_ele_old = numpy.hstack((ele1_nan,data_ele_new))
                if n2>0:
                    ele2= numpy.linspace(new_f_ele+1,ang_max,n2)
                    ele2_nan= numpy.ones(n2)*numpy.nan
                    data_ele = numpy.hstack((data_ele,ele2))
                    data_ele_old = numpy.hstack((data_ele_old,ele2_nan))

                self.data_ele_tmp[val_ch] = data_ele_old
                self.res_ele      = data_ele
                self.res_weather[val_ch]  = self.replaceNAN(data_weather=data_weather,data_ele=data_ele_old,val=self.val_mean)
                data_ele                                    = self.res_ele
                data_weather                                = self.res_weather[val_ch]
        #print("self.data_ele_tmp",self.data_ele_tmp)
        return data_weather,data_ele

    def const_ploteo_vRF(self,val_ch,data_weather,data_ele,res,ang_max,ang_min):

        data_ele_new ,data_ele_old= self.globalCheckPED(data_ele,1)

        data_ele = data_ele_old.copy()

        diff_1 = ang_max - data_ele[0]
        angles_1_nan = numpy.linspace(ang_max,data_ele[0]+1,int(diff_1)-1)#*numpy.nan

        diff_2 = data_ele[-1]-ang_min
        angles_2_nan = numpy.linspace(data_ele[-1]-1,ang_min,int(diff_2)-1)#*numpy.nan

        angles_filled = numpy.concatenate((angles_1_nan,data_ele,angles_2_nan))

        print(angles_filled)

        data_1_nan = numpy.ones([angles_1_nan.shape[0],len(self.r_mask)])*numpy.nan
        data_2_nan = numpy.ones([angles_2_nan.shape[0],len(self.r_mask)])*numpy.nan

        data_filled = numpy.concatenate((data_1_nan,data_weather,data_2_nan),axis=0)
        #val_mean         = numpy.mean(data_weather[:,-1])
        #self.val_mean    = val_mean
        print(data_filled)
        data_filled     = self.replaceNAN(data_weather=data_filled,data_ele=angles_filled,val=numpy.nan)

        print(data_filled)
        print(data_filled.shape)
        print(angles_filled.shape)

        return data_filled,angles_filled

    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        data         = self.data[-1]
        r            = self.data.yrange
        delta_height = r[1]-r[0]
        r_mask       = numpy.where(r>=0)[0]
        self.r_mask =r_mask
        ##print("delta_height",delta_height)
        #print("r_mask",r_mask,len(r_mask))
        r            = numpy.arange(len(r_mask))*delta_height
        self.y       = 2*r
        res          = 1
        ###print("data['weather'].shape[0]",data['weather'].shape[0])
        ang_max = self.ang_max
        ang_min = self.ang_min
        var_ang      =ang_max -  ang_min
        step         = (int(var_ang)/(res*data['weather'].shape[0]))
        ###print("step",step)
        #--------------------------------------------------------
        ##print('weather',data['weather'].shape)
        ##print('ele',data['ele'].shape)

        ###self.res_weather, self.res_ele = self.const_ploteo(data_weather=data['weather'][:,r_mask],data_ele=data['ele'],step=step,res=res,ang_max=ang_max,ang_min=ang_min)
        ###self.res_azi                   = numpy.mean(data['azi'])
        ###print("self.res_ele",self.res_ele)

        plt.clf()
        subplots = [121, 122]
        #if self.ini==0:
            #self.res_weather= numpy.ones([self.nplots,int(var_ang),len(r_mask)])*numpy.nan
            #print("SHAPE",self.data_ele_tmp.shape)

        for i,ax in enumerate(self.axes):
            res_weather, self.res_ele = self.const_ploteo_vRF(val_ch=i, data_weather=data['weather'][i][:,r_mask],data_ele=data['ele'],res=res,ang_max=ang_max,ang_min=ang_min)
            self.res_azi                   = numpy.mean(data['azi'])

            if ax.firsttime:
                #plt.clf()
                print("Frist Plot")
                print(data['weather'][i][:,r_mask].shape)
                print(data['ele'].shape)
                cgax, pm = wrl.vis.plot_rhi(res_weather,r=r,th=self.res_ele,ax=subplots[i], proj='cg',vmin=20, vmax=80)
                #cgax, pm = wrl.vis.plot_rhi(data['weather'][i][:,r_mask],r=r,th=data['ele'],ax=subplots[i], proj='cg',vmin=20, vmax=80)
                gh = cgax.get_grid_helper()
                locs = numpy.linspace(ang_min,ang_max,var_ang+1)
                gh.grid_finder.grid_locator1 = FixedLocator(locs)
                gh.grid_finder.tick_formatter1 = DictFormatter(dict([(i, r"${0:.0f}^\circ$".format(i)) for i in locs]))


                #fig=self.figures[0]
            else:
                #plt.clf()
                print("ELSE PLOT")
                cgax, pm = wrl.vis.plot_rhi(res_weather,r=r,th=self.res_ele,ax=subplots[i], proj='cg',vmin=20, vmax=80)
                #cgax, pm = wrl.vis.plot_rhi(data['weather'][i][:,r_mask],r=r,th=data['ele'],ax=subplots[i], proj='cg',vmin=20, vmax=80)
                gh = cgax.get_grid_helper()
                locs = numpy.linspace(ang_min,ang_max,var_ang+1)
                gh.grid_finder.grid_locator1 = FixedLocator(locs)
                gh.grid_finder.tick_formatter1 = DictFormatter(dict([(i, r"${0:.0f}^\circ$".format(i)) for i in locs]))

            caax = cgax.parasites[0]
            paax = cgax.parasites[1]
            cbar = plt.gcf().colorbar(pm, pad=0.075)
            caax.set_xlabel('x_range [km]')
            caax.set_ylabel('y_range [km]')
            plt.text(1.0, 1.05, 'Elevacion '+str(thisDatetime)+"  Step   "+str(self.ini)+ " Azi: "+str(round(self.res_azi,2)), transform=caax.transAxes, va='bottom',ha='right')
        print("***************************self.ini****************************",self.ini)
        self.ini= self.ini+1

class WeatherRHI_vRF4_Plot(Plot):
    CODE = 'weather'
    plot_name = 'weather'
    #plot_type = 'rhistyle'
    buffering = False
    data_ele_tmp = None

    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        self.polar = True
        if self.channels is not None:
            self.nplots = len(self.channels)
            self.nrows = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.nrows = self.nplots
            self.channels = list(range(self.nplots))
            #print("JERE")
            #exit(1)
        #print("channels",self.channels)
        #print("que saldra", self.data.shape(self.CODE)[0])
        #self.titles = ['{} Channel {}'.format(self.CODE.upper(), x) for x in range(self.nrows)]

        #print("self.titles",self.titles)
        if self.CODE == 'Power':
            self.cb_label = r'Power (dB)'
        elif self.CODE == 'Doppler':
            self.cb_label = r'Velocity (m/s)'
        self.colorbar=True
        self.width   =8
        self.height  =8
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_ele   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.08})
        self.flag    =0
        self.indicador= 0
        self.last_data_ele = None
        self.val_mean      = None

    def update(self, dataOut):

        if self.mode == 'Power':
            self.CODE = 'Power'
        elif self.mode == 'Doppler':
            self.CODE = 'Doppler'

        data = {}
        meta = {}
        if hasattr(dataOut, 'dataPP_POWER'):
            factor = 1
        if hasattr(dataOut, 'nFFTPoints'):
            factor = dataOut.normFactor

        if self.CODE == 'Power':
            data[self.CODE] = 10*numpy.log10(dataOut.data_360_Power/(factor))
        elif self.CODE == 'Doppler':
            data[self.CODE] = dataOut.data_360_Velocity/(factor)

        data['azi']     = dataOut.data_azi
        data['ele']     = dataOut.data_ele

        return data, meta

    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        data         = self.data[-1]
        r            = self.data.yrange
        delta_height = r[1]-r[0]
        r_mask       = numpy.where(r>=0)[0]
        self.r_mask =r_mask
        r            = numpy.arange(len(r_mask))*delta_height
        self.y       = 2*r
        res          = 1
        ang_max = self.ang_max
        ang_min = self.ang_min
        var_ang      =ang_max -  ang_min
        step         = (int(var_ang)/(res*data[self.CODE].shape[0]))

        z = data[self.CODE][self.channels[0]][:,r_mask]

        #print(z[2,:])
        self.titles = []

        #exit(1)

        if self.CODE == 'Power':
            cmap = 'jet'
        elif self.CODE == 'Doppler':
            cmap = 'RdBu'

        self.ymax = self.ymax if self.ymax else numpy.nanmax(r)
        self.ymin = self.ymin if self.ymin else numpy.nanmin(r)
        self.zmax = self.zmax if self.zmax else numpy.nanmax(z)
        self.zmin = self.zmin if self.zmin else numpy.nanmin(z)

        #plt.clf()
        subplots = [121, 122]

        r, theta = numpy.meshgrid(r, numpy.radians(data['ele']) )

        points_cb = 200
        mylevs_cbar = list(numpy.linspace(self.zmin,self.zmax,points_cb)) #niveles de la barra de colores

        for i,ax in enumerate(self.axes):

            if ax.firsttime:
                ax.set_xlim(numpy.radians(self.ang_min),numpy.radians(self.ang_max))
                ax.plt = ax.contourf(theta, r, z, points_cb, cmap=cmap, vmin=self.zmin, vmax=self.zmax, levels=mylevs_cbar)
                #print(ax.plt)
                #exit(1)
                '''
                self.figures[-1].colorbar(plt, orientation="vertical", fraction=0.025, pad=0.07)
                print(self.figures[0])
                print(self.figures)
                print(plt)
                print(ax)
                exit(1)
                '''

            else:
                ax.set_xlim(numpy.radians(self.ang_min),numpy.radians(self.ang_max))
                ax.plt = ax.contourf(theta, r, z, points_cb, cmap=cmap, vmin=self.zmin, vmax=self.zmax, levels=mylevs_cbar)
                #self.figures[0].colorbar(plt, orientation="vertical", fraction=0.025, pad=0.07)

            #print(self.titles)
            if len(self.channels) !=1:
                self.titles = ['{} Azi: {} Channel {}'.format(self.CODE.upper(), str(round(numpy.mean(data['azi']),2)), x) for x in range(self.nrows)]
            else:
                self.titles = ['{} Azi: {} Channel {}'.format(self.CODE.upper(), str(round(numpy.mean(data['azi']),2)), self.channels[0])]
            #self.titles.append('Azi: {}'.format(str(round(numpy.mean(data['azi']),2))))
            #self.titles.append(str(round(numpy.mean(data['azi']),2)))
            #print(self.titles)
            #plt.text(1.0, 1.05, str(thisDatetime)+ " Azi: "+str(round(numpy.mean(data['azi']),2)), transform=caax.transAxes, va='bottom',ha='right')
        #print("***************************self.ini****************************",self.ini)
        #self.figures[-1].colorbar(plt, orientation="vertical", fraction=0.025, pad=0.07)
        #self.ini= self.ini+1
