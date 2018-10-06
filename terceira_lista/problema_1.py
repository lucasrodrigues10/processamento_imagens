import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
c = 30
mag = 20 * np.log(np.abs(fshift))
mag = np.log(1 + mag)

# filtro
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
num = 30
fshift[crow-num:crow+num, ccol-num:ccol+num] = 0

# anti transformada
f_ishift = np.fft.ifftshift(fshift)
img_back = np.abs(np.fft.ifft2(f_ishift))

# plota
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.imshow(mag, cmap='gray')
plt.subplot(133)
plt.imshow(img_back)
plt.show()
