import os
import datetime
import warnings
import numpy
from mpl_toolkits.axisartist.grid_finder import FixedLocator, DictFormatter
from matplotlib.patches import Circle
from cartopy.feature import ShapelyFeature
import cartopy.io.shapereader as shpreader

from schainpy.model.graphics.jroplot_base import Plot, plt, ccrs
from schainpy.model.graphics.jroplot_spectra import SpectraPlot, RTIPlot, CoherencePlot, SpectraCutPlot
from schainpy.utils import log
from schainpy.model.graphics.plotting_codes import cb_tables


EARTH_RADIUS = 6.3710e3


def antenna_to_cartesian(ranges, azimuths, elevations):
    """
    Return Cartesian coordinates from antenna coordinates.

    Parameters
    ----------
    ranges : array
        Distances to the center of the radar gates (bins) in kilometers.
    azimuths : array
        Azimuth angle of the radar in degrees.
    elevations : array
        Elevation angle of the radar in degrees.

    Returns
    -------
    x, y, z : array
        Cartesian coordinates in meters from the radar.

    Notes
    -----
    The calculation for Cartesian coordinate is adapted from equations
    2.28(b) and 2.28(c) of Doviak and Zrnic [1]_ assuming a
    standard atmosphere (4/3 Earth's radius model).

    .. math::

        z = \\sqrt{r^2+R^2+2*r*R*sin(\\theta_e)} - R

        s = R * arcsin(\\frac{r*cos(\\theta_e)}{R+z})

        x = s * sin(\\theta_a)

        y = s * cos(\\theta_a)

    Where r is the distance from the radar to the center of the gate,
    :math:`\\theta_a` is the azimuth angle, :math:`\\theta_e` is the
    elevation angle, s is the arc length, and R is the effective radius
    of the earth, taken to be 4/3 the mean radius of earth (6371 km).

    References
    ----------
    .. [1] Doviak and Zrnic, Doppler Radar and Weather Observations, Second
        Edition, 1993, p. 21.

    """
    theta_e = numpy.deg2rad(elevations) # elevation angle in radians.
    theta_a = numpy.deg2rad(azimuths) # azimuth angle in radians.
    R = 6371.0 * 1000.0 * 4.0 / 3.0     # effective radius of earth in meters.
    r = ranges * 1000.0                 # distances to gates in meters.

    z = (r ** 2 + R ** 2 + 2.0 * r * R * numpy.sin(theta_e)) ** 0.5 - R
    s = R * numpy.arcsin(r * numpy.cos(theta_e) / (R + z))  # arc length in m.
    x = s * numpy.sin(theta_a)
    y = s * numpy.cos(theta_a)
    return x, y, z

def cartesian_to_geographic_aeqd(x, y, lon_0, lat_0, R=EARTH_RADIUS):
    """
    Azimuthal equidistant Cartesian to geographic coordinate transform.

    Transform a set of Cartesian/Cartographic coordinates (x, y) to
    geographic coordinate system (lat, lon) using a azimuthal equidistant
    map projection [1]_.

    .. math::

        lat = \\arcsin(\\cos(c) * \\sin(lat_0) +
                       (y * \\sin(c) * \\cos(lat_0) / \\rho))

        lon = lon_0 + \\arctan2(
            x * \\sin(c),
            \\rho * \\cos(lat_0) * \\cos(c) - y * \\sin(lat_0) * \\sin(c))

        \\rho = \\sqrt(x^2 + y^2)

        c = \\rho / R

    Where x, y are the Cartesian position from the center of projection;
    lat, lon the corresponding latitude and longitude; lat_0, lon_0 are the
    latitude and longitude of the center of the projection; R is the radius of
    the earth (defaults to ~6371 km). lon is adjusted to be between -180 and
    180.

    Parameters
    ----------
    x, y : array-like
        Cartesian coordinates in the same units as R, typically meters.
    lon_0, lat_0 : float
        Longitude and latitude, in degrees, of the center of the projection.
    R : float, optional
        Earth radius in the same units as x and y. The default value is in
        units of meters.

    Returns
    -------
    lon, lat : array
        Longitude and latitude of Cartesian coordinates in degrees.

    References
    ----------
    .. [1] Snyder, J. P. Map Projections--A Working Manual. U. S. Geological
        Survey Professional Paper 1395, 1987, pp. 191-202.

    """
    x = numpy.atleast_1d(numpy.asarray(x))
    y = numpy.atleast_1d(numpy.asarray(y))

    lat_0_rad = numpy.deg2rad(lat_0)
    lon_0_rad = numpy.deg2rad(lon_0)

    rho = numpy.sqrt(x*x + y*y)
    c = rho / R

    with warnings.catch_warnings():
        # division by zero may occur here but is properly addressed below so
        # the warnings can be ignored
        warnings.simplefilter("ignore", RuntimeWarning)
        lat_rad = numpy.arcsin(numpy.cos(c) * numpy.sin(lat_0_rad) +
                            y * numpy.sin(c) * numpy.cos(lat_0_rad) / rho)
    lat_deg = numpy.rad2deg(lat_rad)
    # fix cases where the distance from the center of the projection is zero
    lat_deg[rho == 0] = lat_0

    x1 = x * numpy.sin(c)
    x2 = rho*numpy.cos(lat_0_rad)*numpy.cos(c) - y*numpy.sin(lat_0_rad)*numpy.sin(c)
    lon_rad = lon_0_rad + numpy.arctan2(x1, x2)
    lon_deg = numpy.rad2deg(lon_rad)
    # Longitudes should be from -180 to 180 degrees
    lon_deg[lon_deg > 180] -= 360.
    lon_deg[lon_deg < -180] += 360.

    return lon_deg, lat_deg

