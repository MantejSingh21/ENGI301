# Import Libraries
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
import threading 
import os
# Initial Variables
servo1 = "P2_1"
servo2 = "P2_3"
servo3 = "P1_36"
servo4 = "P1_33"


def setup():
    PWM.start(servo1, 5, 50, 0)
    PWM.start(servo2, 5, 50, 0)
    PWM.start(servo3, 5, 50, 0)
    PWM.start(servo4, 5, 50, 0)

def moveFrontRight():

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))

    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo1, 10)
    time.sleep (0.1)

    PWM.set_duty_cycle(servo1, 5)

    print("Front Right Motion cycle complete")
    
def moveFrontLeft():
    

    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    
    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo2, 10)
    time.sleep (0.1)

    PWM.set_duty_cycle(servo2, 5)

    print("Front Left Motion cycle complete")

def moveBackRight():
    
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))

    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo3, 5)
    time.sleep (0.1)

    PWM.set_duty_cycle(servo3, 20)

    print("Back Right Motion cycle complete")

def moveBackLeft():
    
    print("Task 4 assigned to thread: {}".format(threading.current_thread().name))
    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo4, 5)
    time.sleep (0.1)

    PWM.set_duty_cycle(servo4, 15)

    print("Back Left Motion cycle complete")

if __name__ == "__main__":
    
    #moveFrontRight()
    setup()
    
    while(1):
    
        t1 = threading.Thread(target=moveFrontRight, name="t1")
        t1.start()
        t2 = threading.Thread(target=moveFrontLeft, name="t2")
        t2.start()
        t3 = threading.Thread(target=moveBackLeft, name="t3")
        t3.start()
        t4 = threading.Thread(target=moveBackRight, name="t4")
        t4.start()
        time.sleep(1)
        # t1.join()
    
