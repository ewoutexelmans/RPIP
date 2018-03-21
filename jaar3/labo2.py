import urllib.request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = [2,3,4,17,27,22,10,9,11]
GPIO.setup(led, GPIO.OUT)

url = 'https://darksky.net/forecast/51.2211,4.3997/ca12/nl'
webpagina = urllib.request.urlopen(url)
html_data = webpagina.read()
webpagina.close()

html_string = str(html_data)
index = html_string.find("summary swap\">")+14
temp = int(html_string[index])

if temp<0:
    GPIO.output(led[0],True)
elif temp<5:
    GPIO.output(led[1],True)
elif temp<10:
    GPIO.output(led[2],True)
elif temp<15:
    GPIO.output(led[3],True)
elif temp<20:
    GPIO.output(led[4],True)
elif temp<25:
    GPIO.output(led[5],True)
elif temp<30:
    GPIO.output(led[6],True)
elif temp<35:
    GPIO.output(led[7],True)
elif temp>=35:
    GPIO.output(led[8],True)
else:
    print("Can't find the local temperature.")

time.sleep(1)
print("Cleanup and shutting down program")
GPIO.cleanup()

