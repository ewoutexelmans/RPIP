import RPi.GPIO as GPIO
import time

switch=18
led=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)


def btnPress():
	if GPIO.input(led):
		state=0
	else:
		state=1
	return state

try:
	while True:
		if GPIO.wait_for_edge(switch, GPIO.RISING):
				GPIO.output(led, btnPress())

except KeyboardInterrupt:
	print "cleanup program"
except:
	print "Other error or exception occured!"
finally:
	GPIO.cleanup()
