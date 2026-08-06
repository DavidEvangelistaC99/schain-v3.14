import os
import h5py
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
from matplotlib.patches import Circle
from matplotlib.colors import ListedColormap, BoundaryNorm

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.feature import ShapelyFeature

# ==========================================================
# Logo
# ==========================================================

LOGO = "/home/david/Documents/schain-v3.14/scripts/LogoIGP.png"
LOGO_SIZE = 0.12
LOGO_MARGIN = 0.02

# ==========================================================
# Fuente Times New Roman
# ==========================================================

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.serif'] = ['Times New Roman']
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.size'] = 15

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

RADAR_LAT = -12.04042
RADAR_LON = -75.29591

XRANGE = 60  # km
h0 = 37 # Para SNR índice para chirp 145, para cc 38

SHOW_H0_CIRCLE = True 

PATH = "/home/david/Documents/schain-v3.14/scripts/DATA/SOPHY_20260302_005800_E4.2_W.hdf5"
# PATH = "/home/david/Documents/DATA/CHIRP@2025-10-07T19-57-06/param-01_AUG/SNR_PPI_EL_1.0/SOPHY_20251007_200049_E1.0_SNR.hdf5"

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

    #mask = -2.75

    H = f["Data/spectral_width/H"][:]

    az = f["Metadata/azimuth"][:]
    ele = f["Metadata/elevation"][:]
    r = f["Metadata/range"][:]

    # Eliminar todo lo que esté antes de ese radio
    H[:, :h0] = np.nan

    # Aumentar 5 dB solamente donde no hay NaN
    # H[~np.isnan(H)] += 4.7

# Radio correspondiente al índice h0
if 0 <= h0 < len(r):
    h0_radius = r[h0]
else:
    raise ValueError(f"h0={h0} está fuera del rango [0,{len(r)-1}]")

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
fig.patch.set_facecolor("#EEEEEE")


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
# CÍRCULO EN h0
# ==========================================================

if SHOW_H0_CIRCLE:

    c = Circle(
        (RADAR_LON, RADAR_LAT),
        km2deg(h0_radius),
        fill=False,
        edgecolor="black",
        linewidth=1.2,
        linestyle="--",      # línea punteada
        transform=ccrs.PlateCarree(),
        zorder=20
    )

    #ax.add_patch(c)


# ==========================================================
# RADAR
# ==========================================================


ax.plot(
    -75.29591, 
    -12.04042,
    # RADAR_LON,
    # RADAR_LAT,
    marker="*",
    markersize=5,
    color="red",
    transform=ccrs.PlateCarree()
)


# ==========================================================
# ESCALA DE REFLECTIVIDAD (dBZ)
# ==========================================================

levels = np.arange(0, 25, 1.0)

colors = [
    "#00ffff", "#00aaf2", "#0055e5", "#0000d8", 
    "#007f00", "#00aa00", "#00d400", "#00ff00",
    "#ffff00", "#ffd400", "#ffaa00", "#ff7f00",
    "#ff0000", "#d40000", "#aa0000", "#7f0000",
    "#ff00ff", "#d400d4", "#aa00aa", "#7f007f",
    "#9938ff", "#832ed8", "#6e25b2", "#591c8c",
]

'''colors = [
    "#2b2b2b",  # -20
    "#3d4950",  # -15
    "#536d7a",  # -10
    "#7f7f7f",  # -5
    "#b0b0b0",  # 0
    "#40d9d9",  # 5
    "#3aa6ff",  # 10
    "#0000ff",  # 15
    "#82F02D",  # 25
    "#2DF03A",  # 30
    "#008800",  # 35
    "#ffcc00",  # 45
    "#ff9900",  # 50
    "#ff6600",  # 55
    "#ff0000",  # 60
    "#cc0000",  # 65
    "#800000",  # 70
    "#ff00ff",   # 75-80
    "#8036e7",
    "#ffffff"
]'''

cmap = ListedColormap(colors)
norm = BoundaryNorm(levels, cmap.N)

# ==========================================================
# PPI
# ==========================================================

pcm = ax.pcolormesh(
    lon,
    lat,
    H,
    shading="auto",
    cmap=cmap,
    norm=norm,
    transform=ccrs.PlateCarree()
)

cbar = plt.colorbar(
    pcm,
    pad=0.02,
    ticks=np.arange(0, 26, 5)
)

cbar.set_label(
    "Spectral Width (m/s)",
    fontsize=17,
    fontname="Times New Roman"
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

# ==========================================================
# LOGO IGP
# ==========================================================

'''logo = mpimg.imread(LOGO)

pos = ax.get_position()

logo_w = 0.10
logo_h = 0.10

dx = 0.01
dy = -0.065

logo_ax = fig.add_axes([
    pos.x1 - logo_w - dx,
    pos.y1 - logo_h - dy,
    logo_w,
    logo_h
], zorder=100)

logo_ax.imshow(logo)
logo_ax.axis("off")'''

#plt.title(f"PPI SNR  EL={mean_el:.1f}°")

#plt.show()

# ==========================================================
# SALIDA
# ==========================================================

SAVE_FIGURE = True

OUTPUT_FILE = "PPI_W.png"

DPI = 600     # 300 para artículos, 600 para alta resolución

# ==========================================================
# GUARDAR FIGURA
# ==========================================================

if SAVE_FIGURE:
    fig.savefig(
        OUTPUT_FILE,
        dpi=DPI,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
        edgecolor="none"
    )
    print(f"Figura guardada en:\n{OUTPUT_FILE}")

plt.show()