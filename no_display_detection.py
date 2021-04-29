import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
import cv2.aruco as aruco
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import math


#------------------------------------------------------------------------------
#------- ROTATIONS https://www.learnopencv.com/rotation-matrix-to-euler-angles/
#------------------------------------------------------------------------------
# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6


# Calculates rotation matrix to euler angles
# The result is the same as MATLAB except the order
# of the euler angles ( x and z are swapped ).
def rotationMatrixToEulerAngles(R):
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([x, y, z])



R_flip  = np.zeros((3,3), dtype=np.float32)
R_flip[0,0] = 1.0
R_flip[1,1] =-1.0
R_flip[2,2] =-1.0



camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 60

mtx = np.array([[505.377, 0, 305.481],
       [0, 505.035, 236.892],
       [0, 0, 1]])

dist = np.array([[0.17123, -0.17193, -0.00691, -0.0107, -0.2530]])


raw_capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
 



f = open("distance_time.txt", "w")
f2 = open("velocity_time.txt", "w")
f3 = open("yaw_time.txt", "w")
start_time = time.time()
time_array = []
distance_array = []


dist1 = 0
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0

model = LinearRegression()

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):

    image = frame.array
    #cv2.imshow("Frame", image)

    parameters =  aruco.DetectorParameters_create()
    parameters.adaptiveThreshConstant = 10
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    #font = cv2.FONT_HERSHEY_SIMPLEX

    if np.all(ids != None):  
        for i in range(0, len(ids)):  
            # second arg is the size of the real world marker (in any unit)
            # the translational vectors are returned with the same unit
            ret = aruco.estimatePoseSingleMarkers(corners[i], 2.5, mtx, dist)
            rvec, tvec = ret[0][0,0,:], ret[1][0,0,:]

        #for i in range(0, len(ids)):
            #aruco.drawAxis(image, mtx, dist, rvec, tvec, 1)

        t5 = t4
        t4 = t3
        t3 = t2
        t2 = t1
        t1 = time.time() - start_time

        dist1 = math.sqrt(pow(tvec[0], 2) + pow(tvec[1], 2) + pow(tvec[2], 2))
        if dist1 > 300:
            break


        R_ct = np.matrix(cv2.Rodrigues(rvec)[0])
        R_tc = R_ct.T

        roll, pitch, yaw = rotationMatrixToEulerAngles(R_flip*R_tc)
        pitch_time = str(math.degrees(pitch)) + " " + str(t1) + "\n"
        f3.write(pitch_time)


        print("Positon: d=%f,   Angle: theta=%f deg    (x=%f   y=%f   z=%f)"%(dist1, math.degrees(pitch), tvec[0], tvec[1], tvec[2]))
        dist_time = str(dist1) + " " + str(t1) + "\n"
        time_array.append(t1)
        distance_array.append(dist1)

        if len(time_array) > 7:
            x = np.array(time_array[-7:]).reshape(-1,1)
            y = np.array(distance_array[-7:]) 

            model.fit(x, y)
            velocity = float(model.coef_)
            vel_time = str(velocity) + " " + str(t4) + "\n"
            f2.write(vel_time)


        f.write(dist_time)
        #aruco.drawDetectedMarkers(image, corners)

    #else:
        # code to show 'No Ids' when no markers are found
        #cv2.putText(image, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)

    #cv2.imshow('frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    raw_capture.truncate(0)

f.close()
f2.close()
f3.close()
cv2.destroyAllWindows()