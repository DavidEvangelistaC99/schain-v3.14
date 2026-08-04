import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

df = pd.read_excel('sensitivity-data.xlsx')
df = df.fillna(0)

# Agregar la columna Angle como primera columna
df.insert(0, 'Angle', np.arange(len(df)))

# Guardar como CSV
df.to_csv("sensitivity-data.csv", index=False)

x = np.arange(len(df))

cc = df['CC'].to_numpy()
chirp = df['CHIRP'].to_numpy()

plt.figure(figsize=(10,4))

plt.plot(x, cc, color='blue', linewidth=0.5,
         label='Complementary codes')
plt.plot(x, chirp, color='red', linewidth=0.5,
         label='Chirp')

plt.fill_between(x, cc, 0, color='blue', alpha=0.3)
plt.fill_between(x, chirp, 0, color='red', alpha=0.3)

plt.xlabel('Angle (°)')
plt.ylabel('SNR (dB)')

plt.xlim(0,359)
plt.ylim(0,40)

plt.xticks([0,89,179,269,359], ['0','90','180','270','360'])

plt.legend()
plt.style.use(['science'])
plt.show()