import cv2
import numpy as np
import cv2.aruco as aruco
import numpy as np

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import math


camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 60

mtx = np.array([[505.377, 0, 305.481],
       [0, 505.035, 236.892],
       [0, 0, 1]])

dist = np.array([[0.17123, -0.17193, -0.00691, -0.0107, -0.2530]])


raw_capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
 
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array
    #cv2.imshow("Frame", image)

    parameters =  aruco.DetectorParameters_create()
    parameters.adaptiveThreshConstant = 10
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if np.all(ids != None):  
        for i in range(0, len(ids)):  
            # second arg is the size of the real world marker (in any unit)
            # the translational vectors are returned with the same unit
            ret = aruco.estimatePoseSingleMarkers(corners[i], 2.5, mtx, dist)
            rvec, tvec = ret[0][0,0,:], ret[1][0,0,:]
            #(rvec - tvec).any() 

        for i in range(0, len(ids)):
            aruco.drawAxis(image, mtx, dist, rvec, tvec, 0.1)

        dist = math.sqrt(pow(tvec[0], 2) + pow(tvec[1], 2) + pow(tvec[2], 2))
        angle = rvec[2] / math.pi * 180

        print("Positon: d=%f,   Angle: theta=%f deg    (x=%f   y=%f   z=%f)"%(dist, angle, tvec[0], tvec[1], tvec[2]))

        aruco.drawDetectedMarkers(image, corners)

    else:
        # code to show 'No Ids' when no markers are found
        cv2.putText(image, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

    #cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    raw_capture.truncate(0)

cv2.destroyAllWindows()

