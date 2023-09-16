#Adding rectangles to the blank image
import cv2
import numpy as np

img = np.zeros((500,500,3)) #Creating a blank image

rectangle_img=cv2.rectangle(img,(0,50),(333,333),(0,0,250))
cv2.imshow("rectangleOnImage",rectangle_img)

circle_img=cv2.circle(img,(50,50),30,(0,250,250))
cv2.imshow("CircleOnImage",circle_img)
cv2.waitKey(0)