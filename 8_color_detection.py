import cv2
import numpy as np
def empty(a):
    pass

cv2.namedWindow("Trackbars")  #making a window for trackbars
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",175,179,empty)  #making a actual trackbars
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("sat Min","Trackbars",166,255,empty)
cv2.createTrackbar("sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("val Min","Trackbars",0,255,empty)
cv2.createTrackbar("val Max","Trackbars",255,255,empty)

while True:
    img =cv2.imread("c:/opencv/test_folder/rose.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #converting bgr image to hsv
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")  #getting the value of hue from our original image
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("val Min","Trackbars")
    v_max = cv2.getTrackbarPos("val Max","Trackbars")
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    higher = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,higher)
    imgResult = cv2.bitwise_and(img,img,mask = mask)
    cv2.imshow("mask", mask)
    cv2.imshow("result",imgResult)
    cv2.imshow("rose", imgHSV)
    cv2.waitKey(1)

