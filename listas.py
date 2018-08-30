# -*- coding: utf-8 -*-

import colorsys as cs
import math
import time

import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def converte_para_cinza(img):
    img_em_cinza = rgb2gray(img)
    return img_em_cinza


def mostra_imagem(img):
    ndim = len(img.shape)
    if ndim == 2:
        plt.imshow(img, cmap=plt.get_cmap('gray'))
        plt.show()
    else:
        plt.imshow(img, cmap=plt.get_cmap('prism'))
        plt.show()


def salva_imagem(img):
    ndim = len(img.shape)
    if ndim == 2:
        plt.imsave('output_cinza.png', img, cmap='img_em_cinza')
    else:
        plt.imsave('output_colorido.png', img)


def rgb_para_hsv(img):
    alt = img.shape[0]
    larg = img.shape[1]
    imagem_hsv = np.zeros((alt, larg, 3))
    for i in range(alt):
        for j in range(larg):
            # Alpha = img[i][j][3]
            Alpha = 1  # Comentar essa linha e descomentar a de cima caso a imagem seja RGBA
            R = img[i][j][0] * Alpha / 255
            G = img[i][j][1] * Alpha / 255
            B = img[i][j][2] * Alpha / 255
            imagem_hsv[i][j][0], imagem_hsv[i][j][1], imagem_hsv[i][j][2] = cs.rgb_to_hsv(R, G, B)
    return imagem_hsv


def rgb_para_hsi(img):
    alt = img.shape[0]
    larg = img.shape[1]
    imagem_hsi = np.zeros((alt, larg, 3))
    for i in range(alt):
        for j in range(larg):
            # Alpha = img[i][j][3]
            Alpha = 1  # Comentar essa linha e descomentar a de cima caso a imagem seja RGBA
            R = img[i][j][0] * Alpha / 255
            G = img[i][j][1] * Alpha / 255
            B = img[i][j][2] * Alpha / 255
            H = cs.rgb_to_hsv(R, G, B)[0]  # calculo da matiz

            # calculo da intensidade
            # I = (R+G+B)/255

            I = (R + G + B) / 3
            # calculo da saturacao
            Cmin = min(R, G, B)

            if (I == 0):
                S = 0
            else:
                S = 1 - Cmin / I

            imagem_hsi[i][j][0] = H
            imagem_hsi[i][j][1] = S
            imagem_hsi[i][j][2] = I
    return imagem_hsi


def hsi_para_rgb(img):
    pi = math.pi
    alt = img.shape[0]
    larg = img.shape[1]
    imagem_rgb = np.zeros((alt, larg, 3))
    for i in range(alt):
        for j in range(larg):
            H = img[i][j][0] * 2 * pi
            S = img[i][j][1]
            I = img[i][j][2]
            if (H < 2 * pi / 3 and H >= 0):
                R = (1 + S * math.cos(H) / math.cos(pi / 3 - H)) / 3
                B = (1 - S) / 3
                G = 1 - R - B
            elif (H >= 2 * pi / 3 and H < 4 * pi / 3):
                H = H - 2 * pi / 3
                R = (1 - S) / 3
                G = (1 + S * math.cos(H) / math.cos(pi / 3 - H)) / 3
                B = 1 - R - G
            elif (H >= 4 * pi / 3 and H < 2 * pi):
                H = H - 4 * pi / 3
                G = (1 - S) / 3
                B = (1 + S * math.cos(H) / math.cos(pi / 3 - H)) / 3
                R = 1 - B - G

            R = 3 * I * R
            G = 3 * I * G
            B = 3 * I * B
            imagem_rgb[i][j][0] = R
            imagem_rgb[i][j][1] = G
            imagem_rgb[i][j][2] = B
    return imagem_rgb


