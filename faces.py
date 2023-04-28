import cv2

img = cv2.imread("4f.jpg")

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(grey)

print(len(faces))

for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,100),2)

cv2.imshow("rec",img)
cv2.waitKey(0)   

