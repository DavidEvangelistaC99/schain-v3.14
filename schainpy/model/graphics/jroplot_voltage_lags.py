
import os
import datetime
import numpy
from schainpy.model.proc.jroproc_base import ProcessingUnit, Operation, MPDecorator  #YONG

from .jroplot_spectra import RTIPlot, NoisePlot

from schainpy.utils import log
from .plotting_codes import *

from schainpy.model.graphics.jroplot_base import Plot, plt

import matplotlib.pyplot as plt
import matplotlib.colors as colors

import time
import math


from matplotlib.ticker import MultipleLocator



class RTIDPPlot(RTIPlot):

    '''
       Plot for RTI Double Pulse Experiment
    '''

    CODE = 'RTIDP'
    colormap = 'jro'
    plot_name = 'RTI'

    #cb_label = 'Ne Electron Density (1/cm3)'

    def setup(self):
        self.xaxis = 'time'
        self.ncols = 1
        self.nrows = 3
        self.nplots = self.nrows
        #self.height=10
        if self.showSNR:
            self.nrows += 1
            self.nplots += 1

        self.ylabel = 'Height [km]'
        self.xlabel = 'Time (LT)'

        self.cb_label = 'Intensity (dB)'


        #self.cb_label = cb_label

        self.titles = ['{} Channel {}'.format(
            self.plot_name.upper(), '0x1'),'{} Channel {}'.format(
                self.plot_name.upper(), '0'),'{} Channel {}'.format(
                    self.plot_name.upper(), '1')]


    def plot(self):

        self.data.normalize_heights()
        self.x = self.data.times
        self.y = self.data.heights[0:self.data.NDP]

        if self.showSNR:
            self.z = numpy.concatenate(
                (self.data[self.CODE], self.data['snr'])
            )
        else:

            self.z = self.data[self.CODE]
            #print(numpy.max(self.z[0,0:]))

        self.z = numpy.ma.masked_invalid(self.z)

        if self.decimation is None:
            x, y, z = self.fill_gaps(self.x, self.y, self.z)
        else:
            x, y, z = self.fill_gaps(*self.decimate())

        for n, ax in enumerate(self.axes):


            self.zmax = self.zmax if self.zmax is not None else numpy.max(
                self.z[1][0,12:40])
            self.zmin = self.zmin if self.zmin is not None else numpy.min(
                self.z[1][0,12:40])



            if ax.firsttime:

                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]


                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )
                #plt.tight_layout()
            else:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.collections.remove(ax.collections[0])
                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )
                #plt.tight_layout()


class RTILPPlot(RTIPlot):

    '''
       Plot for RTI Long Pulse
    '''

    CODE = 'RTILP'
    colormap = 'jro'
    plot_name = 'RTI LP'

    #cb_label = 'Ne Electron Density (1/cm3)'

    def setup(self):
        self.xaxis = 'time'
        self.ncols = 1
        self.nrows = 4
        self.nplots = self.nrows
        if self.showSNR:
            self.nrows += 1
            self.nplots += 1

        self.ylabel = 'Height [km]'
        self.xlabel = 'Time (LT)'

        self.cb_label = 'Intensity (dB)'



        #self.cb_label = cb_label

        self.titles = ['{} Channel {}'.format(
            self.plot_name.upper(), '0'),'{} Channel {}'.format(
                self.plot_name.upper(), '1'),'{} Channel {}'.format(
                    self.plot_name.upper(), '2'),'{} Channel {}'.format(
                        self.plot_name.upper(), '3')]


    def plot(self):

        self.data.normalize_heights()
        self.x = self.data.times
        self.y = self.data.heights[0:self.data.NRANGE]

        if self.showSNR:
            self.z = numpy.concatenate(
                (self.data[self.CODE], self.data['snr'])
            )
        else:

            self.z = self.data[self.CODE]
            #print(numpy.max(self.z[0,0:]))

        self.z = numpy.ma.masked_invalid(self.z)

        if self.decimation is None:
            x, y, z = self.fill_gaps(self.x, self.y, self.z)
        else:
            x, y, z = self.fill_gaps(*self.decimate())

        for n, ax in enumerate(self.axes):


            self.zmax = self.zmax if self.zmax is not None else numpy.max(
                self.z[1][0,12:40])
            self.zmin = self.zmin if self.zmin is not None else numpy.min(
                self.z[1][0,12:40])

            if ax.firsttime:

                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]


                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )
                #plt.tight_layout()
            else:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.collections.remove(ax.collections[0])
                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )
                #plt.tight_layout()


