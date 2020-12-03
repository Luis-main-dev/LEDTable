#!/usr/bin/env python3

import time
from rpi_ws281x import *
import argparse
import random

# LED strip configuration:
LED_COUNT      = 144     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 1     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def randomColor(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

        #time.sleep(wait_ms/1000.0) #Prüfen ob alle gleichzeitig an gehen, ansonsten auskommentieren
    strip.show()

def strobo(strip):
    count = 0
    while count < 5000:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,255))
        time.sleep(0.1)
        strip.show()
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0,0,0))
        time.sleep(0.1)
        strip.show()
        count+=1

def randomColorMatrix(strip):
    r= 0
    g= 0
    b= 0

    count= 0
    mode= 0
    while count < 5000:
        count+=1
        strip.setPixelColor(random.randint(0,143), Color(r, g, b))

        if count > 80:
            strip.setPixelColor(random.randint(0, 143), Color(0, 0, 0))

        strip.show()
        time.sleep(0.01)
        if (count % 100) == 0:
            mode = random.randint(0, 4)

        if mode == 0 and r < 255:
            print("mode 0")
            r+= 1
        if mode == 1 and g < 255:
            print("mode 1")
            g+=1
        if mode == 2 and r > 0:
            print("mode 2")
            r-=1
        if mode == 3 and b < 255 and g > 0:
            print("mode 3")
            b+=1
            g-=1




# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        while True:
            print ('Start showing random Colors')
            #randomColor(strip, Color(random.randint(0,255),random.randint(0,255), random.randint(0,255)))
            randomColorMatrix(strip)
            #strobo(strip)
            time.sleep(2)

    except KeyboardInterrupt:
        if args.clear:
            #randomColor(strip, Color(0,0,0), 10)
            randomColorMatrix(strip)
            #strobo(strip)
