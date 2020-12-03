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


def randomColor(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        #time.sleep(wait_ms/1000.0) #Prüfen ob alle gleichzeitig an gehen, ansonsten auskommentieren

# zeigt alle LEDs mit Farbe
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

# zeigt markante LEDs (Debug Info)
def singleColor(strip):
    strip.setPixelColor(0, Color(255,0,0))
    strip.setPixelColor(11, Color(0,255,0))
    strip.setPixelColor(143, Color(0,0,255))
    strip.show()

# erzeugt einen Farbverlauf-Rahmen um die Matrix
def frameEffect(strip):
    r = 252
    g = 0
    b = 0

    for numA in range(0, 12):   # oben, rot zu gelb
        strip.setPixelColor(numA, Color(r, g, b))
        g+=21
        strip.show()
        time.sleep(0.5)

    numB = 12
    while numB <= 131:          # rechts, gelb zu grün
        strip.setPixelColor(numB, Color(r, g, b))
        if (numB % 2) == 0:
            numB+= 23
        else:
            numB+=1
        r-= 21
        strip.show()
        time.sleep(0.5)

    for numC in range(132, 144):    # unten, grün zu blau
        strip.setPixelColor(numC, Color(r, g, b))
        b+=21
        g-=21
        strip.show()
        time.sleep(0.5)

    numD = 120
    while numD >= 23:       # links, blau zu lila
        strip.setPixelColor(numD, Color(r, g, b))
        if (numD % 2) == 0:
            numD-= 1
        else:
            numD-=23
        r+=21
        strip.show()
        time.sleep(0.5)

def waveEffectOld(strip):
    r= 255
    g= 0
    b= 0

    newLine= 11
    lineRepeater= 0
    numA= 0
    brtn= 0
    repeatingEnd = 255
    thadePoint = 125
    # strip.setBrightness(brtn)

    while numA < 144:
        strip.setPixelColor(numA, Color(r, g, b))

        if numA == newLine:

            if lineRepeater == repeatingEnd:
                darkA = numA
                while darkA >= 0:
                    strip.setPixelColor(darkA, Color(0, 0, 0))
                    darkA-= 1

                #strip.show()
                newLine+= 12
                brtn= 0
                lineRepeater = 0
                print("Line is ending!")
                # time.sleep(0.2)

            if lineRepeater < repeatingEnd:
                numA-= 11
                brtn+= 1
                lineRepeater+=1
                print("Heller!")
                time.sleep(0.01)
            """"
            if lineRepeater > thadePoint and lineRepeater <= repeatingEnd:
                numA-= 11
                brtn-= 1
                lineRepeater+=1
                print("Dunkler!")
                time.sleep(0.01)
                """
            strip.setBrightness(brtn)
            strip.show()
        numA+= 1

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
