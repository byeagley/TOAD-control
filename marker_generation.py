import cv2
import numpy as np
import cv2.aruco as aruco



aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
marker = np.zeros((200, 200), dtype=np.uint8)
marker = aruco.drawMarker(aruco_dict, 1, 200, marker, 1)

cv2.imwrite("marker.png", marker)
