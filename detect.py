import cv2
import numpy as np

class Detect(object):
    def __init__(self):
        self.device_number = 0
        self.cap = cv2.VideoCapture(self.device_number)

        self.width = 640
        self.height = 480

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,self.height)

        

    def get_yolo_result(self):
        pass
        # true  