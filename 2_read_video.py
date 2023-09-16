#importing a video and opening the front camera
import cv2
cap = cv2.VideoCapture("c:/opencv/test_folder/car.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()