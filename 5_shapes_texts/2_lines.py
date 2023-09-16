#Adding lines to the blank image
import cv2
import numpy as np

img = np.zeros((500,500,3))
lined_img=cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,250),3)
cv2.imshow("lineOnImage",lined_img)
cv2.waitKey(0)