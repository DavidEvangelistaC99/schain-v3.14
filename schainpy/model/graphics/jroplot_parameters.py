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

    def update(self, dataOut):

        data = {}
        meta = {}
        print("aprox",dataOut.data_360[0])
        data['weather'] = 10*numpy.log10(dataOut.data_360[0]/(250.0))
        #print(data['weather'])
        data['azi']     = dataOut.data_azi
        print("UPDATE",data['azi'])
        return data, meta

    def const_ploteo(self,data_weather,data_azi,step,res):
        #print("data_weather",data_weather)
        print("data_azi",data_azi)
        print("step",step)
        if self.ini==0:
            #------- AZIMUTH
            n     = (360/res)-len(data_azi)
            start = data_azi[-1] + res
            end   = data_azi[0]  - res
            if start>end:
                end        = end + 360
            azi_vacia = numpy.linspace(start,end,int(n))
            azi_vacia = numpy.where(azi_vacia>360,azi_vacia-360,azi_vacia)
            data_azi  = numpy.hstack((data_azi,azi_vacia))
            # RADAR
            val_mean         = numpy.mean(data_weather[:,0])
            data_weather_cmp = numpy.ones([(360-data_weather.shape[0]),data_weather.shape[1]])*val_mean
            data_weather     = numpy.vstack((data_weather,data_weather_cmp))
        else:
            # azimuth
            flag=0
            start_azi = self.res_azi[0]
            start = data_azi[0]
            end   = data_azi[-1]
            print("start",start)
            print("end",end)
            if start< start_azi:
                start = start +360
            if end <start_azi:
                end  = end +360

            print("start",start)
            print("end",end)
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

            print(pos_ini)
            print(len_azi)
            print("shape",self.res_azi.shape)
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
        print("--------------------------------------",self.ini,"-----------------------------------")
        #numpy.set_printoptions(suppress=True)
        #print(self.data.times)
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1])
        data         = self.data[-1]
        # ALTURA altura_tmp_h
        altura_h     = (data['weather'].shape[1])/10.0
        stoprange = float(altura_h*1.5)#stoprange = float(33*1.5) por ahora 400
        rangestep = float(0.15)
        r      = numpy.arange(0, stoprange, rangestep)
        self.y = 2*r
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
        print("Time---->",self.data.times[-1],thisDatetime)
        #print("alturas", len(self.y))
        self.res_weather, self.res_azi = self.const_ploteo(data_weather=data['weather'],data_azi=data['azi'],step=step,res=res)
        #numpy.set_printoptions(suppress=True)
        #print("resultado",self.res_azi)
        ##########################################################
        #################    PLOTEO           ###################
        ##########################################################

        for i,ax in enumerate(self.axes):
            if ax.firsttime:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.res_weather,r=r,az=self.res_azi,fig=self.figures[0], proj='cg', vmin=1, vmax=60)
            else:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.res_weather,r=r,az=self.res_azi,fig=self.figures[0], proj='cg', vmin=0, vmax=60)
        caax = cgax.parasites[0]
        paax = cgax.parasites[1]
        cbar = plt.gcf().colorbar(pm, pad=0.075)
        caax.set_xlabel('x_range [km]')
        caax.set_ylabel('y_range [km]')
        plt.text(1.0, 1.05, 'azimuth '+str(thisDatetime)+"step"+str(self.ini), transform=caax.transAxes, va='bottom',ha='right')

        self.ini= self.ini+1
