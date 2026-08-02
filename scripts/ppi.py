import h5py
import numpy as np
import matplotlib.pyplot as plt

# Abrir archivo

# path = "/home/david/Documents/DATA/CHIRP@2025-10-07T19-57-06/param-01_AUG/SNR_PPI_EL_1.0/SOPHY_20251007_200049_E1.0_SNR.hdf5"
path = "/home/david/Documents/DATA/HYO@2025-11-11T00-00-34/param-01_AUG/SNR_PPI_EL_1.0/SOPHY_20251031_000826_E1.0_SNR.hdf5"

with h5py.File(path, "r") as f:

    # Datos
    H = f["Data/snr/H"][:]              # (371,1000)
    az = f["Metadata/azimuth"][:]       # grados
    r = f["Metadata/range"][:]          # metros
    # Convertir a dB
    H = 10*np.log10(H)

# Convertir azimut a radianes
theta = np.deg2rad(az)

# Crear malla polar
R, TH = np.meshgrid(r, theta)

# Convertir a coordenadas cartesianas
X = R * np.sin(TH)
Y = R * np.cos(TH)

# Graficar
plt.figure(figsize=(8,8))

pcm = plt.pcolormesh(
    X,
    Y,
    H,
    shading="auto",
    cmap="jet",
    vmin=-10,   # valor mínimo
    vmax=40     # valor máximo
)

plt.colorbar(pcm, label="SNR Horizontal (dB)")
plt.xlabel("Este-Oeste (m)")
plt.ylabel("Norte-Sur (m)")
plt.title("PPI SNR Horizontal")
plt.axis("equal")
plt.tight_layout()
plt.show()

print(np.nanmin(H))
print(np.nanmax(H))
print(np.nanmean(H))