import cv2
import numpy as np
from matplotlib import pyplot as plt

# simple average filter without scale parameter
mean_filter = np.ones((3, 3))
# create a Gaussian filter
x = cv2.getGaussianKernel(8, 2)
gaussian = x * xT
# D if different edge detection filters
# scharr in the X direction
scharr = np.array([[- 3, 0, 3],
                   [- 10, 0, 10],
                   [- 3, 0, 3]])
# sobel in the X direction
sobel_x = np.array([[- 1, 0, 1],
                    [- 2, 0, 2],
                    [- 1, 0, 1]])
# sobel in the Y direction
sobel_y = np.array([[- 1, - 2, - 1],
                    [0, 0, 0],
                    [1, 2, 1]])
# laplaciano
laplacian = np.array([[0, 1, 0],
                      [1, - 4, 1],
                      [0, 1, 0]])
filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
filter_name = ['filter_media', 'gaussiano', 'laplaciano', 'sobel_x', \
               'sobel_y', 'scharr_x']
fft_filters = [np.fft.fft2(x, [200, 200]) for x in filters]
fft_sh if t = [np.fft.fftshift(y) for and in fft_filters]
mag_spectrum = [np.log(np, abs(z) + 1) for z in fft_sh if t]
#
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(mag_spectrum[i], cmap='gray')
    plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])
plt.show()
