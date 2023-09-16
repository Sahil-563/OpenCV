import cv2
cap = cv2.VideoCapture(0)
width = 300
height = 350
dim = (width,height)
while True:
    success, img = cap.read()
    cannyimg = cv2.Canny(img,50,50)
    #resized_img=cv2.resize(cannyimg,dim,interpolation=cv2.INTER_AREA) 
    cv2.imshow("Video",cannyimg)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()