import cv2 as cv
import numpy as np
import cv.aruco as aruco

parameters =  cv.aruco.DetectorParameters_create()
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)

cap = cv.VideoCapture(1) 

def track(matrix_coeffs, distortion_coeffs):
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict, parameters=parameters, cameraMatrix=matrix_coeffs, distCoeff=distortion_coeffs)

