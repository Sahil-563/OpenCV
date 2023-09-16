#deteciton of shapes and counters:--
import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getcontours(image):
    contours,hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area>200:
            cv2.drawContours(imgContours,cnt,-1,(255,0,0),2)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcnr = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objcnr == 3:
                objecttype = "Tri"
            else:
                objecttype = None
            cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContours,objecttype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)


img = cv2.imread("c:/opencv/test_folder/shapes_2.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgContours = img.copy()
blur_img = cv2.GaussianBlur(gray_img,(3,3),0)
canny_img = cv2.Canny(blur_img,100,100)
blank_img = np.zeros_like(img)
getcontours(canny_img)

img_stack = stackImages(1,([img,gray_img,blur_img],[canny_img,imgContours,blank_img]))


# cv2.imshow("orignal_img",img)
# cv2.imshow("gray_image",gray_img)
# cv2.imshow("blur_img",blur_img)
# cv2.imshow("canny",canny_img)
cv2.imshow("stack",img_stack)
cv2.waitKey(0)