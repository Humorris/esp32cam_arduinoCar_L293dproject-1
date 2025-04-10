import cv2
import numpy as np

cap = cv2.VideoCapture('http://admin:admin@192.168.92.111:8081/video')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame' ,frame)

    if cv2.waitKey(1) &0xFF ==ord('q'):
        break

cap.realease()
cv2.destroyAllWindows()