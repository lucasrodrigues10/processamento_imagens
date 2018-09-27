import cv2
import numpy as np

img_quad = cv2.imread('quad.bmp', cv2.IMREAD_GRAYSCALE)
img_quad = img_quad.astype(float)

# PASSA ALTA
img_a = cv2.filter2D(img_quad, -1, np.matrix([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]))

# NORMALIZA
img_b_normal = cv2.normalize(img_a, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# MEDIA
img_b = cv2.filter2D(img_b_normal, -1, np.matrix([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]))

# SOBER
img_c_vert = cv2.filter2D(img_quad, -1, np.matrix([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]))
img_c_hor = cv2.filter2D(img_c_vert, -1, np.matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]))

# cv2.imshow('IMAGEM ORIGINAL: ', img_quad)
# cv2.imshow('IMAGEM A: ', img_a)
cv2.imshow('IMAGEM B: ', img_b_normal)
# cv2.imshow('IMAGEM C VERTICAL: ', img_c_vert)
cv2.imshow('IMAGEM C HORIZONTAL: ', img_c_hor)

cv2.waitKey(0)
cv2.destroyAllWindows()
