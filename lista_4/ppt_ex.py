import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('codigo_barra.png', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
img_fft = 20 * np.log(np.abs(fshift))

# laplacian
laplacian = np.array([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])

# anti transformada
f_ishift = np.fft.ifftshift(fshift)
img_back = np.abs(np.fft.ifft2(f_ishift))

plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2), plt.imshow(img_fft, cmap='gray')
plt.title('Imagem_FFT'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3), plt.imshow(img_back, cmap='gray')
plt.title('Imagem_iFFT'), plt.xticks([]), plt.yticks([])