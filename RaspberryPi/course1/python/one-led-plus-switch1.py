#!/usr/bin/python3

import gpiozero, time

one_led = gpiozero.LED(17)

print("LED on with switch")
print("Ctrl C to quit")

button = gpiozero.Button(25)

while True:
    if button.is_pressed:
        one_led.on()
    else:
        one_led.off()
    time.sleep(0.1)
