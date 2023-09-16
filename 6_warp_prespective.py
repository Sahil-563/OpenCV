import cv2
import numpy as np
img = cv2.imread("c:/opencv/test_folder/card1.jpeg")

width,height  = 250,350

pts1 = np.float32([[353,60],[669,61],[380,481],[643,480]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("output",imgOutput)

cv2.imshow("img",img)
cv2.waitKey(0)