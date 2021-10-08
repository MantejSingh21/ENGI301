# Import Libraries
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
# Initial Variables
servo1 = "P2_1"
servo2 = "P2_3"



# Calibrate servo
PWM.start(servo1,50,60)
time.sleep (1.0)
PWM.stop(servo1)
PWM.cleanup()

PWM.start(servo2,50,60)
time.sleep (1.0)
PWM.stop(servo2)
PWM.cleanup()



while True:
    
# Rotate the servo CCW 180 degrees
    PWM.start(servo1,0,100)
    PWM.start(servo2,50,100)
    time.sleep (1.0)
    PWM.stop(servo1)
    PWM.stop(servo2)
    PWM.cleanup()
    print('Motion detected!')
    
    PWM.start(servo1,50,100)
    PWM.start(servo2,0,100)
    time.sleep (1.0)
    PWM.stop(servo1)
    PWM.stop(servo2)
    PWM.cleanup() 

    time.sleep(1.0)
    # Press CTRL + C to end program