class DenRTIPlot(RTIPlot):

    '''
       Plot for Den
    '''

    CODE = 'denrti'
    colormap = 'jro'
    plot_name = 'Electron Density'

    #cb_label = 'Ne Electron Density (1/cm3)'

    def setup(self):
        self.xaxis = 'time'
        self.ncols = 1
        self.nrows = self.data.shape(self.CODE)[0]
        self.nplots = self.nrows
        if self.showSNR:
            self.nrows += 1
            self.nplots += 1

        self.ylabel = 'Height [km]'
        self.xlabel = 'Time (LT)'

        self.plots_adjust.update({'wspace': 0.8, 'hspace':0.2, 'left': 0.2, 'right': 0.9, 'bottom': 0.18})

        if self.CODE == 'denrti' or self.CODE=='denrtiLP':
            self.cb_label = r'$\mathrm{N_e}$ Electron Density ($\mathrm{1/cm^3}$)'

        #self.cb_label = cb_label
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.plot_name)]
            if self.showSNR:
                self.titles.append('SNR')

    def plot(self):

        self.data.normalize_heights()
        self.x = self.data.times
        self.y = self.data.heights



        if self.showSNR:
            self.z = numpy.concatenate(
                (self.data[self.CODE], self.data['snr'])
            )
        else:
            self.z = self.data[self.CODE]

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
                if numpy.log10(self.zmin)<0:
                    self.zmin=1
                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n],
                                       norm=colors.LogNorm()
                                       )
                #plt.tight_layout()

            else:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.collections.remove(ax.collections[0])
                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n],
                                       norm=colors.LogNorm()
                                       )
                #plt.tight_layout()



class DenRTILPPlot(DenRTIPlot):

    '''
       Plot for Electron Temperature
    '''

    CODE = 'denrtiLP'
    colormap = 'jro'
    plot_name = 'Electron Density'


class ETempRTIPlot(RTIPlot):

    '''
       Plot for Electron Temperature
    '''

    CODE = 'ETemp'
    colormap = 'jet'
    plot_name = 'Electron Temperature'

    #cb_label = 'Ne Electron Density (1/cm3)'

    def setup(self):
        self.xaxis = 'time'
        self.ncols = 1
        self.nrows = self.data.shape(self.CODE)[0]
        self.nplots = self.nrows
        if self.showSNR:
            self.nrows += 1
            self.nplots += 1

        self.ylabel = 'Height [km]'
        self.xlabel = 'Time (LT)'
        self.plots_adjust.update({'wspace': 0.8, 'hspace':0.2, 'left': 0.2, 'right': 0.9, 'bottom': 0.18})
        if self.CODE == 'ETemp' or self.CODE == 'ETempLP':
            self.cb_label = 'Electron Temperature (K)'
        if self.CODE == 'ITemp' or self.CODE == 'ITempLP':
            self.cb_label = 'Ion Temperature (K)'


        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.plot_name)]
            if self.showSNR:
                self.titles.append('SNR')

    def plot(self):

        self.data.normalize_heights()
        self.x = self.data.times
        self.y = self.data.heights

        if self.showSNR:
            self.z = numpy.concatenate(
                (self.data[self.CODE], self.data['snr'])
            )
        else:
            self.z = self.data[self.CODE]

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
                #plt.tight_layout()

            else:
                if self.zlimits is not None:
                    self.zmin, self.zmax = self.zlimits[n]
                ax.collections.remove(ax.collections[0])
                ax.plt = ax.pcolormesh(x, y, z[n].T * self.factors[n],
                                       vmin=self.zmin,
                                       vmax=self.zmax,
                                       cmap=self.cmaps[n]
                                       )
                #plt.tight_layout()



class ITempRTIPlot(ETempRTIPlot):

    '''
       Plot for Ion Temperature
    '''

    CODE = 'ITemp'
    colormap = 'jet'
    plot_name = 'Ion Temperature'


