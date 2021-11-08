# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Bubba - The spider robot
--------------------------------------------------------------------------
License:   
Copyright 2020 Mantej Singh

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
"""

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
trigger = "P1_6"
echo = "P1_8"


# Set up function to intialize the servo motors
def setup():
    PWM.start(servo1, 5, 50, 0)
    PWM.start(servo2, 5, 50, 0)
    PWM.start(servo3, 5, 50, 0)
    PWM.start(servo4, 5, 50, 0)
    

def moveFrontRight():

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))

    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo1, 15)
    time.sleep (0.5)

    PWM.set_duty_cycle(servo1, 5)

    print("Front Right Motion cycle complete")
    
def moveFrontLeft():
    
    time.sleep (1)
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    
    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo2, 15)
    time.sleep (0.5)

    PWM.set_duty_cycle(servo2, 5)

    print("Front Left Motion cycle complete")

def moveBackRight():
    
    time.sleep (1.5)
    print("Task 3 assigned to thread: {}".format(threading.current_thread().name))
    
    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo3, 5)
    time.sleep (0.5)

    PWM.set_duty_cycle(servo3, 20)

    print("Back Right Motion cycle complete")

def moveBackLeft():
    
    print("Task 4 assigned to thread: {}".format(threading.current_thread().name))
    # Rotate the servo CCW 180 degrees
    PWM.set_duty_cycle(servo4, 5)
    time.sleep (0.5)

    PWM.set_duty_cycle(servo4, 20)

    print("Back Left Motion cycle complete")

if __name__ == "__main__":
    
    # Intialize the setup function
    setup()
    
    
    while(1):
    
        # Spawn 4 threads and execute each function
        t1 = threading.Thread(target=moveFrontRight, name="t1")
        t1.start()
        t2 = threading.Thread(target=moveFrontLeft, name="t2")
        t2.start()
        t3 = threading.Thread(target=moveBackLeft, name="t3")
        t3.start()
        t4 = threading.Thread(target=moveBackRight, name="t4")
        t4.start()
        time.sleep(1)
    
