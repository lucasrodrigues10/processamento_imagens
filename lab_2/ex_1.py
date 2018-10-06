import numpy as np
import cv2
from matplotlib import pyplot as plt

# le
img = cv2.imread('sunset3.bmp', 0)
# transformada linha
f = np.fft.fft(img)
fshift = np.fft.fftshift(f)
img_uni = 20 * np.log(np.abs(fshift))
# transpose
img_uni = np.transpose(img_uni)
# transformada colunas
f = np.fft.fft(img_uni)
fshift = np.fft.fftshift(f)
img_uni = 20 * np.log(np.abs(fshift))

# anti transformada
f_ishift = np.fft.ifftshift(fshift)
img_back = np.abs(np.fft.ifft2(f_ishift))


plt.subplot(121)
plt.imshow(img_back, cmap='gray')
plt.subplot(122)
plt.imshow(img, cmap='gray')
plt.show()
