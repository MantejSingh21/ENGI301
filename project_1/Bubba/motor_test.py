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


def moveFrontRight():
    
    print("ID of process 1: {}".format(os.getpid()))
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))

 
        
    # Rotate the servo CCW 180 degrees
    PWM.start(servo1,10,100)
    time.sleep (0.1)
    PWM.stop(servo1)
    PWM.cleanup()

    
    PWM.start(servo1,30,100)
    time.sleep (0.1)
    PWM.stop(servo1)
    PWM.cleanup() 

    print("Front Right Motion cycle complete")
    moveFrontLeft()
        
def moveFrontLeft():
    
    print("ID of process 2: {}".format(os.getpid()))
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    

        
    # Rotate the servo CCW 180 degrees
    PWM.start(servo2,10,100)
    time.sleep (0.1)
    PWM.stop(servo2)
    PWM.cleanup()

    
    PWM.start(servo2,30,100)
    time.sleep (0.1)
    PWM.stop(servo2)
    PWM.cleanup() 

    print("Front Left Motion cycle complete")
    moveBackRight()

def moveBackRight():
    
    print("ID of process 3: {}".format(os.getpid()))
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))

 
        
    # Rotate the servo CCW 180 degrees
    PWM.start(servo3,10,100)
    time.sleep (0.1)
    PWM.stop(servo3)
    PWM.cleanup()

    
    PWM.start(servo3,30,100)
    time.sleep (0.1)
    PWM.stop(servo3)
    PWM.cleanup() 

    print("Back Right Motion cycle complete")
    moveBackLeft()

def moveBackLeft():
    
    print("ID of process 4: {}".format(os.getpid()))
    print("Task 4 assigned to thread: {}".format(threading.current_thread().name))

 
        
    # Rotate the servo CCW 180 degrees
    PWM.start(servo4,10,100)
    time.sleep (0.1)
    PWM.stop(servo4)
    PWM.cleanup()

    
    PWM.start(servo4,30,100)
    time.sleep (0.1)
    PWM.stop(servo4)
    PWM.cleanup() 

    print("Back Left Motion cycle complete")
    moveFrontRight()

if __name__ == "__main__":
    
    moveFrontRight()
    
    # t1 = threading.Thread(target=moveFrontRight, name="t1")
    # t1.start()
    # t2 = threading.Thread(target=moveFrontLeft, name="t2")
    # t2.start()
    # t1.join()
    
