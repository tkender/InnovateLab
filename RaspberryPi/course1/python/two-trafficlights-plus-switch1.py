#!/usr/bin/python3

import gpiozero, time

red1_led    = gpiozero.LED(17)
yellow1_led = gpiozero.LED(27)
green1_led  = gpiozero.LED(22)

red2_led    = gpiozero.LED(13)
yellow2_led = gpiozero.LED(19)
green2_led  = gpiozero.LED(26)

print("Two stoplights with car sensor")
print("Ctrl C to quit")

mintime = 10 # seconds
greentime = 3 # seconds
yellowtime = 1 # second

button = gpiozero.Button(25)

# everything starts in off state
while True:
    # G    R    3 sec
    green1_led.on()
    red2_led.on()

    wasPressed = False
    for i in range(int(mintime / 0.1)):
        if button.is_pressed:
            wasPressed = True
        time.sleep(0.1)

    if not wasPressed:
        while not button.is_pressed:
            time.sleep(0.1)

    # Y    R    1 sec
    green1_led.off()
    yellow1_led.on()
    time.sleep(yellowtime)

    # R    G    3 sec
    yellow1_led.off()
    red1_led.on()
    red2_led.off()
    green2_led.on()
    time.sleep(greentime)

    # R    Y    1 sec
    green2_led.off()
    yellow2_led.on()
    time.sleep(yellowtime)

    # all off before restarting
    red1_led.off()
    yellow2_led.off()
