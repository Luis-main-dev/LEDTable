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
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def randomColor(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        #time.sleep(wait_ms/1000.0) #Prüfen ob alle gleichzeitig an gehen, ansonsten auskommentieren

def showAllColors(strip):
    r = 0
    g = 0
    b = 0
    for k in range(0, 10):
        for i in range(strip.numPixels()):
            time.sleep(0.1)
            strip.setPixelColor(i, Color(r,g,b))
            print ("r ", r, ", g ", g, ", b ", b)
            if(r < 255):
                r+=1
            elif(g < 255):
                g+= 1
            elif(b < 255):
                b+=1

            strip.show()

def singleColor(strip):
    strip.setPixelColor(0, Color(255,0,0))
    strip.setPixelColor(11, Color(0,255,0))
    strip.setPixelColor(143, Color(0,0,255))
    strip.show()

def frameEffect(strip):
    r = 50
    g = 30
    b = 30
    for numA in range(0, 12):   # oben
        strip.setPixelColor(numA, Color(r, g, b))
        r+=3

    numB = 12
    while numB <= 131:          # rechts
        strip.setPixelColor(numB, Color(r, g, b))
        if (numB % 2) == 0:
            numB+= 23
        else:
            numB+=1
        r+=3

    for numC in range(132, 144):    # unten
        strip.setPixelColor(numC, Color(r, g, b))
        r+=3

    numD = 120
    while numD >= 23:       # links
        strip.setPixelColor(numD, Color(r, g, b))
        if (numD % 2) == 0:
            numD-= 1
        else:
            numD-=23
        r+=3

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
            # randomColor(strip, Color(random.randint(0,255),random.randint(0,255), random.randint(0,255)))
            # showAllColors(strip)
            # singleColor(strip)
            frameEffect(strip)
            time.sleep(5)

    except KeyboardInterrupt:
        if args.clear:
            # randomColor(strip, Color(0,0,0), 10)
            # showAllColors(strip)
            # singleColor(strip)
            frameEffect(strip)