class ElectronTempLPPlot(ETempRTIPlot):

    '''
       Plot for Electron Temperature LP
    '''

    CODE = 'ETempLP'
    colormap = 'jet'
    plot_name = 'Electron Temperature'


class IonTempLPPlot(ETempRTIPlot):

    '''
       Plot for Ion Temperature LP
    '''

    CODE = 'ITempLP'
    colormap = 'jet'
    plot_name = 'Ion Temperature'


class HFracRTIPlot(ETempRTIPlot):

    '''
       Plot for H+ LP
    '''

    CODE = 'HFracLP'
    colormap = 'jet'
    plot_name = 'H+ Frac'


class HeFracRTIPlot(ETempRTIPlot):

    '''
       Plot for He+ LP
    '''

    CODE = 'HeFracLP'
    colormap = 'jet'
    plot_name = 'He+ Frac'


class TempsDPPlot(Plot):
    '''
    Plot for Electron - Ion Temperatures
    '''

    CODE = 'tempsDP'
    plot_name = 'Temperatures'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = 'Temperature (K)'
        self.width = 3.5
        self.height = 5.5
        self.colorbar = False
        self.plots_adjust.update({'wspace': 0.8, 'hspace':0.2, 'left': 0.2, 'right': 0.9, 'bottom': 0.18})
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]

    def plot(self):

        self.x = self.data['tempsDP'][:,-1]
        self.y = self.data.heights[0:self.data.NSHTS]

        self.xmin = -100
        self.xmax = 5000
        ax = self.axes[0]

        if ax.firsttime:

            ax.errorbar(self.x, self.y, xerr=self.data.ete2, fmt='r^',elinewidth=1.0,color='b',linewidth=2.0, label='Te')
            ax.errorbar(self.data.ti2, self.y, fmt='k^', xerr=self.data.eti2,elinewidth=1.0,color='b',linewidth=2.0, label='Ti')
            plt.legend(loc='lower right')
            self.ystep_given = 50
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            ax.grid(which='minor')
            #plt.tight_layout()


        else:
            self.clear_figures()
            ax.errorbar(self.x, self.y, xerr=self.data.ete2, fmt='r^',elinewidth=1.0,color='b',linewidth=2.0, label='Te')
            ax.errorbar(self.data.ti2, self.y, fmt='k^', xerr=self.data.eti2,elinewidth=1.0,color='b',linewidth=2.0, label='Ti')
            plt.legend(loc='lower right')
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            #plt.tight_layout()


class TempsHPPlot(Plot):
    '''
    Plot for Temperatures Hybrid Experiment
    '''

    CODE = 'temps_LP'
    plot_name = 'Temperatures'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = 'Temperature (K)'
        self.width = 3.5
        self.height = 6.5
        self.colorbar = False
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]

    def plot(self):

        self.x = self.data['temps_LP'][:,-1]
        self.y = self.data.heights[0:self.data.NACF]
        self.xmin = -100
        self.xmax = 4500
        ax = self.axes[0]

        if ax.firsttime:

            ax.errorbar(self.x, self.y, xerr=self.data.ete, fmt='r^',elinewidth=1.0,color='b',linewidth=2.0, label='Te')
            ax.errorbar(self.data.ti, self.y, fmt='k^', xerr=self.data.eti,elinewidth=1.0,color='b',linewidth=2.0, label='Ti')
            plt.legend(loc='lower right')
            self.ystep_given = 200
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            ax.grid(which='minor')
            #plt.tight_layout()


        else:
            self.clear_figures()
            ax.errorbar(self.x, self.y, xerr=self.data.ete, fmt='r^',elinewidth=1.0,color='b',linewidth=2.0, label='Te')
            ax.errorbar(self.data.ti, self.y, fmt='k^', xerr=self.data.eti,elinewidth=1.0,color='b',linewidth=2.0, label='Ti')
            plt.legend(loc='lower right')
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            #plt.tight_layout()


