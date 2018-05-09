import RPi.GPIO as GPIO
import readchar

GPIO.setmode(GPIO.BCM)

pin1 = 12
pin2 = 18

freq = 100
dc = 10

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

pwm1 = GPIO.PWM(pin1,freq)
pwm2 = GPIO.PWM(pin2,freq)
pwm1.start(dc)
pwm2.start(dc)


while readchar.readkey() != readchar.key.ENTER:
    if readchar.readkey()=='a':
        freq = 100
        print(freq)
    if readchar.readkey()=='z':
        freq = 1000
        print(freq)
    if readchar.readkey()=='e':
        freq = 5000
        print(freq)
    if readchar.readkey()=='r':
        freq = 10000
        print(freq)
    if readchar.readkey()=='q':
        dc = 10
        print(dc)
    if readchar.readkey()=='s':
        dc = 50
        print(dc)

    pwm1.ChangeDutyCycle(dc)
    pwm2.ChangeDutyCycle(dc)
    pwm1.ChangeFrequency(freq)
    pwm2.ChangeFrequency(freq)

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
print("Cleanup and shutting down program")
