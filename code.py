# Created by: Daria Bernice Calitis
# Created on: Feb 2022
# This program is called Blinky and a Button

"""

Turns on the built-in LED for a certain time, then off for one second, repreatedly.
But the interval increases each time by 1 more second.

"""

import board
import digitalio
import time

blink_time = 1  # Duration of a turned on LED

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True       # Turns on LED
    time.sleep(blink_time) # Wait for the length of blink_time
    led.value = False      # Turns off LED
    time.sleep(1)          # Wait for 1 second
    blink_time += 1        # Adds 1 second to blink_time  