class FracsHPPlot(Plot):
    '''
    Plot for Composition LP
    '''

    CODE = 'fracs_LP'
    plot_name = 'Composition'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = 'Frac'
        self.width = 3.5
        self.height = 6.5
        self.colorbar = False
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]

    def plot(self):

        self.x = self.data['fracs_LP'][:,-1]
        self.y = self.data.heights[0:self.data.NACF]

        self.xmin = 0
        self.xmax = 1
        ax = self.axes[0]

        if ax.firsttime:

            ax.errorbar(self.x, self.y[self.data.cut:], xerr=self.data.eph, fmt='r^',elinewidth=1.0,color='b',linewidth=2.0, label='H+')
            ax.errorbar(self.data.phe, self.y[self.data.cut:], fmt='k^', xerr=self.data.ephe,elinewidth=1.0,color='b',linewidth=2.0, label='He+')
            plt.legend(loc='lower right')
            self.xstep_given = 0.2
            self.ystep_given = 200
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            ax.grid(which='minor')
            #plt.tight_layout()


        else:
            self.clear_figures()
            ax.errorbar(self.x, self.y[self.data.cut:], xerr=self.data.eph, fmt='r^',elinewidth=1.0,color='b',linewidth=2.0, label='H+')
            ax.errorbar(self.data.phe, self.y[self.data.cut:], fmt='k^', xerr=self.data.ephe,elinewidth=1.0,color='b',linewidth=2.0, label='He+')
            plt.legend(loc='lower right')
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            #plt.tight_layout()



class EDensityPlot(Plot):
    '''
    Plot for electron density
    '''

    CODE = 'den'
    plot_name = 'Electron Density'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = r'$\mathrm{N_e}$ Electron Density ($\mathrm{1/cm^3}$)'
        self.width = 4
        self.height = 6.5
        self.colorbar = False
        self.plots_adjust.update({'wspace': 0.8, 'hspace':0.2, 'left': 0.2, 'right': 0.9, 'bottom': 0.18})
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]

    def plot(self):


        self.x = self.data[self.CODE]
        self.y = self.data.heights
        self.xmin = 1000
        self.xmax = 10000000
        ax = self.axes[0]

        if ax.firsttime:
            self.autoxticks=False
            #if self.CODE=='den':
            ax.errorbar(self.data.dphi, self.y[:self.data.NSHTS], xerr=1, fmt='h-',elinewidth=1.0,color='g',linewidth=1.0, label='Faraday Profile',markersize=2)
            #ax.errorbar(self.data.dphi, self.y[:self.data.NSHTS], xerr=self.data.sdn1, fmt='h-',elinewidth=1.0,color='g',linewidth=1.0, label='Faraday Profile',markersize=2)

            ax.errorbar(self.x[:,-1], self.y[:self.data.NSHTS], fmt='k^-', xerr=self.data.sdp2,elinewidth=1.0,color='b',linewidth=1.0, label='Power Profile',markersize=2)
            #else:
                #ax.errorbar(self.data.dphi[:self.data.cut], self.y[:self.data.cut], xerr=1, fmt='h-',elinewidth=1.0,color='g',linewidth=1.0, label='Faraday Profile',markersize=2)
                #ax.errorbar(self.x[:self.data.cut,-1], self.y[:self.data.cut], fmt='k^-', xerr=self.data.sdp2[:self.data.cut],elinewidth=1.0,color='b',linewidth=1.0, label='Power Profile',markersize=2)

            if self.CODE=='denLP':
                ax.errorbar(self.data.ne[self.data.cut:], self.y[self.data.cut:], xerr=self.data.ene[self.data.cut:], fmt='r^-',elinewidth=1.0,color='r',linewidth=1.0, label='LP Profile',markersize=2)

            plt.legend(loc='upper right')
            ax.set_xscale("log", nonposx='clip')
            grid_y_ticks=numpy.arange(numpy.nanmin(self.y),numpy.nanmax(self.y),50)
            self.ystep_given=100
            if self.CODE=='denLP':
                self.ystep_given=200
            ax.set_yticks(grid_y_ticks,minor=True)
            ax.grid(which='minor')
            #plt.tight_layout()



        else:

            self.clear_figures()
            #if self.CODE=='den':
            ax.errorbar(self.data.dphi, self.y[:self.data.NSHTS], xerr=1, fmt='h-',elinewidth=1.0,color='g',linewidth=1.0, label='Faraday Profile',markersize=2)
            #ax.errorbar(self.data.dphi, self.y[:self.data.NSHTS], xerr=self.data.sdn1, fmt='h-',elinewidth=1.0,color='g',linewidth=1.0, label='Faraday Profile',markersize=2)

            ax.errorbar(self.x[:,-1], self.y[:self.data.NSHTS], fmt='k^-', xerr=self.data.sdp2,elinewidth=1.0,color='b',linewidth=1.0, label='Power Profile',markersize=2)
            ax.errorbar(self.x[:,-2], self.y[:self.data.NSHTS], elinewidth=1.0,color='r',linewidth=0.5,linestyle="dashed")
            #else:
                #ax.errorbar(self.data.dphi[:self.data.cut], self.y[:self.data.cut], xerr=1, fmt='h-',elinewidth=1.0,color='g',linewidth=1.0, label='Faraday Profile',markersize=2)
                #ax.errorbar(self.x[:self.data.cut,-1], self.y[:self.data.cut], fmt='k^-', xerr=self.data.sdp2[:self.data.cut],elinewidth=1.0,color='b',linewidth=1.0, label='Power Profile',markersize=2)
                #ax.errorbar(self.x[:self.data.cut,-2], self.y[:self.data.cut], elinewidth=1.0,color='r',linewidth=0.5,linestyle="dashed")

            if self.CODE=='denLP':
                ax.errorbar(self.data.ne[self.data.cut:], self.y[self.data.cut:], fmt='r^-', xerr=self.data.ene[self.data.cut:],elinewidth=1.0,color='r',linewidth=1.0, label='LP Profile',markersize=2)

            ax.set_xscale("log", nonposx='clip')
            grid_y_ticks=numpy.arange(numpy.nanmin(self.y),numpy.nanmax(self.y),50)
            ax.set_yticks(grid_y_ticks,minor=True)
            ax.grid(which='minor')
            plt.legend(loc='upper right')
            #plt.tight_layout()

