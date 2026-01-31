import numpy as np
import cv2
import serial

# Libraries
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Arduino data
arduinoDaten = serial.Serial('COM3', 9600)
# From screen
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(len(faces))
    if len(faces) > 1:
        befehl = 'e1'
    else:
        befehl = 'a1'
    befehl = befehl + '\r'
    arduinoDaten.write(befehl.encode())
    # Detecting faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('From Kamera', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
