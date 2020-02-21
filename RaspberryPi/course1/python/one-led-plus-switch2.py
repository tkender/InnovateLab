#!/usr/bin/python3

import gpiozero, signal

one_led = gpiozero.LED(17)

print("LED on with switch")
print("Ctrl C to quit")

def onbuttonpress():
    one_led.on()

def onbuttonrelease():
    one_led.off()

button = gpiozero.Button(25)
button.when_pressed = onbuttonpress
button.when_released = onbuttonrelease

signal.pause()
