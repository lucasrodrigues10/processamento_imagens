import numpy as np
import cv2
from matplotlib import pyplot as plt

# le
img = cv2.imread('messi.jpg', 0)

# transf
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
mag = 20 * np.log(np.abs(fshift))

# filtro
laplacian = np.array([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])
laplacian = np.fft.fft2(laplacian)
laplacian = np.fft.fftshift(laplacian)
laplacian = np.log(np.abs(laplacian) + 1)
mag = mag

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
