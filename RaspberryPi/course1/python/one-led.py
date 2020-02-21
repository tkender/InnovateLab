#!/usr/bin/python3

import gpiozero
import time

one_led = gpiozero.LED(17)

print("LED on")

one_led.on()
time.sleep(5) # seconds
# everything turns off at the end
one_led.off()
print("LED off")
