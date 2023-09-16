import cv2
import numpy as np
frame_width = 500
frame_height = 500
cap = cv2.VideoCapture(1)
cap.set(3,frame_width)
cap.set(4,frame_height)
cap.set(10,150)

def empty(a):
    pass

cv2.namedWindow ("HSV")
cv2.resizeWindow("HSV",640, 240),
cv2.createTrackbar("HUE Min", "HSV",0,179, empty)
cv2.createTrackbar("SAT Min", "HSV",0,255, empty)
cv2.createTrackbar("VALUE Min", "HSV",0,255, empty)
cv2.createTrackbar("HUE Max", "HSV",179,179, empty)
cv2.createTrackbar("SAT Max", "HSV",255,255,empty)
cv2.createTrackbar("VALUE Max", "HSV",255,255,empty)
while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE Min","HSV")  #getting the value of hue from our original image
    h_max = cv2.getTrackbarPos("HUE Max","HSV")
    s_min = cv2.getTrackbarPos("SAT Min","HSV")
    s_max = cv2.getTrackbarPos("SAT Max","HSV")
    v_min = cv2.getTrackbarPos("VALUE Min","HSV")
    v_max = cv2.getTrackbarPos("VALUE Max","HSV")
    lower = np.array([h_min,s_min,v_min])
    higher = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,higher)
    imgResult = cv2.bitwise_and(img,img,mask = mask)

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([mask,imgResult])
    # cv2.imshow("hsv_image", imgHsv)
    # cv2.imshow("mask", mask)
    cv2.imshow("result",hstack)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
    