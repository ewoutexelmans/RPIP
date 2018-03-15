import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

led = 4
button = [17, 27, 22]

index = 0

guess = []
key = [1, 2, 3, 1, 2]

burn = False

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def print_name(x, index):
    print("Button {} pressed".format(x))
    guess.insert(x, index)
    if guess == key:
        print("You guessed correctly")
        return True
    else:
        return False

try:
    print("Press the buttons in the correct sequence to make the led burn")
    while not burn:

        if count > 4:
            index = 0

        if GPIO.input(button[0]):
            x = 1
            burn = print_name(x)
            index += 1
        elif GPIO.input(button[1]):
            x = 2
            burn = print_name(x)
            index += 1
        elif GPIO.input(button[2]):
            x = 3
            burn = print_name(x)
            index += 1
        time.sleep(0.3)
    else:
        GPIO.output(led, burn)
        time.sleep(2)


except KeyboardInterrupt:
    print("Keyboard interrupt, exiting script")

except:
    print("Other error or exception occured!")

finally:
    print("Cleanup resources")
    GPIO.cleanup()
