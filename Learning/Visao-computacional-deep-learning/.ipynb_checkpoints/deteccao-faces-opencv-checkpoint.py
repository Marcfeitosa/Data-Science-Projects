# Data Science do Zero - Capítulo 10 Visão Computacional e Deep Learning

#Instalacao do OpenCV com Python.
#pip install opencv-python

#importando a biblioteca
import cv2

# verificando a versao do OpenCV
print("OpenCV: {}".format(cv2.__version__))

# Importando os métodos necessários
from cv2 import imread
from cv2 import CascadeClassifier

# carregando a imagem de teste
img_array = imread('imagens/woman.jpeg')

# carregando o modelo pre-treinado
classifier = CascadeClassifier('modelos/haarcascade_frontalface_default.xml')

# realizando a detecção da face
#bboxes = classifier.detectMultiScale(img_array)
bboxes = classifier.detectMultiScale(img_array,minNeighbors=8)


# Verificando as bounding box
for box in bboxes:
	print("Face encontrada com as coordenadas: {}".format(box))

#plotando um retangulo na face encontrada

#importando o metodo responsável para desenhar o retangulo 
from cv2 import rectangle
from cv2 import imshow,waitKey,destroyAllWindows


#Loop em cada face detectada para "desenhar" o retangulo de acordo com suas coordenadas
for box in bboxes:
	# pegando as coordenadas x e y e altura e largura da caixa
	x, y, width, height = box
	x2, y2 = x + width, y + height
	# desenhando o retangulo na imagem
	rectangle(img_array, (x, y), (x2, y2), (0,0,255), 3)

# exibindo a imagem
imshow('face detectada', img_array)

waitKey(0)
# fecha a janela da imagem
destroyAllWindows()