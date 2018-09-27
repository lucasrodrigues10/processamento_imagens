import cv2

img_cranio = cv2.imread('CRANIO.bmp', cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(img_cranio, cv2.COLORMAP_JET)

cv2.imshow('IMAGEM CRANIO: ', img_cranio)
cv2.imshow('IMAGEM MODIFICADA: ', im_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
