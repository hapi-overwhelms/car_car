from .control import Control
from .detect import Detect
from .lcd import Lcd

class Brain(object):
    def __init__(self):
        self.control = Control()
        self.det = Detect()

    def location_judge(self,location:list):
        pixel = abs(location[0] - location[1]) * abs(location[2] - location[3])
        location_x = (location[0] + location[1]) /2
        location_y = (location[2] + location[3]) /2

        if (location_x) > self.det.width and location_y > self.det.height:
            print("one")
        elif(location_x < self.det.width) and location_y > self.det.height:
            print("two")
        elif(location_x < self.det.width) and location_y < self.det.height:
            print("three")
        elif (location_x) > self.det.width and location_y < self.det.height:
            print("four")
        elif  (location_x) == self.det.width and location_y == self.det.height:
            self.control.car_front()

    def start(self):
        while True:
            ret, self.frame = self.cap.read()
            ball_exisit , location = self.det.get_yolo_result(self.frame)
            if ball_exisit:
                self.location_judge(location)