def antenna_to_geographic(ranges, azimuths, elevations, site):

    x, y, z = antenna_to_cartesian(numpy.array(ranges), numpy.array(azimuths), numpy.array(elevations))
    lon, lat = cartesian_to_geographic_aeqd(x, y, site[0], site[1], R=6370997.)

    return lon, lat

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



class WeatherParamsPlot(Plot):

    plot_type = 'scattermap'
    buffering = False

    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots= 1

        if self.channels is not None:
            self.nplots = len(self.channels)
            self.ncols = len(self.channels)
        else:
            self.nplots = self.data.shape(self.CODE)[0]
            self.ncols = self.nplots
            self.channels = list(range(self.nplots))

        self.colorbar=True
        if len(self.channels)>1:
            self.width = 12
        else:
            self.width   =8
        self.height  =7
        self.ini     =0
        self.len_azi =0
        self.buffer_ini  = None
        self.buffer_ele   = None
        self.plots_adjust.update({'wspace': 0.4, 'hspace':0.4, 'left': 0.1, 'right': 0.9, 'bottom': 0.1})
        self.flag    =0
        self.indicador= 0
        self.last_data_ele = None
        self.val_mean      = None

    def update(self, dataOut):

        vars = {
            'S' : 0,
            'V' : 1,
            'W' : 2,
            'SNR' : 3,
            'Z' : 4,
            'D' : 5,
            'P' : 6,
            'R' : 7,
        }

        data = {}
        meta = {}

        ##if hasattr(dataOut, 'nFFTPoints'):
        ##    factor = dataOut.normFactor*10.0 # CONSIDERACION ENTRE PULSE PAIR Y FFT
        ##else:
        ##    factor = 1

        if hasattr(dataOut, 'dparam'):
            tmp = getattr(dataOut, 'data_param')
        else:
            #print("-------------------self.attr_data[0]",self.attr_data[0])
            if 'S' in self.attr_data[0]:
                if self.attr_data[0]=='S':
                    tmp = 10*numpy.log10(10.0*getattr(dataOut, 'data_param')[:,0,:]) ## /(factor))   ya no considerar factor se aplica factor jroproc_parametrs
                if self.attr_data[0]=='SNR':
                    tmp = 10*numpy.log10(getattr(dataOut, 'data_param')[:,3,:])
            else:
                tmp = getattr(dataOut, 'data_param')[:,vars[self.attr_data[0]],:]

        if self.mask:
            #---------nuevo procesamiento mask----------------#
            """
            self.mask1 = 0.1   # Umbral para alturas < index
            self.mask =  0.3   # Umbral para alturas >= index
            # Crear máscaras por rangos de altura
            print("SHAPE: ",dataOut.data_param.shape)
            mask1 = (dataOut.data_param[:,3,:] < self.mask1) & (numpy.arange(dataOut.data_param.shape[3])[None, None, :] <  self.index)
            mask  = (dataOut.data_param[:,3,:] < self.mask)  & (numpy.arange(dataOut.data_param.shape[3])[None, None, :] >= self.index)
            # Aplicar filtros
            tmp[mask1] = numpy.nan
            tmp[mask]  = numpy.nan
            mask       = numpy.nansum((tmp, numpy.roll(tmp, 1),numpy.roll(tmp, -1)), axis=0) == tmp
            tmp[mask]  = numpy.nan
            """
            #-----------------------original---------------------#
            mask = dataOut.data_param[:,3,:] < self.mask
            tmp[mask] = numpy.nan
            mask = numpy.nansum((tmp, numpy.roll(tmp, 1),numpy.roll(tmp, -1)), axis=0) == tmp
            tmp[mask] = numpy.nan

            #------------------------------------------------------#
        r = dataOut.heightList
        delta_height = r[1]-r[0]
        valid = numpy.where(r>=0)[0]
        data['r'] = numpy.arange(len(valid))*delta_height

        data['data'] = [0, 0]

        try:
            data['data'][0] = tmp[0][:,valid]
            data['data'][1] = tmp[1][:,valid]
        except:
            data['data'][0] = tmp[0][:,valid]
            data['data'][1] = tmp[0][:,valid]

        if dataOut.mode_op == 'PPI':
            self.CODE = 'PPI'
            self.title = self.CODE
        elif dataOut.mode_op == 'RHI':
            self.CODE = 'RHI'
            self.title = self.CODE

        data['azi'] = dataOut.data_azi
        data['ele'] = dataOut.data_ele

        if isinstance(dataOut.mode_op, bytes):
            try:
                dataOut.mode_op = dataOut.mode_op.decode()
            except:
                dataOut.mode_op = str(dataOut.mode_op, 'utf-8')
        data['mode_op'] = dataOut.mode_op
        self.mode = dataOut.mode_op

        return data, meta

    def plot(self):
        data = self.data[-1]
        z = data['data']
        r = data['r']
        self.titles = []

        self.zmax = self.zmax if self.zmax else numpy.nanmax(z)
        self.zmin = self.zmin if self.zmin is not None else numpy.nanmin(z)

        if isinstance(data['mode_op'], bytes):
            data['mode_op'] = data['mode_op'].decode()

        if data['mode_op'] == 'RHI':
            r, theta = numpy.meshgrid(r, numpy.radians(data['ele']))
            len_aux = int(data['azi'].shape[0]/4)
            mean = numpy.mean(data['azi'][len_aux:-len_aux])
            x, y = r*numpy.cos(theta), r*numpy.sin(theta)
            if self.yrange:
                self.ylabel= 'Height [km]'
                self.xlabel= 'Distance from radar [km]'
                self.ymax = self.yrange
                self.ymin = 0
                self.xmax = self.xrange if self.xrange else numpy.nanmax(r)
                self.xmin = 0 #-self.xrange if self.xrange else -numpy.nanmax(r)  # HARDCODE
                self.setrhilimits = False
            else:
                self.ymin = 0
                self.ymax = numpy.nanmax(r)
                self.xmin = -numpy.nanmax(r)
                self.xmax = numpy.nanmax(r)

        elif data['mode_op'] == 'PPI':
            r, theta = numpy.meshgrid(r, -numpy.radians(data['azi'])+numpy.pi/2)
            len_aux = int(data['ele'].shape[0]/4)
            mean = numpy.mean(data['ele'][len_aux:-len_aux])
            x, y = r*numpy.cos(theta)*numpy.cos(numpy.radians(mean)), r*numpy.sin(
                    theta)*numpy.cos(numpy.radians(mean))
            x = km2deg(x) + self.longitude
            y = km2deg(y) + self.latitude
            if self.xrange:
                self.ylabel= 'Latitude'
                self.xlabel= 'Longitude'

                self.xmin = km2deg(-self.xrange) + self.longitude
                self.xmax = km2deg(self.xrange) + self.longitude

                self.ymin = km2deg(-self.xrange) + self.latitude
                self.ymax = km2deg(self.xrange) + self.latitude
            else:
                self.xmin = km2deg(-numpy.nanmax(r)) + self.longitude
                self.xmax = km2deg(numpy.nanmax(r)) + self.longitude

                self.ymin = km2deg(-numpy.nanmax(r)) + self.latitude
                self.ymax = km2deg(numpy.nanmax(r)) + self.latitude

        self.clear_figures()

        if data['mode_op'] == 'PPI':
            axes = self.axes['PPI']
        else:
            axes = self.axes['RHI']

        if self.colormap in cb_tables:
            norm = cb_tables[self.colormap]['norm']
        else:
            norm = None

        for i, ax in enumerate(axes):

            if norm is None:
                ax.plt = ax.pcolormesh(x, y, z[i], cmap=self.colormap, vmin=self.zmin, vmax=self.zmax)
            else:
                ax.plt = ax.pcolormesh(x, y, z[i], cmap=self.colormap, norm=norm)

            if data['mode_op'] == 'RHI':
                len_aux = int(data['azi'].shape[0]/4)
                mean = numpy.mean(data['azi'][len_aux:-len_aux])
                if len(self.channels) !=1:
                    self.titles = ['RHI {} at AZ: {} CH {}'.format(self.labels[x], str(round(mean,1)), x) for x in self.channels]
                else:
                    self.titles = ['RHI {} at AZ: {} CH {}'.format(self.labels[0], str(round(mean,1)), self.channels[0])]
            elif data['mode_op'] == 'PPI':
                len_aux = int(data['ele'].shape[0]/4)
                mean = numpy.mean(data['ele'][len_aux:-len_aux])
                if len(self.channels) !=1:
                    self.titles = ['PPI {} at EL: {} CH {}'.format(self.labels[x], str(round(mean,1)), x) for x in self.channels]
                else:
                    self.titles = ['PPI {} at EL: {} CH {}'.format(self.labels[0], str(round(mean,1)), self.channels[0])]
            self.mode_value = round(mean,1)

            if data['mode_op'] == 'PPI':
                if self.map:
                    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                    linewidth=1, color='gray', alpha=0.5, linestyle='--')
                    gl.xlabel_style = {'size': 8}
                    gl.ylabel_style = {'size': 8}
                    gl.xlabels_top = False
                    gl.ylabels_right = False
                    shape_d = os.path.join(self.shapes,'Distritos/PER_adm3.shp')
                    shape_p = os.path.join(self.shapes,'PER_ADM2/PER_ADM2.shp')
                    capitales = os.path.join(self.shapes,'CAPITALES/cap_distrito.shp')
                    vias = os.path.join(self.shapes,'Carreteras/VIAS_NACIONAL_250000.shp')
                    reader_d = shpreader.BasicReader(shape_d, encoding='latin1')
                    reader_p = shpreader.BasicReader(shape_p, encoding='latin1')
                    reader_c = shpreader.BasicReader(capitales, encoding='latin1')
                    reader_v = shpreader.BasicReader(vias, encoding='latin1')
                    caps = [x for x in reader_c.records() if x.attributes['DEPARTA']=='JUNIN' and x.attributes['CATEGORIA']=='CIUDAD']
                    districts = [x for x in reader_d.records() if x.attributes['NAME_1']=='Piura']
                    provs = [x for x in reader_p.records()]
                    vias = [x for x in reader_v.records()]

                    # Display limits and streets
                    shape_feature = ShapelyFeature([x.geometry for x in districts], ccrs.PlateCarree(), facecolor="none", edgecolor='grey', lw=0.5)
                    ax.add_feature(shape_feature)
                    shape_feature = ShapelyFeature([x.geometry for x in provs], ccrs.PlateCarree(), facecolor="none", edgecolor='white', lw=1)
                    ax.add_feature(shape_feature)
                    shape_feature = ShapelyFeature([x.geometry for x in vias], ccrs.PlateCarree(), facecolor="none", edgecolor='yellow', lw=1)
                    ax.add_feature(shape_feature)

                    for cap in caps:
                        if cap.attributes['NOMBRE'] in ('CONCEPCIÓN', 'HUANCAYO', 'JAUJA', 'LA OROYA', 'CHUPACA'):
                            ax.text(cap.attributes['X'], cap.attributes['Y'], cap.attributes['NOMBRE'], size=7, color='white', weight='bold')
                        elif cap.attributes['NOMBRE'] in ('NEGRITOS', 'SAN LUCAS', 'QUERECOTILLO', 'TAMBO GRANDE', 'CHULUCANAS', 'CATACAOS', 'LA UNION'):
                            ax.text(cap.attributes['X'], cap.attributes['Y'], cap.attributes['NOMBRE'].title(), size=6, color='white')
                    ax.plot(-75.3199751, -12.041787, '*', color='orange')
                else:
                    ax.grid(color='grey', alpha=0.5, linestyle='--', linewidth=1)

                if self.xrange<=10:
                    ranges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                elif self.xrange<=30:
                    ranges = [5, 10, 15, 20, 25, 30, 35]
                elif self.xrange<=60:
                    ranges = [10, 20, 30, 40, 50, 60]
                elif self.xrange<=100:
                    ranges = [15, 30, 45, 60, 75, 90]

                for R in ranges:
                    if R <= self.xrange:
                        circle = Circle((self.longitude, self.latitude), km2deg(R), facecolor='none',
                            edgecolor='skyblue', linewidth=1, alpha=0.5)
                        ax.add_patch(circle)
                        ax.text(km2deg(R)*numpy.cos(numpy.radians(45))+self.longitude,
                            km2deg(R)*numpy.sin(numpy.radians(45))+self.latitude,
                            '{}km'.format(R), color='skyblue', size=7)
            elif data['mode_op'] == 'RHI':
                ax.grid(color='grey', alpha=0.5, linestyle='--', linewidth=1)

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
        data['weather'] = 10*numpy.log10(dataOut.data_360[0]/(250**2))
        data['azi']     = dataOut.data_azi

        return data, meta

    def plot(self):
        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1])
        print("--------------------------------------",self.ini,"-----------------------------------")
        print("time",self.data.times[-1])
        data   = self.data[-1]
        #print("debug_0", data)
        tmp_h     = (data['weather'].shape[1])/10.0
        #print("debug_1",tmp_h)
        stoprange = float(tmp_h*1.5)#stoprange = float(33*1.5) por ahora 400
        rangestep = float(0.15)
        r      = numpy.arange(0, stoprange, rangestep)
        self.y = 2*r
        print("---------------")
        tmp_v  = data['weather']
        #print("tmp_v",tmp_v.shape)
        tmp_z  = data['azi']
        print("tmp_z-------------->",tmp_z)
        ##if self.ini==0:
        ##    tmp_z= [0,1,2,3,4,5,6,7,8,9]

        #print("tmp_z",tmp_z.shape)
        res             = 1
        step   = (360/(res*tmp_v.shape[0]))
        #print("step",step)
        mode   = 1
        if mode==0:
            #print("self.ini",self.ini)
            val             = numpy.mean(tmp_v[:,0])
            self.len_azi    = len(tmp_z)
            ones            = numpy.ones([(360-tmp_v.shape[0]),tmp_v.shape[1]])*val
            self.buffer_ini = numpy.vstack((tmp_v,ones))

            n      = ((360/res)-len(tmp_z))
            start  = tmp_z[-1]+res
            end    = tmp_z[0]-res
            if start>end:
                end = end+360
            azi_zeros           = numpy.linspace(start,end,int(n))
            azi_zeros           = numpy.where(azi_zeros>360,azi_zeros-360,azi_zeros)
            self.buffer_ini_azi = numpy.hstack((tmp_z,azi_zeros))
            self.ini            = self.ini+1

        if mode==1:
            #print("################")
            #print("################")
            #print("mode",self.ini)
            #print("self.ini",self.ini)
            if self.ini==0:
                res             = 1
                step            = (360/(res*tmp_v.shape[0]))
                val             = numpy.mean(tmp_v[:,0])
                self.len_azi    = len(tmp_z)
                self.buf_tmp    = tmp_v
                ones            = numpy.ones([(360-tmp_v.shape[0]),tmp_v.shape[1]])*val
                self.buffer_ini = numpy.vstack((tmp_v,ones))

                n      = ((360/res)-len(tmp_z))
                start  = tmp_z[-1]+res
                end    = tmp_z[0]-res
                if start>end:
                    end =end+360
                azi_zeros           = numpy.linspace(start,end,int(n))
                azi_zeros           = numpy.where(azi_zeros>360,azi_zeros-360,azi_zeros)
                self.buf_azi        = tmp_z
                self.buffer_ini_azi = numpy.hstack((tmp_z,azi_zeros))
                self.ini            = self.ini+1
            elif 0<self.ini<step:
                '''
                if self.ini>31:
                    start= tmp_z[0]
                    end  =tmp_z[-1]
                    print("start","end",start,end)
                if self.ini==32:
                    tmp_v=tmp_v+20
                if self.ini==33:
                    tmp_v=tmp_v+10
                if self.ini==34:
                    tmp_v=tmp_v+20
                if self.ini==35:
                    tmp_v=tmp_v+20
                '''
                self.buf_tmp= numpy.vstack((self.buf_tmp,tmp_v))
                print("ERROR_INMINENTE",self.buf_tmp.shape)
                if self.buf_tmp.shape[0]==360:
                    print("entre aqui en 360 grados")
                    self.buffer_ini=self.buf_tmp
                else:
                    # nuevo#########
                    self.buffer_ini[0:self.buf_tmp.shape[0],:]=self.buf_tmp
                    ################
                    #val=30.0
                    #ones            = numpy.ones([(360-self.buf_tmp.shape[0]),self.buf_tmp.shape[1]])*val
                    #self.buffer_ini = numpy.vstack((self.buf_tmp,ones))

                self.buf_azi    = numpy.hstack((self.buf_azi,tmp_z))
                n      = ((360/res)-len(self.buf_azi))
                print("n----->",n)
                if n==0:
                    self.buffer_ini_azi = self.buf_azi
                else:
                    start  = self.buf_azi[-1]+res
                    end    = self.buf_azi[0]-res
                    print("start",start)
                    print("end",end)
                    if start>end:
                        end =end+360
                    azi_zeros           = numpy.linspace(start,end,int(n))
                    azi_zeros           = numpy.where(azi_zeros>360,azi_zeros-360,azi_zeros)
                    print("self.buf_azi",self.buf_azi[0])
                    print("tmp_Z 0 ",tmp_z[0])
                    print("tmp_Z -1",tmp_z[-1])
                    if tmp_z[0]<self.buf_azi[0] <tmp_z[-1]:
                        print("activando indicador")
                        self.indicador=1
                    if self.indicador==1:
                        azi_zeros           = numpy.ones(360-len(self.buf_azi))*(tmp_z[-1]+res)
                        ###start  = tmp_z[-1]+res
                        ###end    = tmp_z[0]-res
                        ###if start>end:
                        ###    end =end+360
                        ###azi_zeros           = numpy.linspace(start,end,int(n))
                        ###azi_zeros           = numpy.where(azi_zeros>360,azi_zeros-360,azi_zeros)
                        #print("azi_zeros",azi_zeros)

                        ######self.buffer_ini_azi = numpy.hstack((self.buf_azi,azi_zeros))
                        #self.buffer_ini[0:tmv.shape[0],:]=tmp_v
                        ##self.indicador=0

                    #    self.indicador = True
                    #if self.indicador==True:
                    #    azi_zeros           = numpy.ones(360-len(self.buf_azi))*(tmp_z[-1]+res)

                    #self.buf_azi        = tmp_z
                    self.buffer_ini_azi = numpy.hstack((self.buf_azi,azi_zeros))

                if self.ini==step-1:
                    start= tmp_z[0]
                    end  = tmp_z[-1]
                    #print("start","end",start,end)
                    ###print(self.buffer_ini_azi[:80])
                self.ini            = self.ini+1

            else:
                step   = (360/(res*tmp_v.shape[0]))
                # aqui estaba realizando el debug de simulacion
                # tmp_v=tmp_v +5 en cada step sumaba 5
                # y el mismo valor despues de la primera vuelta
                #tmp_v=tmp_v+5+(self.ini-step)*1### aqui yo habia sumado 5 por las puras

                start= tmp_z[0]
                end  = tmp_z[-1]
                #print("start","end",start,end)
                ###print(self.buffer_ini_azi[:120])

                if step>=2:
                    if self.flag<step-1:
                        limit_i=self.buf_azi[len(tmp_z)*(self.flag+1)]
                        limit_s=self.buf_azi[len(tmp_z)*(self.flag+2)-1]
                        print("flag",self.flag,limit_i,limit_s)
                        if limit_i< tmp_z[-1]< limit_s:
                            index_i=int(numpy.where(tmp_z<=self.buf_azi[len(tmp_z)*(self.flag+1)])[0][-1])
                            tmp_r    =int(numpy.where(self.buf_azi[(self.flag+1)*len(tmp_z):(self.flag+2)*len(tmp_z)]>=tmp_z[-1])[0][0])
                            print("tmp_r",tmp_r)
                            index_f=(self.flag+1)*len(tmp_z)+tmp_r

                            if len(tmp_z[index_i:])>len(self.buf_azi[len(tmp_z)*(self.flag+1):index_f]):
                                final = len(self.buf_azi[len(tmp_z)*(self.flag+1):index_f])
                            else:
                                final= len(tmp_z[index_i:])
                            self.buf_azi[len(tmp_z)*(self.flag+1):index_f]=tmp_z[index_i:index_i+final]
                            self.buf_tmp[len(tmp_z)*(self.flag+1):index_f,:]=tmp_v[index_i:index_i+final,:]
                        if limit_i<tmp_z[0]<limit_s:
                            index_f =int(numpy.where(self.buf_azi>=tmp_z[-1])[0][0])
                            n_p =index_f-len(tmp_z)*(self.flag+1)
                            if n_p>0:
                                self.buf_azi[len(tmp_z)*(self.flag+1):index_f]=tmp_z[-1]*numpy.ones(n_p)
                                self.buf_tmp[len(tmp_z)*(self.flag+1):index_f,:]=tmp_v[-1,:]*numpy.ones([n_p,tmp_v.shape[1]])

                '''
                        if self.buf_azi[len(tmp_z)]<tmp_z[-1]<self.buf_azi[2*len(tmp_z)-1]:
                            index_i= int(numpy.where(tmp_z  <=  self.buf_azi[len(tmp_z)])[0][-1])
                            index_f= int(numpy.where(self.buf_azi>=tmp_z[-1])[0][0])
                            #print("index",index_i,index_f)
                            if len(tmp_z[index_i:])>len(self.buf_azi[len(tmp_z):index_f]):
                                final = len(self.buf_azi[len(tmp_z):index_f])
                            else:
                                final = len(tmp_z[index_i:])
                            self.buf_azi[len(tmp_z):index_f]=tmp_z[index_i:index_i+final]
                            self.buf_tmp[len(tmp_z):index_f,:]=tmp_v[index_i:index_i+final,:]
                '''
                self.buf_tmp[len(tmp_z)*(self.flag):len(tmp_z)*(self.flag+1),:]=tmp_v
                self.buf_azi[len(tmp_z)*(self.flag):len(tmp_z)*(self.flag+1)] = tmp_z
                self.buffer_ini=self.buf_tmp
                self.buffer_ini_azi = self.buf_azi
                ##print("--------salida------------")
                start= tmp_z[0]
                end  = tmp_z[-1]
                ##print("start","end",start,end)
                ##print(self.buffer_ini_azi[:120])
                self.ini= self.ini+1
                self.flag = self.flag +1
                if self.flag==step:
                    self.flag=0
        numpy.set_printoptions(suppress=True)
        print("buffer_ini_azi")
        print(self.buffer_ini_azi[:20])
        print(self.buffer_ini_azi[-40:])
        for i,ax in enumerate(self.axes):
            if ax.firsttime:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.buffer_ini,r=r,az=self.buffer_ini_azi,fig=self.figures[0], proj='cg', vmin=1, vmax=60)
            else:
                plt.clf()
                cgax, pm = wrl.vis.plot_ppi(self.buffer_ini,r=r,az=self.buffer_ini_azi,fig=self.figures[0], proj='cg', vmin=1, vmax=60)
        caax = cgax.parasites[0]
        paax = cgax.parasites[1]
        cbar = plt.gcf().colorbar(pm, pad=0.075)
        caax.set_xlabel('x_range [km]')
        caax.set_ylabel('y_range [km]')
        plt.text(1.0, 1.05, 'azimuth '+str(thisDatetime)+"step"+str(self.ini), transform=caax.transAxes, va='bottom',ha='right')
        #import time
        #time.sleep(0.5)
