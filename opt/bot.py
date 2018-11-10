import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print 'Got command: %s' % command

        if command == '/roll':
                bot.sendMessage(chat_id, random.randint(1,6))
        elif command == '/time':
                bot.sendMessage(chat_id, str(datetime.datetime.now()))

        elif command == '/red':
                GPIO.output(21,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(21,GPIO.LOW)
                bot.sendMessage(chat_id, "Blinked red LED")

        elif command == '/yellow':
                GPIO.output(5,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(5,GPIO.LOW)
                bot.sendMessage(chat_id, "Blinked yellow LED")

        elif command == '/green':
                GPIO.output(10,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(10,GPIO.LOW)
                bot.sendMessage(chat_id, "Blinked green LED")

        elif command == '/white':
                GPIO.output(27,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(27,GPIO.LOW)
                bot.sendMessage(chat_id, "Blinked white LED")

        elif command == '/kit':
                bot.sendMessage(chat_id, "I need ya buddy!")
                count = 0
                while (count < 4):
                        GPIO.output(21,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(5,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(10,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(27,GPIO.HIGH)
						time.sleep(0.1)
                        GPIO.output(21,GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(5,GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(10,GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(27,GPIO.LOW)
                        GPIO.output(27,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(10,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(5,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(21,GPIO.HIGH)
                        time.sleep(0.1)
                        GPIO.output(27,GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(10,GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(5,GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(21,GPIO.LOW)
                        count = count + 1
                bot.sendMessage(chat_id, "Right away Michael.")

bot = telepot.Bot('INSERT YOUR BOT TOKEN HERE!')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
        time.sleep(10)