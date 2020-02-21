#!/usr/bin/python3

import gpiozero, time

one_led = gpiozero.LED(17)

print("LED blinker")
print("Ctrl C to quit")

ontime = 0.33 # seconds
offtime = 0.33 # seconds

while True:
    one_led.on()
    time.sleep(ontime)
    one_led.off()
    time.sleep(offtime)
