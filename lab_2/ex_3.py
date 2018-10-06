import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('sunset3.bmp',0)
f = np.fft.fft2(img)
f[8][18] = 0
f[248][238] = 0
fshift = np.fft.fftshift(f)
magnitude_spectrum = (20 * np.log(np.abs(fshift)))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


fi = np.float32(np.fft.ifft2(f))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(fi, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()