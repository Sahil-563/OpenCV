import cv2
img = cv2.imread("c:/opencv/test_folder/dog.jpg")
print(img.shape)
width = 300
height = 400
dim= (width,height)
croped_img = img[0:200,200:300]
print(croped_img.shape)
resized_image = cv2.resize(img,dim)
print(resized_image.shape)
cv2.imshow("dog",img)
cv2.imshow("resized_image",resized_image)
cv2.imshow("croped_image",croped_img)
cv2.waitKey(0)