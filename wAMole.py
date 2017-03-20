import RPi.GPIO as GPIO
import time

switch=18
led=[23,24,25,8,7]
freq=2.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)

def whack(switch):
	global freq
	if GPIO.input(led[2]):
		print "Whack!"
		freq/=2
	else:
		print "Miss!"

GPIO.add_event_detect(switch, GPIO.RISING,callback=whack,bouncetime=100)

try:
	while True:
		for i in range(len(led)):
			GPIO.output(led, GPIO.LOW)
			GPIO.output(led[i], GPIO.HIGH)
			time.sleep(freq)		

except KeyboardInterrupt:
	print "cleanup program"
except:
	print "Other error or exception occured!"
finally:
	GPIO.cleanup()
