# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    led[0] = (0, 0, 255) # bright blue
    time.sleep(3)
    led.brightness = 0.1
    led[0] = (0, 0, 255) # fading blue, signaling something wrong
    time.sleep(3)
    led.brightness = 1
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(0.5)
    led.brightness = 0
    led[0] = (255, 0, 0) #red, beginning of the SOS message,three secs to speel out S in short pulses
    time.sleep(1)
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(0.5)
    led.brightness = 0
    led[0] = (255, 0, 0) #red
    time.sleep(1) # short pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(0.5)
    led.brightness = 0
    led[0] = (255, 0, 0) #red
    time.sleep(1) # short pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(0.5)
    led.brightness = 0
    led[0] = (255, 0, 0) #red, spelling out the O using long pulses
    time.sleep(3) # long pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(3)
    led.brightness = 0
    led[0] = (255, 0, 0) #red
    time.sleep(3) # long pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(1)
    led.brightness = 0
    led[0] = (255, 0, 0) #red
    time.sleep(3) # long pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(3)
    led.brightness = 0
    led[0] = (255, 0, 0) #red,three secs to speel out S in short pulses
    time.sleep(0.5)
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(0.5)
    led.brightness = 0
    led[0] = (255, 0, 0) #red
    time.sleep(1) # short pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # pause between the message
    time.sleep(0.5)
    led.brightness = 0
    led[0] = (255, 0, 0) #red
    time.sleep(1) # short pulse duration
    led.brightness = 0.5
    led[0] = (255, 0, 0) # stop ending the message
    time.sleep(0.5)
    led.brightness = 0

