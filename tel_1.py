from Adafruit_IO import Client, Feed, Data
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import os
"""

GRL
Active Key
aio_bRDk35cNyF0fn4umtJwbIoJAHHoM
Hide Code Samples

Arduino
=======
#define IO_USERNAME  "GRL"
#define IO_KEY       "aio_bRDk35cNyF0fn4umtJwbIoJAHHoM"

Linux Shell
===========
export IO_USERNAME="GRL"
export IO_KEY="aio_bRDk35cNyF0fn4umtJwbIoJAHHoM"

Scripting
=========
ADAFRUIT_IO_USERNAME = "GRL"
ADAFRUIT_IO_KEY = "aio_bRDk35cNyF0fn4umtJwbIoJAHHoM"
"""

#creation the feed(this should be done only once)…..if you want to create the feed automatically from code then run this part of code separately or else you can create
#feed = Feed(name='light-bot-feed')
#result = aio.create_feed(feed)
#adafruit_io user name and active key

ADAFRUIT_IO_USERNAME = os.getenv('GRL')
ADAFRUIT_IO_KEY = os.getenv('aio_bRDk35cNyF0fn4umtJwbIoJAHHoM')
aio = Client('GRL','aio_bRDk35cNyF0fn4umtJwbIoJAHHoM')
Telegram_token = os.getenv('1020207388:AAEwLSS9zdmlpnEUaDkwmRizOfDQacVIGYg')

#this function is used reply when you start the bot
def start(bot, update):
    bot.send_message(chat_id = update.effective_chat.id, text="Welcome!")
    bot.send_message(chat_id = update.effective_chat.id, text="if you like to turn on the light then type 'Turn on the light' or if you would like to turn off the lights then type 'Turn off the light'")

#this function is used reply when we input apart from the requirement
def wrong_message(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops, I unable to understand that. Please try again!")

#this function is used to send data to adafruit_io feed mentioned
def send_data_adafruit(value1):
  value = Data(value=value1)
  value_send = aio.create_data('light-bot-feed',value)  

#function to turn on the light 
def turn_on_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning on the light")
  bot.send_photo(chat_id, photo='http://scienceblog.cancerresearchuk.org/wp-content/uploads/2015/08/Lightbulb_hero2.jpg')
  send_data_adafruit(1)

#function to turn off the light
def turn_off_light(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning off the light")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  send_data_adafruit(0)

def text_given(bot, update):
  text = update.message.text
  if text == 'Start':
    start(bot,update)
  elif text == 'Turn on the light':
    turn_on_light(bot,update)
  elif text == 'Turn off the light':
    turn_off_light(bot,update)
  else:
    wrong_message(bot,update)
    
ud = Updater('1020207388:AAEwLSS9zdmlpnEUaDkwmRizOfDQacVIGYg')
dip = ud.dispatcher
dip.add_handler(MessageHandler(Filters.text, text_given))

ud.start_polling()
ud.idle()