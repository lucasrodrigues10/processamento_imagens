import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', 0)
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# OR
'''
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

plt.subplot(2, 1, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 1, 2), plt.imshow(res, cmap='gray')
plt.title('Imagem Grandona'), plt.xticks([]), plt.yticks([])
plt.show()
'''
cv2.imshow('imagem original', img)
cv2.imshow('imagem alterada', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
