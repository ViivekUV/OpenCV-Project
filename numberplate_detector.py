from cv2 import cv2
import numpy as np

minArea = 500 
color = (0,255,0)
imgName = "car1.jpg"
numberPlateCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")
img = cv2.imread("images/"+imgName)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

licensePlates = numberPlateCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in licensePlates:
    area = w * h
    if area > minArea:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgROI = img[y:y+h,x:x+w]

cv2.imshow("Result", img)
cv2.imshow("NumberPlate",imgROI)
if cv2.waitKey(1) & 0xFF == ord('s'):
    cv2.imwrite("Scanned/"+imgName,imgROI)
    cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
    cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
    
    
cv2.waitKey(0)