#!/usr/bin/python3
import RPi.GPIO as GPIO
import readchar


GPIO.setmode(GPIO.BCM)

led = 4
buttons = [2,3]

dc = 50

GPIO.setup(led , GPIO.OUT)
GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwmPin = GPIO.PWM(led, 100)
pwmPin.start(dc)

def change_brightness(channel):
    global dc
    if channel == buttons[0]:
        dc+=10 if dc <100 else 0
    else:
        dc-=10 if dc >0 else 0
    pwmPin.ChangeDutyCycle(dc)

GPIO.add_event_detect(buttons[0], GPIO.FALLING, callback=change_brightness, bouncetime = 100)
GPIO.add_event_detect(buttons[1], GPIO.FALLING, callback=change_brightness, bouncetime = 100)



while readchar.readkey()!=readchar.key.ENTER:
    pass
else:
    print("shutting down program")
    pwmPin.stop()
    GPIO.cleanup()
    print("cleanup complete")


