import pigpio
import time


pinPWM = 12

pwm = pigpio.pi()

def play_note(input):
    tone = input[0]
    length = input[1]
    if tone =='A':
        freq = 440
    elif tone =='B':
        freq = 494
    elif tone =='C':
        freq = 262
    elif tone =='D':
        freq = 294
    elif tone =='E':
        freq = 330
    elif tone =='F':
        freq = 349
    elif tone =='G':
        freq = 392
    else:
        print("tone not found")
    if length == '0':
        hold = 4
    elif length == '1':
        hold = 2
    elif length == '2':
        hold = 1
    elif length == '3':
        hold = 0.5
    elif length == '4':
        hold = 0.25
    else:
        print("length not found")
    pwm.hardware_PWM(pinPWM, freq, 500000)
    time.sleep(hold)

try:
    file = open(music, "r")
    for line in file:
        play_note(line)
    file.close()


pwm2.hardware_PWM(pin2, freq, dc)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You don't have permission to read this file")

except:
    print("Error while reading file")

finally:
    print("Cleanup and shutting down program")
