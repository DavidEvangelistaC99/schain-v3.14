import numpy as np
import matplotlib.pyplot as pl
import wradlib
import warnings
#export WRADLIB_DATA=/path/to/wradlib-data
warnings.filterwarnings('ignore')
'''
try:
    get_ipython().magic('matplotlib inline')
except:
    pl.ion()
'''
filename = wradlib.util.get_wradlib_data_file("/home/soporte/Downloads/raa00-dx_10908-0806021735-fbg---bin.gz")
img, meta = wradlib.io.read_dx(filename)
print("Shape of polar array: %r\n" % (img.shape,))
print("Some meta data of the DX file:")
print("\tdatetime: %r" % (meta["datetime"],))
print("\tRadar ID: %s" % (meta["radarid"],))

img[200:250,:]= np.ones([50,img.shape[1]])*np.nan

img[300:360,:]= np.ones([60,img.shape[1]])*np.nan

cgax, pm= wradlib.vis.plot_ppi(img)
txt = pl.title('Simple PPI')
print("coordenada angular",img[:,0],len(img[:,0]))
print("COORDENADA 0",img[0],len(img[0]))
cbar = pl.gcf().colorbar(pm, pad=0.075)

#r = np.arange(40, 80)
#az = np.arange(200, 250)
#ax, pm = wradlib.vis.plot_ppi(img[200:250, 40:80], r, az, autoext=False)
#ax, pm = wradlib.vis.plot_ppi(img[200:250, 40:80], r, az)

#txt = pl.title('Sector PPI')
pl.show()
