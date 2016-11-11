#!/usr/bin/python
import grovepi
import atexit
import dweepy
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)
temp = grove.GroveTemp(1)
relay = grove.GroveRelay(2)

datafreeboard = {}
datadweet = "Aguilas"

def functionLight(bot, update):
    luxes = light.value()
 #   bot.sendMessage(update.message.chat_id, text='Light! ' + 
str(luxes))

#def functionMessage(bot, update):
 #   bot.sendMessage(update.message.chat_id, text=message)

#def functionPicture(bot, update):
  #  bot.sendPhoto(update.message.chat_id, 
#photo=open('documentation/image.jpg',$

'''
def functionRelay(bot, update):
    relay.on()
    time.sleep(2)
    relay.off()
    bot.sendMessage(update.message.chat_id, text='Relay!')
Â´Â
def functionEcho(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)
'''
def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
        time.sleep(2)
        datafreeboard['alive'] = 0
        datafreeboard['luxes'] =  0
        datafreeboard['message'] = "None"
        datafreeboard['sensort'] = 0
        dweepy.dweet_for(datadweet, datafreeboard)
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

    message = "Hola Cacerola! I'm Xpuhil!"

    while True:
	alive=button.value()
        luxes = light.value()
	luxes.int(luxes)
        sensort = temp.value()
	display.setColor(luxes, luxes, luxes)
	display.clear()

	datafreeboard = {}
        datafreeboard['alive'] = alive
        datafreeboard['alive'] = "1"
        datafreeboard['luxes'] =  luxes
        datafreeboard['message'] = message
        datafreeboard['sensort'] = sensort
        dweepy.dweet_for(datadweet, datafreeboard)

	if button.value() is 1:
            display.setColor(255,0,0)
            display.setCursor(0,0)
	    display.write(str(message))
	    relay.on()
	    time.sleep(1)
	    relay.off()        

        time.sleep(1)
