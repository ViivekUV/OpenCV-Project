from cv2 import cv2  
 
faceCascade= cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('images/face2.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
faces = faceCascade.detectMultiScale(img,2.5,4)
 
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
 
cv2.imshow("Result", img)
cv2.waitKey(0)
