import numpy as np
import cv2
from matplotlib import pyplot as plt
#le
img = cv2.imread('neymar.jpg', 0)

# transf
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = 20 * np.log(np.abs(fshift))

# filtro
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
num = 100
fshift[crow-num:crow+num, ccol-num:ccol+num] = 1

# anti transformada
f_ishift = np.fft.ifftshift(fshift)
img_back = np.abs(np.fft.ifft2(f_ishift))

plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.imshow(mag, cmap='gray')
plt.subplot(133)
plt.imshow(img_back)
plt.show()
