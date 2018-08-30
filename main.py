import cv2
import numpy as np
from matplotlib import pyplot as plt

img_limiar = cv2.imread('limiar.png')
limiar, img_limiar = cv2.threshold(img_limiar, 160, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('LIMIAR', img_limiar)

img_soccer = cv2.imread('soccer.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img_soccer], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.hist(img_soccer.ravel())
plt.show()

'''
print(img_soccer.shape)
print(img_soccer.item(0, 0, 1))
img_soccer.itemset((0, 0, 2), 255)
img_soccer.itemset((0, 0, 1), 0)
img_soccer.itemset((0, 0, 0), 0)
'''

# y=150 x=250
# y=250 x=330

bola = img_soccer[180:250, 250:320]
img_soccer[80:80 + (250 - 180), 400:400 + (320 - 250)] = bola
'''
    0 - Blue
    1 - Green
    2 - Vermelho
'''

cv2.imwrite('soccer-2.png', img_soccer)

#cv2.imshow('Soccer', img_soccer)
cv2.waitKey(0)
cv2.destroyAllWindows()
