import cv2
from matplotlib import pyplot as plt

img = cv2.imread('ativ.bmp')
height, width = img.shape[:2]
img_128_a = cv2.resize(img, (128, 128), interpolation=cv2.INTER_CUBIC)
img_128_blur_a = cv2.blur(img_128_a, (5, 5))
img_256_blur_b = cv2.blur(img, (5, 5))
img_128_b = cv2.resize(img_256_blur_b, (128, 128), interpolation=cv2.INTER_CUBIC)



'''
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(231), plt.imshow(img), plt.title('a) 256x256')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(img_128_a), plt.title('a) 128x128')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(img_128_blur_a), plt.title('a) img_128_blur')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(img), plt.title('b) 256x256')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(img_256_blur_b), plt.title('b) 256x256_blur')
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(img_128_b), plt.title('b) 128x128_blur')
plt.xticks([]), plt.yticks([])
plt.show()
'''


'''
a informacao ainda esta la 
depois que vc corta 



cv2.imshow('imagem original', img)
cv2.imshow('imagem alterada', img_128_a)
cv2.imshow('imagem alterada', img_128_blur_a)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''