class FaradayAnglePlot(Plot):
    '''
    Plot for electron density
    '''

    CODE = 'FaradayAngle'
    plot_name = 'Faraday Angle'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = 'Faraday Angle (º)'
        self.width = 4
        self.height = 6.5
        self.colorbar = False
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]

    def plot(self):


        self.x = self.data[self.CODE]
        self.y = self.data.heights
        self.xmin = -180
        self.xmax = 180
        ax = self.axes[0]

        if ax.firsttime:
            self.autoxticks=False
            #if self.CODE=='den':
            ax.plot(self.x, self.y,marker='o',color='g',linewidth=1.0,markersize=2)

            grid_y_ticks=numpy.arange(numpy.nanmin(self.y),numpy.nanmax(self.y),50)
            self.ystep_given=100
            if self.CODE=='denLP':
                self.ystep_given=200
            ax.set_yticks(grid_y_ticks,minor=True)
            ax.grid(which='minor')
            #plt.tight_layout()
        else:

            self.clear_figures()
            #if self.CODE=='den':
            #print(numpy.shape(self.x))
            ax.plot(self.x[:,-1], self.y, marker='o',color='g',linewidth=1.0, markersize=2)

            grid_y_ticks=numpy.arange(numpy.nanmin(self.y),numpy.nanmax(self.y),50)
            ax.set_yticks(grid_y_ticks,minor=True)
            ax.grid(which='minor')

class EDensityHPPlot(EDensityPlot):

    '''
       Plot for Electron Density Hybrid Experiment
    '''

    CODE = 'denLP'
    plot_name = 'Electron Density'
    plot_type = 'scatterbuffer'


