# importeren van de nodige libraries
import paho.mqtt.client as mqtt

# callback functie voor connect event
def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

# callback functie voor message event
def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

# callback functie voor publish  event
def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

# callback functie voor subscribe event
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
# aanmaken van mqtt client object
mqttc = mqtt.Client()

# toewijzen van callback functies
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

#connect and subscribe
mqttc.connect("localhost")
mqttc.subscribe("house/firstfloor")

# main loop
try:
    while True:
        mqttc.loop()
except KeyboardInterrupt:
    pass

