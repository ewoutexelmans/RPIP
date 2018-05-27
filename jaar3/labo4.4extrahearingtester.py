#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpiod

GPIO.setmode(GPIO.BCM)

pwm = pigpio.pi()

buttons=[2,3]
pwmPin = 12

wait = True

freq = 0

def result(buttons[1]):
    global freq
    print(f"You can hear sounds up to {freq} Hz")

GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(buttons[0], GPIO.RISING)
GPIO.add_event_detect(buttons[1], GPIO.RISING, callback = result, bouncetime=100)


print("This is a program to test your hearing\nPush the firs button to start the test\nPush the second button when you can't hear anything anymore\nUSE A LOW VOLUME!!!!!")

while wait:
    if GPIO.event_detected(buttons[0]):
        wait = False
        print("Started hearing test")
GPIO.remove_event_detect(buttons[0])

for i in range(0,22000):
    freq = i
    pwm.hardware_PWM(pwmPin, freq, 500000)


GPIO.remove_event_detect(buttons[1])
GPIO.cleanup()
