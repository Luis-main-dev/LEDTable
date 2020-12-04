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
LED_BRIGHTNESS = 15     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def circleEffect(strip):
    strip.setPixelColor(strip.getNumOfCoordinates(5, 5), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(5, 6), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(5, 4), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(6, 3), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(6, 4), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(5, 3), Color(255, 0, 0))
    time.sleep(2)
    strip.show()

    strip.setPixelColor(strip.getNumOfCoordinates(5, 7), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(6, 7), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(5, 8), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(6, 8), Color(255, 0, 0))
    time.sleep(2)
    strip.show()

    strip.setPixelColor(strip.getNumOfCoordinates(4, 4), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(4, 6), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(4, 7), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(4, 5), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(3, 5), Color(255, 0, 0))
    time.sleep(2)
    strip.show()
    strip.setPixelColor(strip.getNumOfCoordinates(3, 6), Color(255, 0, 0))
    time.sleep(2)
    strip.show()

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
            circleEffect(strip)
            time.sleep(5)

    except KeyboardInterrupt:
        if args.clear:
            circleEffect(strip)
