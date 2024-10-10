import cv2
alg=cv2.CascadeClassifier("C:/Users/balam/Downloads/haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    if img is None:
        break
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=alg.detectMultiScale(grayimg,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(150,150,255),2)
    cv2.imshow('detection',img)
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()

