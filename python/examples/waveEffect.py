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
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def waveEffect(strip):
    # Farbe
    r= 255
    g= 0
    b= 0

    # Nummer aller LEDs
    numA= -1

    # markiert das Zeilenende
    newLine = 11

    lineRepeater = 0

    # maximale Anzahl der Zeilenwiederholungen
    lineRepeaterEnd = 50

    # Mittelpunkt der Anzahl der Zeilenwiederholungen
    lineRepeaterMidPoint = 25

    # Helligkeit
    brtn= 0

    while numA < 144:
        numA += 1
        strip.setPixelColor(numA, Color(r, g, b))
        strip.show()

        if numA == newLine: # Zeilen-Ende?

            if lineRepeater < lineRepeaterMidPoint:    # heller
                brtn+=4
            elif lineRepeater < lineRepeaterEnd:    # dunkler
                brtn-=4

            #print("bntn ", brtn)
            strip.setBrightness(brtn)
            time.sleep(0.0001)  # warten

            if lineRepeater <= lineRepeaterEnd: # Wiederholungsende noch nicht erreicht
                numA-= 11
                lineRepeater+= 1
            else:               # neue Zeile beginnen
                newLine+=12
                lineRepeater= 0

                darkA = numA    # vorherige Zeilen löschen
                while darkA >= 0:
                    strip.setPixelColor(darkA, Color(0, 0, 0))
                    darkA -= 1



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
            # frameEffect(strip)
            waveEffect(strip)
            #time.sleep(5)

    except KeyboardInterrupt:
        if args.clear:
            # randomColor(strip, Color(0,0,0), 10)
            # showAllColors(strip)
            # singleColor(strip)
            # frameEffect(strip)
            waveEffect(strip)
