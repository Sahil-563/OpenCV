import cv2
import numpy as np
img = np.zeros((500,500,3))
text = cv2.putText(img,"Hello world",(200,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),4)
cv2.imshow("texted_img",img)
cv2.waitKey(0)