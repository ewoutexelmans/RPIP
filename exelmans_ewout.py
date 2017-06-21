import RPi.GPIO as io
import paho.mqtt.client as mqtt
import time
import os
import json

mqttc = mqtt.Client("", True, None, mqtt.MQTTv31)


btnPin = 11
ledPin = 12

path = os.path.join(os.path.expanduser('~pi'), 'Documents','count.txt')

count = 0


io.setmode(io.BCM)

io.setup(btnPin, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(ledPin, io.OUT)

def mqttInit():
	mqttc.connect("127.0.0.1")
	mqttc.subscribe("examen")
	mqttc.on_message = on_message

def on_message(mqttc, obj, msg):
	try:
		p = msg.payload.decode("utf-8")
		if p == "send":
			file = open(path, "r+")
			if file.mode == 'r+':
				persons = file.read()
				mqttc.publish("examen",  persons)
			file.close()
		return
	except Exception as e:
		print(e)		
			

def btnPress(btnPin):
	global start
	global end
	if io.input(btnPin)==1:
		start=time.time()
	if io.input(btnPin)==0:
		end = time.time()
		elapsed = end - start
		print(elapsed)
	if elapsed<5:
		raise_count()
	else:
		write_count(count, path)

def raise_count():
	global count
	count+=1

def write_count(count, path):
	file = open(path,"r+")
	if file.mode == 'r+':
		file.seek(0)
		file.truncate()
		file.write(count)
		persons = file.read()
		mqttc.publish("examen", persons)
	file.close()
	
def main():
	try:
		mqttInit()
		io.add_event_detect(btnPin, io.BOTH, callback = btnPress, bouncetime=200)
		while(True):
			mqttc.loop()
			io.output(ledPin,True)
	except KeyboardInterrupt:
		print("cleanup program")
	except:
		print("other error occured")
	finally:
		io.cleanup()

if __name__ == "__main__":
	main()