class ACFsPlot(Plot):
    '''
    Plot for ACFs Double Pulse Experiment
    '''

    CODE = 'acfs'
    plot_name = 'ACF'
    plot_type = 'scatterbuffer'


    def setup(self):
        #self.xaxis = 'time'
        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = 'lags (ms)'
        self.width = 3.5
        self.height = 6
        self.colorbar = False
        self.plots_adjust.update({'wspace': 0.8, 'hspace':0.2, 'left': 0.2, 'right': 0.9, 'bottom': 0.18})
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]

    def plot(self):

        self.x = self.data.lags_to_plot
        self.y = self.data['acfs'][:,-1]


        self.xmin = 0.0
        self.xmax = 2.0

        ax = self.axes[0]

        if ax.firsttime:

            for i in range(self.data.NSHTS):
                x_aux = numpy.isfinite(self.x[i,:])
                y_aux = numpy.isfinite(self.y[i,:])
                yerr_aux = numpy.isfinite(self.data.acfs_error_to_plot[i,:])
                x_igcej_aux = numpy.isfinite(self.data.x_igcej_to_plot[i,:])
                y_igcej_aux = numpy.isfinite(self.data.y_igcej_to_plot[i,:])
                x_ibad_aux = numpy.isfinite(self.data.x_ibad_to_plot[i,:])
                y_ibad_aux = numpy.isfinite(self.data.y_ibad_to_plot[i,:])
                if self.x[i,:][~numpy.isnan(self.x[i,:])].shape[0]>2:
                    ax.errorbar(self.x[i,x_aux], self.y[i,y_aux], yerr=self.data.acfs_error_to_plot[i,x_aux],color='b',marker='o',linewidth=1.0,markersize=2)
                ax.plot(self.data.x_igcej_to_plot[i,x_igcej_aux],self.data.y_igcej_to_plot[i,y_igcej_aux],'x',color='red',markersize=2)
                ax.plot(self.data.x_ibad_to_plot[i,x_ibad_aux],self.data.y_ibad_to_plot[i,y_ibad_aux],'X',color='red',markersize=2)

            self.xstep_given = (self.xmax-self.xmin)/(self.data.DPL-1)
            self.ystep_given = 50
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            ax.grid(which='minor')



        else:
            self.clear_figures()

            for i in range(self.data.NSHTS):
                x_aux = numpy.isfinite(self.x[i,:])
                y_aux = numpy.isfinite(self.y[i,:])
                yerr_aux = numpy.isfinite(self.data.acfs_error_to_plot[i,:])
                x_igcej_aux = numpy.isfinite(self.data.x_igcej_to_plot[i,:])
                y_igcej_aux = numpy.isfinite(self.data.y_igcej_to_plot[i,:])
                x_ibad_aux = numpy.isfinite(self.data.x_ibad_to_plot[i,:])
                y_ibad_aux = numpy.isfinite(self.data.y_ibad_to_plot[i,:])
                if self.x[i,:][~numpy.isnan(self.x[i,:])].shape[0]>2:
                    ax.errorbar(self.x[i,x_aux], self.y[i,y_aux], yerr=self.data.acfs_error_to_plot[i,x_aux],linewidth=1.0,markersize=2,color='b',marker='o')
                ax.plot(self.data.x_igcej_to_plot[i,x_igcej_aux],self.data.y_igcej_to_plot[i,y_igcej_aux],'x',color='red',markersize=2)
                ax.plot(self.data.x_ibad_to_plot[i,x_ibad_aux],self.data.y_ibad_to_plot[i,y_ibad_aux],'X',color='red',markersize=2)
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            



class ACFsLPPlot(Plot):
    '''
    Plot for ACFs Double Pulse Experiment
    '''

    CODE = 'acfs_LP'
    plot_name = 'ACF'
    plot_type = 'scatterbuffer'


    def setup(self):
        #self.xaxis = 'time'
        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Range [km]'
        self.xlabel = 'lags (ms)'
        self.width = 3.5
        self.height = 7
        self.colorbar = False
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.CODE.upper())]



    def plot(self):

        self.x = self.data.lags_LP_to_plot
        self.y = self.data['acfs_LP'][:,-1]

        self.xmin = 0.0
        self.xmax = 1.5

        ax = self.axes[0]

        if ax.firsttime:

            for i in range(self.data.NACF):
                x_aux = numpy.isfinite(self.x[i,:])
                y_aux = numpy.isfinite(self.y[i,:])
                yerr_aux = numpy.isfinite(self.data.errors[i,:])

                if self.x[i,:][~numpy.isnan(self.x[i,:])].shape[0]>2:
                    ax.errorbar(self.x[i,x_aux], self.y[i,y_aux], yerr=self.data.errors[i,x_aux],color='b',linewidth=1.0,markersize=2,ecolor='r')

            #self.xstep_given = (self.xmax-self.xmin)/(self.data.NLAG-1)
            self.xstep_given=0.3
            self.ystep_given = 200
            ax.yaxis.set_minor_locator(MultipleLocator(15))
            ax.grid(which='minor')

        else:
            self.clear_figures()

            for i in range(self.data.NACF):
                x_aux = numpy.isfinite(self.x[i,:])
                y_aux = numpy.isfinite(self.y[i,:])
                yerr_aux = numpy.isfinite(self.data.errors[i,:])

                if self.x[i,:][~numpy.isnan(self.x[i,:])].shape[0]>2:
                    ax.errorbar(self.x[i,x_aux], self.y[i,y_aux], yerr=self.data.errors[i,x_aux],color='b',linewidth=1.0,markersize=2,ecolor='r')

            ax.yaxis.set_minor_locator(MultipleLocator(15))


