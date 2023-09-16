import cv2
import mediapipe as mp
import time

ptime = 0
ctime = 0

mphands=mp.solutions.mediapipe.python.solutions.hands  #there is a class in mp.solution which is hands
hand = mphands.Hands() #creating object of hands class
draw = mp.solutions.mediapipe.python.solutions.drawing_utils #drawing circles around differert landmarks of hand
cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hand.process(imgRGB) #Sending image for processing in hand object

    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            for id,lm in enumerate(i.landmark):
                #print(id,lm) #printing the x and y positions of different landmarks in hands with there id number
                #but these x and y values are the ratio of the image we have to find pixel values
                #so we multiply x value of lm with width and yu value with height

                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                              
            draw.draw_landmarks(img,i,mphands.HAND_CONNECTIONS)#draw_landmarks is a function in draw_utils

    #simple code for FPS
    ctime = time.time()
    fps = 1/(ctime - ptime)
    ptime = ctime
    cv2.putText(img , str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),3)

    cv2.imshow("op",img)   
    key = cv2.waitKey(1)
    if key ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()