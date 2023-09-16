import cv2
import numpy as np

#code for trackbars:--
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",400,300)
def empty(a):
    pass

cv2.createTrackbar("hueMin","Trackbars",13,30,empty)
cv2.createTrackbar("hueMax","Trackbars",30,30,empty)
cv2.createTrackbar("satMin","Trackbars",85,255,empty)
cv2.createTrackbar("satMax","Trackbars",255,255,empty)
cv2.createTrackbar("valMin","Trackbars",34,255,empty)
cv2.createTrackbar("valMax","Trackbars",255,255,empty)

while(True):
    path = cv2.imread("c:/opencv/test_folder/Ferrari.png")
    img_hsv = cv2.cvtColor(path,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hueMin","Trackbars")  #getting the value of hue from our original image
    h_max = cv2.getTrackbarPos("hueMax","Trackbars")
    s_min = cv2.getTrackbarPos("satMin","Trackbars")
    s_max = cv2.getTrackbarPos("satMax","Trackbars")
    v_min = cv2.getTrackbarPos("valMin","Trackbars")
    v_max = cv2.getTrackbarPos("valMax","Trackbars")
    #print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    heigher = np.array([h_max,s_max,v_max])
    mask  = cv2.inRange(img_hsv,lower,heigher)

    img_result = cv2.bitwise_and(path,path,mask= mask)
    #cv2.imshow("mask",mask)
    #cv2.imshow("Ferrari",img_hsv)
    cv2.imshow("output",img_result)
    cv2.imshow("real",path)

    cv2.waitKey(1)