class CrossProductsPlot(Plot):
    '''
    Plot for cross products
    '''

    CODE = 'crossprod'
    plot_name = 'Cross Products'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 3
        self.nrows = 1
        self.nplots = 3
        self.ylabel = 'Range [km]'

        self.width = 3.5*self.nplots
        self.height = 5.5
        self.colorbar = False
        self.titles = []

    def plot(self):

        self.x = self.data['crossprod'][:,-1,:,:,:,:]




        self.y = self.data.heights[0:self.data.NDP]



        for n, ax in enumerate(self.axes):

            self.xmin=numpy.min(numpy.concatenate((self.x[n][0,20:30,0,0],self.x[n][1,20:30,0,0],self.x[n][2,20:30,0,0],self.x[n][3,20:30,0,0])))
            self.xmax=numpy.max(numpy.concatenate((self.x[n][0,20:30,0,0],self.x[n][1,20:30,0,0],self.x[n][2,20:30,0,0],self.x[n][3,20:30,0,0])))


            if ax.firsttime:

                self.autoxticks=False
                if n==0:
                    label1='kax'
                    label2='kay'
                    label3='kbx'
                    label4='kby'
                    self.xlimits=[(self.xmin,self.xmax)]
                elif n==1:
                    label1='kax2'
                    label2='kay2'
                    label3='kbx2'
                    label4='kby2'
                    self.xlimits.append((self.xmin,self.xmax))
                elif n==2:
                    label1='kaxay'
                    label2='kbxby'
                    label3='kaxbx'
                    label4='kaxby'
                    self.xlimits.append((self.xmin,self.xmax))


                ax.plotline1 = ax.plot(self.x[n][0,:,0,0], self.y, color='r',linewidth=2.0, label=label1)
                ax.plotline2 = ax.plot(self.x[n][1,:,0,0], self.y, color='k',linewidth=2.0, label=label2)
                ax.plotline3 = ax.plot(self.x[n][2,:,0,0], self.y, color='b',linewidth=2.0, label=label3)
                ax.plotline4 = ax.plot(self.x[n][3,:,0,0], self.y, color='m',linewidth=2.0, label=label4)
                ax.legend(loc='upper right')
                ax.set_xlim(self.xmin, self.xmax)
                self.titles.append('{}'.format(self.plot_name.upper()))
                #plt.tight_layout()


            else:

                if n==0:
                    self.xlimits=[(self.xmin,self.xmax)]
                else:
                    self.xlimits.append((self.xmin,self.xmax))

                ax.set_xlim(self.xmin, self.xmax)


                ax.plotline1[0].set_data(self.x[n][0,:,0,0],self.y)
                ax.plotline2[0].set_data(self.x[n][1,:,0,0],self.y)
                ax.plotline3[0].set_data(self.x[n][2,:,0,0],self.y)
                ax.plotline4[0].set_data(self.x[n][3,:,0,0],self.y)
                self.titles.append('{}'.format(self.plot_name.upper()))
                #plt.tight_layout()



