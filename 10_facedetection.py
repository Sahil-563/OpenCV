import cv2
face_cascade = cv2.CascadeClassifier("c:/opencv/haarcascade_frontalface_default.xml")
img = cv2.imread("c:/opencv/test_folder/face.jpg")
img_gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Faces = face_cascade.detectMultiScale(img_gray,1.1,4)
for(x,y,w,h) in Faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("image",img)
cv2.waitKey(0)