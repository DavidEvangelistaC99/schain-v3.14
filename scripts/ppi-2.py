import os
import h5py
import numpy as np
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

from cartopy.feature import ShapelyFeature
from matplotlib.patches import Circle


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

RADAR_LAT = -12.04042
RADAR_LON = -75.29591

XRANGE = 60       # km

# PATH = "/home/david/Documents/DATA/HYO@2025-11-11T00-00-34/param-01_AUG/SNR_PPI_EL_1.0/SOPHY_20251031_000826_E1.0_SNR.hdf5"
PATH = "/home/david/Documents/DATA/CHIRP@2025-10-07T19-57-06/param-01_AUG/SNR_PPI_EL_1.0/SOPHY_20251007_200049_E1.0_SNR.hdf5"

SHAPES = "/home/david/Documents/schain-v3.14/scripts/shapes"

# ==========================================================
# Conversión km -> grados
# ==========================================================

def km2deg(km):
    return km / 111.32


# ==========================================================
# Leer HDF5
# ==========================================================

with h5py.File(PATH,"r") as f:

    mask = -2.75
    H = f["Data/snr/H"][:]
    H = 10*np.log10(H)

    #mask_array = H < mask
    #H[mask_array] = np.nan


    az = f["Metadata/azimuth"][:]
    ele = f["Metadata/elevation"][:]

    r = f["Metadata/range"][:]

# Si el rango está en metros

# r = r/1000.


# ==========================================================
# Coordenadas PPI
# ==========================================================

theta = -np.deg2rad(az) + np.pi/2

R,TH = np.meshgrid(r,theta)

mean_el = np.mean(ele)

x = R*np.cos(TH)*np.cos(np.deg2rad(mean_el))
y = R*np.sin(TH)*np.cos(np.deg2rad(mean_el))

lon = km2deg(x) + RADAR_LON
lat = km2deg(y) + RADAR_LAT


# ==========================================================
# Figura
# ==========================================================

fig = plt.figure(figsize=(11,11))

ax = plt.axes(projection=ccrs.PlateCarree())

# ax.set_facecolor("#202020")
ax.set_facecolor("#FFEBCD")

ax.set_extent([
    RADAR_LON-km2deg(XRANGE),
    RADAR_LON+km2deg(XRANGE),
    RADAR_LAT-km2deg(XRANGE),
    RADAR_LAT+km2deg(XRANGE)
])


# ==========================================================
# GRID
# ==========================================================

gl = ax.gridlines(draw_labels=True,
                  linewidth=0.7,
                  linestyle='--',
                  alpha=0.5)

gl.top_labels=False
gl.right_labels=False


# ==========================================================
# SHAPEFILES
# ==========================================================

'''reader = shpreader.Reader(
    os.path.join(SHAPES,"Distritos/PER_adm3.shp"),
    encoding="latin1"
)

feature = ShapelyFeature(
    reader.geometries(),
    ccrs.PlateCarree(),
    facecolor="none",
    edgecolor="gray",
    linewidth=0.4
)

ax.add_feature(feature)'''


reader = shpreader.Reader(
    os.path.join(SHAPES,"PER_ADM2/PER_ADM2.shp"),
    encoding="latin1"
)

feature = ShapelyFeature(
    reader.geometries(),
    ccrs.PlateCarree(),
    facecolor="none",
    edgecolor="#4682B4",
    linewidth=1
)

ax.add_feature(feature)


reader = shpreader.Reader(
    os.path.join(SHAPES,"Carreteras/VIAS_NACIONAL_250000.shp"),
    encoding="latin1"
)

feature = ShapelyFeature(
    reader.geometries(),
    ccrs.PlateCarree(),
    facecolor="none",
    edgecolor="#FF6347",
    linewidth=0.8
)

ax.add_feature(feature)


# ==========================================================
# CIUDADES
# ==========================================================

'''reader = shpreader.Reader(
    os.path.join(SHAPES,"CAPITALES/cap_distrito.shp"),
    encoding="latin1"
)

for rec in reader.records():

    nombre = rec.attributes["NOMBRE"]

    ax.text(
        rec.attributes["X"],
        rec.attributes["Y"],
        nombre,
        fontsize=7,
        color="white"
    )'''

reader = shpreader.Reader(
    os.path.join(SHAPES, "CAPITALES/cap_distrito.shp"),
    encoding="latin1"
)

ciudades = (
    "CONCEPCIÓN",
    "HUANCAYO",
    "JAUJA",
    #"LA OROYA",
    "CHUPACA"
)

for rec in reader.records():

    if rec.attributes["NOMBRE"] in ciudades:

        ax.text(
            rec.attributes["X"],
            rec.attributes["Y"],
            rec.attributes["NOMBRE"],
            fontsize=8,
            color="#800000",
            fontweight="bold"
        )


# ==========================================================
# ANILLOS
# ==========================================================

for R in [10,20,30,40,50,60]:

    c = Circle(
        (RADAR_LON,RADAR_LAT),
        km2deg(R),
        fill=False,
        edgecolor="#4682B4",
        linewidth=0.8,
        alpha=0.6,
        transform=ccrs.PlateCarree()
    )

    ax.add_patch(c)

    ax.text(
        RADAR_LON+km2deg(R/np.sqrt(2)),
        RADAR_LAT+km2deg(R/np.sqrt(2)),
        f"{R} km",
        fontsize=7,
        color="#4682B4"
    )


# ==========================================================
# RADAR
# ==========================================================

ax.plot(
    -75.3199751, 
    -12.041787,
    # RADAR_LON,
    # RADAR_LAT,
    marker="*",
    markersize=5,
    color="red",
    transform=ccrs.PlateCarree()
)


# ==========================================================
# PPI
# ==========================================================

'''pcm = ax.pcolormesh(
    lon,
    lat,
    H,
    shading="auto",
    cmap="jet",
    vmin=-10,
    vmax=40,
    transform=ccrs.PlateCarree()
)'''

'''pcm = ax.scatter(
    0,
    0,
    s=0.05,
    color="red",
    transform=ccrs.PlateCarree()
)'''

pcm = ax.pcolormesh(
    lon,
    lat,
    H,
    shading="auto",
    cmap="jet",
    vmin=-10,
    vmax=40,
    transform=ccrs.PlateCarree()
)

print("Radar")
print(RADAR_LAT, RADAR_LON)

print("\nLongitud")
print(np.nanmin(lon), np.nanmax(lon))

print("\nLatitud")
print(np.nanmin(lat), np.nanmax(lat))

print("\nRange")
print(r[0], r[-1])

print("\nAzimuth")
print(np.nanmin(az), np.nanmax(az))

cbar = plt.colorbar(pcm, pad=0.02)
cbar.set_label("SNR (dB)")

plt.title(f"PPI SNR  EL={mean_el:.1f}°")

plt.show()