#!/usr/bin/python3

import gpiozero, time

red_led    = gpiozero.LED(17)
yellow_led = gpiozero.LED(27)
green_led  = gpiozero.LED(22)

print("One stoplight")
print("Ctrl C to quit")

greentime = 3
yellowtime = 1

# everything starts in off state
while True:
    # G    2 sec
    green_led.on()
    time.sleep(greentime)
    green_led.off()

    # Y    1 sec
    yellow_led.on()
    time.sleep(yellowtime)
    yellow_led.off()

    # R    2 sec
    red_led.on()
    time.sleep(greentime+yellowtime)

    # all off before restarting
    red_led.off()
