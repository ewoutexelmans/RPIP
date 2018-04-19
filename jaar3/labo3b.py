import random
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buttons=[2,3]
led=4

GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

score_a = 0
score_b = 0
turn = 0
check = True

def check_player(channel):
    if channel == buttons[0]:
        print("player a pressed the button first")
        global score_a
        score_a+=1
    else:
        print("player b pressed the button first")
        global score_b
        score_b+=1

GPIO.add_event_detect(buttons[0],GPIO.FALLING,callback = check_player, bouncetime = 300)
GPIO.add_event_detect(buttons[1],GPIO.FALLING, callback = check_player, bouncetime = 300)

while turn<10:
    x = random.randint(10,41)/10
    time.sleep(x)
    check = True
    while check:
        GPIO.output(led,GPIO.HIGH)
        if GPIO.event_detected(buttons[0]) or GPIO.event_detected(buttons[1]):
            GPIO.output(led, GPIO.LOW)
            check = False
    turn+=1

if score_a>score_b:
    print("player a won")
elif score_a==score_b:
    print("draw")
else:
    print("player b won")
print("score player a: ",score_a)
print("score player b: ",score_b)

time.sleep(1)

print("Cleanup and shutting down program")
GPIO.remove_event_detect(buttons[0])
GPIO.remove_event_detect(buttons[1])
GPIO.cleanup()

