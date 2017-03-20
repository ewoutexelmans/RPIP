import RPi.GPIO as GPIO
import time

switch=18
led=23
dc=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)

p=GPIO.PWM(led, 50)

p.start(dc)

try:
	while True:
		if GPIO.wait_for_edge(switch, GPIO.RISING):
			if dc <100:
				dc+=10
				p.ChangeDutyCycle(dc)
			else:
				dc=0
				p.ChangeDutyCycle(dc)

except KeyboardInterrupt:
	print "cleanup program"
except:
	print "Other error or exception occured!"
finally:
	p.stop()
	GPIO.cleanup()
