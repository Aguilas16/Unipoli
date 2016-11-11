#!/usr/bin/python
import grovepi
import atexit
import dweepy
import signal
import sys
import time
import ConfigParser

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

credentials = ConfigParser.ConfigParser()
credentialsfile = "credentials.config"
credentials.read(credentialsfile)

button = grove.GroveButton(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)
temp = grove.GroveTemp(1)
relay = grove.GroveRelay(2)

datafreeboard = {}
datadweet = "Aguilas"

def functionLight(bot, update):
    luxes = light.value()
    bot.sendMessage(update.message.chat_id, text='Light! ' + str(luxes))

def functionMessage(bot, update):
    bot.sendMessage(update.message.chat_id, text=message)

#def functionPicture(bot, update):
 #   bot.sendPhoto(update.message.chat_id,photo=open('documentation/image.jpg',$

def functionRelay(bot, update):
    relay.on()
    time.sleep(2)
    relay.off()
    bot.sendMessage(update.message.chat_id, text='Relay!')

def functionEcho(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

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

    credential = credentials.get("telegram", "token")
    updater = Updater(credential)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("light", functionLight))
    dp.add_handler(CommandHandler("message", functionMessage))
#    dp.add_handler(CommandHandler("picture", functionPicture))
    dp.add_handler(CommandHandler("relay", functionRelay))
    dp.add_handler(MessageHandler([Filters.text], functionEcho))

    updater.start_polling()

    message = "Hola Cacerola! I'm Xpuhil!"

    while True:
	alive=button.value()
        luxes = light.value()
	luxes.int(luxes)
        sensort = temp.value()
	display.setColor(luxes, luxes, luxes)
	display.clear()

credential = credentials.get("telegram", "token")
    updater = Updater(credential)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("light", functionLight))
    dp.add_handler(CommandHandler("message", functionMessage))
    dp.add_handler(CommandHandler("picture", functionPicture))
    dp.add_handler(CommandHandler("relay", functionRelay))
    dp.add_handler(MessageHandler([Filters.text], functionEcho))

    updater.start_polling()
	
#	datafreeboard = {}
        datafreeboard['alive'] = alive
#        datafreeboard['alive'] = "1"
        datafreeboard['luxes'] =  luxes
        datafreeboard['message'] = message
        datafreeboard['sensort'] = sensort
        dweepy.dweet_for(datadweet, datafreeboard)
	
	while True:
        luxes = light.value()
        luxes = int(luxes)
        display.setColor(luxes, luxes, luxes)
        display.clear()

	if button.value() is 1:
            display.setColor(255,0,0)
            display.setCursor(0,0)
	    display.write(str(message))
	    relay.on()
	    time.sleep(1)
	    relay.off()        

        time.sleep(1)
