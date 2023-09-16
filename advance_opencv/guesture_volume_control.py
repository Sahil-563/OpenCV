import cv2
import time
import numpy as np
import mediapipe as mp
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
ctime =0
ptime=0

cap = cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4,400)
detector = htm.handDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volumerange =volume.GetVolumeRange()

min_volume = volumerange[0]
max_volume = volumerange[1]


while True:
    success,img=cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw =False)
    if len(lmList)!=0:
        #print(lmList[4],lmList[8])
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx,cy = (x1+x2)//2,(y1+y2)//2

        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,0,255),cv2.FILLED)
        cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        #print(int(length))

        vol = np.interp(length,[30,300],[min_volume,max_volume])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length<30:
            cv2.circle(img,(cx,cy),10,(0,0,255),cv2.FILLED)
       



    ctime = time.time()
    fps =1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img,f"FPS: {int(fps)}",(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow("op",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

