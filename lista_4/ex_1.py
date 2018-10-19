from matplotlib import pyplot as plt
import matplotlib
import cv2

img = cv2.imread('open_cv.png',0)
blur = cv2.blur(img, (5, 5))
GaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)
medianBlur = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)


plt.subplot(321), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322), plt.imshow(blur), plt.title('blur')
plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(GaussianBlur), plt.title('GaussianBlur')
plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(medianBlur), plt.title('medianBlur')
plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(bilateralFilter), plt.title('bilateralFilter')
plt.xticks([]), plt.yticks([])
plt.show()

