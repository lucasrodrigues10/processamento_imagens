import cv2
import numpy as np
from matplotlib import pyplot as plt

# LE A IMAGEM
img_fusca = cv2.imread('fusca.bmp', cv2.IMREAD_GRAYSCALE)

# HISTOGRAMA DA IMAGEM ORIGINAL
histr = cv2.calcHist([img_fusca], [0], None, [256], [0, 256])
plt.plot(histr)
plt.xlim([0, 256])

# FAZ A FUNCAO DE TRANSFERENCIA
v = []
for x in range(0, 1000):
    v.append(int(45.98 * np.log(x + 1)))

for x in range(0, len(img_fusca)):
    for y in range(0, len(img_fusca[x])):
        img_fusca[x][y] = v[img_fusca[x][y]]

# HISTOGRAMA DA IMAGEM MODIFICADA
histr = cv2.calcHist([img_fusca], [0], None, [256], [0, 256])
plt.plot(histr)
plt.xlim([0, 256])

# PLOTA O HISTOGRAMA
plt.xlabel('Intensidade da Iluminacao')
plt.ylabel('Quantidade de Pixels')
plt.title('Histogramas')
plt.show()

# MOSTRA A IMAGEM
cv2.imshow('IMAGEM DO FUSCA: ', img_fusca)
cv2.waitKey(0)
cv2.destroyAllWindows()
