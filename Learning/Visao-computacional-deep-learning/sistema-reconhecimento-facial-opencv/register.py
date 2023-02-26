# -*- coding: utf-8 -*-
# Código para a captura dos regitros do usuário

# Importando as bibliotecas necessárias
import cv2
#import subprocess
import os

# Solicita o nome e matricula do usuário.
nome = input('Entre com seu nome: ')
matricula = input('Entre com sua matricula: ') 

# Armazena o nome e matricula no arquivo de labelmap.
file = open("labelmap.csv", "a")
file.write(matricula+','+nome+"\n") 
file.close()

# Carrega o Detector de Face.
detector= cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')

# Captura o video da camera
# Loop para verificar qual câmera está ativa
for i in range(10):
    cam = cv2.VideoCapture(i)
    if cam.isOpened():
        print(f"Camera index {i} is working")
        break
#cap = VideoCapture(0)

# Inicializa o contador de imagens
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break
    
    k = cv2.waitKey(1)
    
    # Realiza a detecção de face em cada frame.
    faces = detector.detectMultiScale(frame, 1.3, 5)
    
    # Desenha o retângulo na face detectada utilizando as coordenadas.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Exibe a imagem.
    cv2.imshow("Coletor de Imagens - Pressione ENTER para gravar", frame)
    cv2.setWindowProperty("Coletor de Imagens - Pressione ENTER para gravar", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow("Coletor de Imagens - Pressione ENTER para gravar", 0, 0)

    #if k%256 == 27:
    if k == 27 or k == ord('q'):
        # Se pressionar o ESC
        print("saindo...")
        #cam.release()
        #cv2.destroyAllWindows()
        break
    elif k%256 == 13: # Se pressionar o ENTER
        # Converte a imagem para escala de cinza.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Persiste a imagem em disco utilizando o numero de matricula e o contador.
        cv2.imwrite("dataset/user"+'-'+str(matricula)+'-'+str(img_counter)+".jpg", gray[y:y+h,x:x+w])

        print("Imagem gravada!")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
#subprocess.call([r"C:\Users\marcf\anaconda3\envs\rstudio\python.exe", r"C:\Users\marcf\OneDrive\Documentos\Ciencia-de-dados\Visao-computacional-deep-learning\sistema-reconhecimento-facial-opencv\menu.py"])
os.system('start cmd /k "python C:\\Users\\marcf\\OneDrive\\Documentos\\Ciencia-de-dados\\Visao-computacional-deep-learning\\sistema-reconhecimento-facial-opencv\\menu.py"')