def hsv_para_rgb(img):
    alt = img.shape[0]
    larg = img.shape[1]
    imagem_rgb = np.zeros((alt, larg, 3))
    for i in range(alt):
        for j in range(larg):
            H = img[i][j][0]
            S = img[i][j][1]
            V = img[i][j][2]
            imagem_rgb[i][j][0], imagem_rgb[i][j][1], imagem_rgb[i][j][2] = cs.hsv_to_rgb(H, S, V)
    return imagem_rgb


def histograma_cinza(img):
    n, bins, path = plt.hist(img.ravel(), 256, [0, 256])
    plt.xlabel('Abscissa')
    plt.ylabel('Ordenada')
    plt.title('Histograma')
    plt.grid(True)
    # plt.show()
    return n


def histograma_cinza_acumulado(img):
    n, bins, path = plt.hist(img.ravel(), 256, [0, 256], cumulative=True)
    plt.xlabel('Abscissa')
    plt.ylabel('Ordenada')
    plt.title('Histograma')
    plt.grid(True)
    # plt.show()
    return n


def aplica_funcao_trans(img_cinza):
    img = img_cinza.copy()
    funcao_trans = np.arange(255, -1, -1)  # cria um arrayq ue começa em 255 e termina em
    print(funcao_trans)
    alt = img.shape[0]
    larg = img.shape[1]
    for i in range(alt):
        for j in range(larg):
            tom_de_cinza = int(round(img[i][j]))
            img[i][j] = funcao_trans[tom_de_cinza]
    img2 = img
    return img2


def aplica_filtro(img_cinza):
    img = img_cinza.copy()
    alt = img.shape[0]
    larg = img.shape[1]
    for i in range(alt):
        for j in range(larg):
            try:
                img[i][j] = (img[i - 1][j - 1] + img[i][j - 1] + img[i + 1][j - 1] + img[i - 1][j] + img[i][j] + img[i + 1][j] + img[i - 1][j + 1] + img[i][j + 1] + img[i + 1][j + 1]) / 9
            except:
                pass
    return img


inicial = time.time()

# OBS: FICAR ATENTO CASO A IMAGEM FORCEÇA RGB DE O A 255 OU DE 0 A 1
img = mpimg.imread('duck.jpeg')  # lê imagem
img = img.astype(float)  # convertendo tipo doa array

img_em_cinza = converte_para_cinza(img)  # converte para cinza
# imagem_hsv = rgb_para_hsv(img)

# faz o histograma em cinza, guardando valores em vetor_cinza
vetor_cinza = histograma_cinza(img_em_cinza)

# print(vetor_cinza) #-> Mostra valores do vetor
# print(vetor_cinza.shape[0]) -> Mostra tamanho do vetor (256)

# faz o histograma acumulado, guardando valores em vetor_acumulado
vetor_acumulado = histograma_cinza_acumulado(img_em_cinza)

# print(vetor_acumulado) -> mostra valores do vetor acumulado
# print(vetor_acumulado.shape[0]) -> mostra tamanho do vetor acumulado(256)


final = time.time()  # guarda momento que programa terminou
print(final - inicial)  # calcula tempo decorrido
'''
imagem_hsi = rgb_para_hsi(img)
imagem_hsv = rgb_para_hsv(img)


print ("Em RGB ",img[10][10])
print ("Em HSV ",imagem_hsv[10][10])
print ("Em HSI ",imagem_hsi[10][10]) 
print (" Retornando para RGB -----")

imagem_rgb = hsv_para_rgb(imagem_hsv)
print("De HSV para RGB", imagem_rgb[10][10])
imagem_rgb = hsi_para_rgb(imagem_hsi)
print("De HSI para RGB", imagem_rgb[10][10])
'''
img_invertida = aplica_funcao_trans(img_em_cinza)
print('NOVO: ', img_invertida[100][100])
print('ANTIGO: ', int(round(img_em_cinza[100][100])))

img_com_filtro = aplica_filtro(img_em_cinza)
mostra_imagem(img)
mostra_imagem(img_em_cinza)
mostra_imagem(img_com_filtro)
mostra_imagem(img_invertida)
