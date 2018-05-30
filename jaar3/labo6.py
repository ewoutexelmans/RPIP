
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import readchar
import time

GPIO.setmode(GPIO.BCM)

buttons = [2,3]
led=12

dc = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_UP)

pwm = GPIO.PWM(led, 50)
pwm.start(dc)

def button_press(channel):
    s="test"
    if channel == buttons[0]:
        s= "VAR=UP;NAAM=EWOUT"
    if channel == buttons[1]:
        s="VAR=DN;NAAM=EWOUT"
    (rc, mid)=client.publish("testtopic/apLab6/raspklas", s, qos=1)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("testtopic/apLab6/raspklas")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " +str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    global dc
    s=str(msg.payload)
    print(s)
    if "UP;" in s and dc < 100:
        dc+=10
    if "DN;" in s and dc > 0:
        dc-=10
    pwm.ChangeDutyCycle(dc)

def on_publish(client, userdata, mid):
    print("mid "+str(mid))

def on_unsubscribe(client, userdata, mid):
    print("Unsubscribed: "+str(mid))

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

client = mqtt.Client(client_id="clientId-vJ81zLpUgq")

client.on_connect=on_connect
client.on_publish=on_publish
client.on_subscribe=on_subscribe
client.on_message=on_message
client.on_unsubscribe=on_unsubscribe
client.on_disconnect=on_disconnect

client.connect("broker.mqttdashboard.com", 1883)

GPIO.add_event_detect(buttons[0],GPIO.FALLING, callback =button_press,bouncetime = 500)
GPIO.add_event_detect(buttons[1],GPIO.FALLING, callback =button_press, bouncetime = 500)

print("\n===========================\n== Program is running =====\n== End by pressing ENTER ==\n===========================\n")

client.loop_start()

while readchar.readkey()!=readchar.key.ENTER:
    pass

client.unsubscribe("testtopic/apLab6/raspklas")
client.disconnect()
client.loop_stop()


print("Cleanup and shutting down program")
GPIO.remove_event_detect(buttons[0])
GPIO.remove_event_detect(buttons[1])
GPIO.cleanup()
