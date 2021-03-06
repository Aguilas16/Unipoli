#!/usr/bin/python

import atexit
import dweepy
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_i2clcd as lcd

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)
relay = grove.GroveRelay(2)

datafreeboard = {}
datadweet = "ThisIsDweeting"

def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
        time.sleep(2)
        datafreeboard['alive'] = "0"
        datafreeboard['luxes'] =  0
        datafreeboard['message'] = "None"
        dweepy.dweet_for(datadweet, datafreeboard)
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

    message = "Hola Cacerola! I'm Xpuhil!"

    while True:

        luxes = light.value()

        datafreeboard['alive'] = "1"
        datafreeboard['luxes'] =  luxes
        datafreeboard['message'] = message
        dweepy.dweet_for(datadweet, datafreeboard)

        time.sleep(1)
