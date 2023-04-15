import cv2
import time
import numpy as np
import numpy as geek


oeil_cascade=cv2.CascadeClassifier("/home/pi/Downloads/haarcascade_eye.xml")
face_cascade=cv2.CascadeClassifier("/home/pi/Downloads/haarcascade_frontalface_alt2.xml")
cam=cv2.VideoCapture(0)#Entree video de la webcam
debut = 0
debut = int(debut)
clignement = 0
debut_clignot = 0
fin_clignot = 0
clignot = 0

while True:
    ret, frame=cam.read()#renvoit val de retour et l'image (dans frame)
    frame = cv2.flip(frame, 1)#met l'image du bon sens
    tickmark=cv2.getTickCount()#prend une mesure de temps
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#on transforme l'image "frame" en noir et blanc
    oeil=oeil_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=4, minSize=(30, 30))#renvoit coordonnées des 4pts du carre
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)#renvoit coordonnées des 4pts du carre
    for a, b, c, d in face:
        cv2.rectangle(frame, (a, b), (a+c, b+d), (255, 255, 0), 2)
        #coordonnées de départ (x,y), coordonnées d'arrivée (x+w, y+h), couleur, epaisseur trait
        #print("detection du visage en cours")
        for x, y, w, h in oeil:#coordonnées x, y, largeur, hauteur 
            if len(oeil) >= 1 and len(oeil) <= 2:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)#dessine rectangle avec image donnée (frame),
                #print("je suis là 1", debut, len(oeil), len(face))
                print("number of eyes :", len(oeil))
                print("number of face :", len(face))
        
                if fin_clignot != 0:
                    debut_clignot = time.time()
                if clignot == 1:
                    clignement +=1
                    clignot = 0
                
                if cv2.waitKey(1)&0xFF== 32 and debut == 0:   #When space bar pressed, the programme launch
                    print("GO")
                    debut = 1

            elif len(oeil) > 3 and debut == 1:
                print("More than two eyes on the screen")
                #oeil_ouvert = 2
                #continue  
        if len(oeil) < 1 and debut == 1:#for détection visage
            clignot = 1
            fin_clignot = time.time()
            temps_clignot = fin_clignot-debut_clignot
            if temps_clignot > 1:
                cv2.putText(frame, "OPEN YOUR EYES", (50, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255),5)
            
    
    
    if cv2.waitKey(1)&0xFF== 27:#si j'appuie sur echap on quitte le programme
        break
    
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)#calcul nbre image par sec (freq / temps)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
    #affichage d'images par sec, image, "text format flottant", coordonnées affichage text, font, taille texte
    #couleur, epaisseur trait
    cv2.putText(frame, "Number of eyes: {0}".format(len(oeil)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255),2)
    cv2.putText(frame, "Number of blink: {0}".format(clignement), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255),2)
    cv2.putText(frame, "Blink duration: {:05.2f}".format(fin_clignot - debut_clignot), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255),2)
    cv2.imshow('Eye detection', frame)#affiche la video de la camera(titre fenetre, var appliquée à cette fenetre)
    #cv2.imshow('Noir et blanc', gray)#affiche la video en noir et blanc
    
cam.release()#libère les ressources
cv2.destroyAllWindows()