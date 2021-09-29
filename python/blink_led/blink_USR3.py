# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blinking USR3 LED 
--------------------------------------------------------------------------
License:   
Copyright 2021 Mantej Singh

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple program that will use the Adafruit BBIO library to blink the 
USR3 LED at 5Hz.
--------------------------------------------------------------------------
"""

#-------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------
import Adafruit_BBIO.GPIO as GPIO
import time

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

'NONE'

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
GPIO.setup("USR3", GPIO.OUT)

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def blinkUSR3LED():
    """
    This function blinks USR3 LED at 5Hz
    """

    while True:
            # Pull the pin high for 100ms
            GPIO.output("USR3", GPIO.HIGH)
            time.sleep(0.1)
            # Pull the pin low for 100ms
            GPIO.output("USR3", GPIO.LOW)
            time.sleep(0.1)
            # The entire on/off cycle should complete in 0.2s which is = 1/5hz

# END DEF

blinkUSR3LED()