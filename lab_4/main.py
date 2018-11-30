import cv2
from matplotlib import pyplot as plt

# le a imagem
img = cv2.imread('img.jpg')
img_oculos = cv2.imread('img_oculos.jpg')

# cria os classificadores
classificador_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classificador_olhos = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#variavel auxiliar
i = 1
imagens = [img, img_oculos]
imagens_descricao = ['Foto', 'Foto com óculos']
for (img, img_descricao) in zip(imagens, imagens_descricao):
    # converte imagem para cinza
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecta a face
    faces = classificador_face.detectMultiScale(img_cinza, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        regiao_interesse_cinza = img_cinza[y:y + h, x:x + w]
        regiao_interesse_colorido = img[y:y + h, x:x + w]
        olhos = classificador_olhos.detectMultiScale(regiao_interesse_cinza)
        for (ex, ey, ew, eh) in olhos:
            cv2.rectangle(regiao_interesse_colorido, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.subplot(2, 1, i), plt.imshow(RGB_img), plt.title(img_descricao), plt.xticks([]), plt.yticks([])
    i += 1
plt.show()
