import cv2
from matplotlib import pyplot as plt
import numpy as np

# le
img = cv2.imread('quad.bmp', 0)

# v sobel_y
sobel_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])
sobel_y = np.append(sobel_y, np.zeros((253, 3)), axis=0)
sobel_y = np.concatenate([sobel_y, np.zeros((256, 253))], axis=1)

# sobel_x
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
sobel_x = np.append(sobel_x, np.zeros((253, 3)), axis=0)
sobel_x = np.concatenate([sobel_x, np.zeros((256, 253))], axis=1)

# transformada
sobel_x = np.fft.fft2(sobel_x)
#fshift = np.fft.fftshift(sobel_x)
# sobel_x = 20 * np.log(np.abs(fshift))
sobel_y = np.fft.fft2(sobel_y)
#fshift = np.fft.fftshift(sobel_y)
# sobel_y = 20 * np.log(np.abs(fshift))
img = np.fft.fft2(img)
fshift = np.fft.fftshift(img)
img = 20 * np.log(np.abs(fshift))

# filtro composto
filtro_comp = sobel_x * sobel_y
fshift = np.fft.fftshift(filtro_comp)
filtro_comp = 20 * np.log(np.abs(fshift))

img *= filtro_comp

cv2.imshow('Filtro Composto', filtro_comp)
cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
