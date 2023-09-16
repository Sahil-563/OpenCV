from tkinter import Frame
from xml.etree.ElementTree import TreeBuilder
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,Frame =cap.read()
    grayframe = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(grayframe,(7,7),0)
    cv2.imshow("Frame",blur_frame)
    key = cv2.waitKey(1)
    if key ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
