import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0)

while True:
    ret,frame = vid.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    faces = faceCascade.detectMultiScale(grey)
    for (x,y,w,h,) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,5,10),3)
    
    cv2.imshow("frame",frame)
    if cv2.waitKey(25)==32:
        break

vid.release()
cv2.destroyAllWindows()    




