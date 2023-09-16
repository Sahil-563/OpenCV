import cv2
import numpy as np
img  = np.zeros((500,500,3))
cv2.imshow("Blank image", img)
#adding colors to the image red,blue or green
img[:]=250,0,0
cv2.imshow("blue image",img)
#adding colors to the specific region of image red,blue or green
img[0:200,0:200]=0,250,0
cv2.imshow("green image",img)
cv2.waitKey(0)