class CrossProductsLPPlot(Plot):
    '''
    Plot for cross products LP
    '''

    CODE = 'crossprodlp'
    plot_name = 'Cross Products LP'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 2
        self.nrows = 1
        self.nplots = 2
        self.ylabel = 'Range [km]'
        self.xlabel = 'dB'
        self.width = 3.5*self.nplots
        self.height = 5.5
        self.colorbar = False
        self.titles = []
        self.plotline_array=numpy.zeros((2,self.data.NLAG),dtype=object)
    def plot(self):


        self.x = self.data[self.CODE][:,-1,:,:]


        self.y = self.data.heights[0:self.data.NRANGE]


        label_array=numpy.array(['lag '+ str(x) for x in range(self.data.NLAG)])
        color_array=['r','k','g','b','c','m','y','orange','steelblue','purple','peru','darksalmon','grey','limegreen','olive','midnightblue']


        for n, ax in enumerate(self.axes):

            self.xmin=30
            self.xmax=70
            #print(self.x[0,12:15,n])
            #input()
            #self.xmin=numpy.min(numpy.concatenate((self.x[0,:,n],self.x[1,:,n])))
            #self.xmax=numpy.max(numpy.concatenate((self.x[0,:,n],self.x[1,:,n])))

            #print("before",self.plotline_array)

            if ax.firsttime:

                self.autoxticks=False


                for i in range(self.data.NLAG):
                    #print(i)
                    #print(numpy.shape(self.x))
                    self.plotline_array[n,i], = ax.plot(self.x[i,:,n], self.y, color=color_array[i],linewidth=1.0, label=label_array[i])
                #ax.plotline1 = ax.plot(self.x[0,:,n], self.y, color='r',linewidth=2.0, label=label_array[0])
                #ax.plotline2 = ax.plot(self.x[n][1,:,0,0], self.y, color='k',linewidth=2.0, label=label2)
                #ax.plotline3 = ax.plot(self.x[n][2,:,0,0], self.y, color='b',linewidth=2.0, label=label3)
                #ax.plotline4 = ax.plot(self.x[n][3,:,0,0], self.y, color='m',linewidth=2.0, label=label4)


                #print(self.plotline_array)



                ax.legend(loc='upper right')
                ax.set_xlim(self.xmin, self.xmax)
                if n==0:
                    self.titles.append('{} CH0'.format(self.plot_name.upper()))
                if n==1:
                    self.titles.append('{} CH1'.format(self.plot_name.upper()))

                #plt.tight_layout()

            else:
                #print(self.plotline_array)
                for i in range(self.data.NLAG):

                    self.plotline_array[n,i].set_data(self.x[i,:,n],self.y)



                #ax.plotline1[0].set_data(self.x[n][0,:,0,0],self.y)
                #ax.plotline2[0].set_data(self.x[n][1,:,0,0],self.y)
                #ax.plotline3[0].set_data(self.x[n][2,:,0,0],self.y)
                #ax.plotline4[0].set_data(self.x[n][3,:,0,0],self.y)

                if n==0:
                    self.titles.append('{} CH0'.format(self.plot_name.upper()))
                if n==1:
                    self.titles.append('{} CH1'.format(self.plot_name.upper()))

                #plt.tight_layout()


class NoiseDPPlot(NoisePlot):
    '''
    Plot for noise Double Pulse
    '''

    CODE = 'noisedp'
    plot_name = 'Noise'
    plot_type = 'scatterbuffer'


class XmitWaveformPlot(Plot):
    '''
    Plot for xmit waveform
    '''

    CODE = 'xmit'
    plot_name = 'Xmit Waveform'
    plot_type = 'scatterbuffer'


    def setup(self):

        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = ''
        self.xlabel = 'Number of Lag'
        self.width = 5.5
        self.height = 3.5
        self.colorbar = False
        if not self.titles:
            self.titles = self.data.parameters \
                if self.data.parameters else ['{}'.format(self.plot_name.upper())]

    def plot(self):

        self.x = numpy.arange(0,self.data.NLAG,1,'float32')
        self.y = self.data['xmit'][:,-1,:]

        self.xmin = 0
        self.xmax = self.data.NLAG-1
        self.ymin = -1.0
        self.ymax = 1.0
        ax = self.axes[0]

        if ax.firsttime:
            ax.plotline0=ax.plot(self.x,self.y[0,:],color='blue')
            ax.plotline1=ax.plot(self.x,self.y[1,:],color='red')
            secax=ax.secondary_xaxis(location=0.5)
            secax.xaxis.tick_bottom()
            secax.tick_params( labelleft=False, labeltop=False,
                      labelright=False, labelbottom=False)

            self.xstep_given = 3
            self.ystep_given = .25
            secax.set_xticks(numpy.linspace(self.xmin, self.xmax, 6)) #only works on matplotlib.version>3.2

        else:
            ax.plotline0[0].set_data(self.x,self.y[0,:])
            ax.plotline1[0].set_data(self.x,self.y[1,:])
