import os
import datetime
import numpy

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
        self.nplots= 1
        self.ylabel= 'Range [Km]'
        self.titles= ['Weather']
        self.colorbar=False
        self.width   =8
        self.height  =8
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

        ####print("factor",factor)
        data['weather'] = 10*numpy.log10(dataOut.data_360[1]/(factor))
        ####print("weather",data['weather'])
        data['azi']     = dataOut.data_azi
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
            size2=size2+list2_[i]-1
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
                for k in range(list2_[value]-1):
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
        ####print("----------------activeNEWFUNCTION")
        data= data_azi
        data_T= data_weather
        ####print("data_azi",data_azi)
        ####print("VAL:",val)
        ####print("SHAPE",data_T.shape)
        for i in range(len(data)):
            if numpy.isnan(data[i]):
               ####print("NAN")
               #data_T[i,:]=numpy.ones(data_T.shape[1])*val
               data_T[i,:]=numpy.ones(data_T.shape[1])*numpy.nan
        return data_T

    def const_ploteo(self,data_weather,data_azi,step,res):
        if self.ini==0:
            #------- AZIMUTH
            n     = (360/res)-len(data_azi)
            #--------------------- new -------------------------
            ####data_azi_old  = data_azi
            data_azi_new ,data_azi_old= self.globalCheckPED(data_azi)
            #------------------------
            ####data_azi_new  = self.fixDATA(data_azi)
            #ata_azi_new   = self.fixDATANEW(data_azi)

            start = data_azi_new[-1] + res
            end   = data_azi_new[0]  - res
            ##### new
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
            ####data_azi_old = data_azi
            ### weather ###
            ####data_weather = self.replaceNAN(data_weather=data_weather,data_azi=data_azi_old,val=self.val_mean)

            ####if numpy.isnan(data_azi[0]):
            ####    data_azi[0]=self.last_data_azi+1
            ####data_azi = self.fixDATA(data_azi)
            start = data_azi[0]
            end   = data_azi[-1]
            self.last_data_azi= end
            ####print("start",start)
            ####print("end",end)
            if start< start_azi:
                start = start +360
            if end <start_azi:
                end  = end +360
            ####print("start",start)
            ####print("end",end)
            #### AQUI SERA LA MAGIA
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
            ####print(pos_ini)
            ####print(len_azi)
            ####print("shape",self.res_azi.shape)
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
        #print("--------------------------------------",self.ini,"-----------------------------------")
        #numpy.set_printoptions(suppress=True)
        ####print("times: ",self.data.times)
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1]).strftime('%Y-%m-%d %H:%M:%S')
        #print("times: ",thisDatetime)
        data         = self.data[-1]
        ####ALTURA altura_tmp_h
        ###print("Y RANGES",self.data.yrange,len(self.data.yrange))
        ###altura_h     = (data['weather'].shape[1])/10.0
        ###stoprange = float(altura_h*0.3)#stoprange = float(33*1.5) por ahora 400
        ###rangestep = float(0.03)
        ###r      = numpy.arange(0, stoprange, rangestep)
        ###print("r",r,len(r))
        #-----------------------------update----------------------
        r=  self.data.yrange
        delta_height = r[1]-r[0]
        #print("1",r)
        r_mask= numpy.where(r>=0)[0]
        r = numpy.arange(len(r_mask))*delta_height
        #print("2",r)
        self.y = 2*r
        ######self.y = self.data.yrange
        # RADAR
        #data_weather = data['weather']
        # PEDESTAL
        #data_azi  = data['azi']
        res     = 1
        # STEP
        step    = (360/(res*data['weather'].shape[0]))
        #print("shape wr_data", wr_data.shape)
        #print("shape wr_azi",wr_azi.shape)
        #print("step",step)
        ####print("Time---->",self.data.times[-1],thisDatetime)
        #print("alturas", len(self.y))numpy.where(r>=0)
        self.res_weather, self.res_azi = self.const_ploteo(data_weather=data['weather'][:,r_mask],data_azi=data['azi'],step=step,res=res)
        #numpy.set_printoptions(suppress=True)
        #print("resultado",self.res_azi)
        ###########################/DATA_RM/10_tmp/ch0###############################
        #################    PLOTEO           ###################
        ##########################################################

        for i,ax in enumerate(self.axes):
            if ax.firsttime:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.res_weather,r=r,az=self.res_azi,fig=self.figures[0], proj='cg', vmin=8, vmax=35)
            else:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.res_weather,r=r,az=self.res_azi,fig=self.figures[0], proj='cg', vmin=8, vmax=35)
        caax = cgax.parasites[0]
        paax = cgax.parasites[1]
        cbar = plt.gcf().colorbar(pm, pad=0.075)
        caax.set_xlabel('x_range [km]')
        caax.set_ylabel('y_range [km]')
        plt.text(1.0, 1.05, 'azimuth '+str(thisDatetime)+"  step   "+str(self.ini), transform=caax.transAxes, va='bottom',ha='right')

        self.ini= self.ini+1
