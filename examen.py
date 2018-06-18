import time
import math
import readchar
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

looping = True

button = 4
pwmPin = 12

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pwmPin, GPIO.OUT)

pwm = GPIO.PWM(pwmPin, 1500)

def interrupt(channel):
    global looping
    looping=False

GPIO.add_event_detect(button, GPIO.FALLING, callback=interrupt,bouncetime=30)

file = open("sinus", "w")

for x in range(0,361,18):
    sine = str(math.sin(x))
    file.write(sine +"\n")
file.close()
file = open("sinus", "r")
print(file.read())
file.close()


while looping:
    print("press a for sine, b for triangle, c to end the program")
    if readchar.readkey()== 'a':
        pwm.start(0)
        file=open("sinus", "r")
        for x in range(0,361,18):
            pwm.ChangeDutyCycle(float(file.readline()))
            time.sleep(0.002)
        file.close()
    if readchar.readkey()== 'b':
        pwm.start(0)
        for i in range(0,101):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.002)
        for i in range(0,101):
            pwm.ChangeDutyCycle(100-i)
            time.sleep(0.002)
    if readchar.readkey()== 'c':
        looping = False

print("cleanup and shutting down program")
GPIO.remove_event_detect(button)
GPIO.cleanup()
