import numpy as np
import cv2
from matplotlib import pyplot as plt

# le
img = cv2.imread('sunset3.bmp', 0)

# transformada
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = 20 * np.log(np.abs(fshift))

# soma os niveis cinzas
soma_cinza = np.sum(img)
print('Soma: ', soma_cinza)
numero_pixels = len(img) * len(img)
print('Numero de Pixel: ', numero_pixels)
divisao = soma_cinza / numero_pixels

# divide
primeiro_valor_fft = f[0, 0] / numero_pixels
print('FFT(0,0)/divisao: ', primeiro_valor_fft)
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.imshow(mag, cmap='gray')
plt.show()
