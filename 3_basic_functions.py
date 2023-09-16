import cv2
import numpy as np
img = cv2.imread("c:/opencv/test_folder/girl.jpg")

kernal = np.ones((5,5),np.uint8) #defining the kernal value for image dialation for the border of the images


#Different functions on images
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Changing original image to a gray scale image
blurImg = cv2.GaussianBlur(img,(11,11),0)  #Changing original image to a blured image
cannyImg = cv2.Canny(img,100,100)     #Changing the original image to canny image
imgdialation = cv2.dilate(cannyImg,kernal,iterations =1) #Changing the thickness of canny image 
imgEroded = cv2.erode(cannyImg,kernal,iterations= 1)   #Changing the thinness of canny image 

#changiing the width height of each image
width = 300
height  = 350
dim=(width,height)

resized_img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)  #resizing the dimensions of the image
resized_grayimg=cv2.resize(grayImg,dim,interpolation=cv2.INTER_AREA)
resized_blurimg=cv2.resize(blurImg,dim,interpolation=cv2.INTER_AREA) 
resized_cannyimg=cv2.resize(cannyImg,dim,interpolation=cv2.INTER_AREA) 
resized_dialatedimg=cv2.resize(imgdialation,dim,interpolation=cv2.INTER_AREA) 
resized_errodedimg=cv2.resize(imgEroded,dim,interpolation=cv2.INTER_AREA) 

cv2.imshow("resizedimage",resized_img)
cv2.imshow("grayimage",resized_grayimg)
cv2.imshow("blurimage",resized_blurimg)
cv2.imshow("cannyimage",resized_cannyimg)
cv2.imshow("dialationiimage",resized_dialatedimg)
cv2.imshow("Erodedimage",resized_errodedimg)

cv2.waitKey(0)