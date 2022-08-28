import RPi.GPIO as GPIO



class Control(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

    def car_stop(self):
        GPIO.output(17, False)
        GPIO.output(18, False)
        GPIO.output(22, False)
        GPIO.output(23, False)

    def car_front(self):
        GPIO.output(17, False)
        GPIO.output(18, True)
        GPIO.output(22, False)
        GPIO.output(23, True)

    def car_back(self):
        GPIO.output(17, True)
        GPIO.output(18, False)
        GPIO.output(22, True)
        GPIO.output(23, False)

    def car_right(self): 
       GPIO.output(17, False)
       GPIO.output(18, True)
       GPIO.output(22, False)
       GPIO.output(23, False)
    
    def car_left(self):
       GPIO.output(17, False)
       GPIO.output(18, False)
       GPIO.output(22, False)
       GPIO.output(23, True)