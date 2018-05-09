import readchar
import pigpio


pin1 = 12
pin2 = 18

freq = 100
dc = 100000



pwm1 = pigpio.pi()
pwm2 = pigpio.pi()
pwm1.hardware_PWM(pin1, freq, dc)
pwm2.hardware_PWM(pin2, freq, dc)



while readchar.readkey() != readchar.key.ENTER:
    if readchar.readkey()=='a':
        freq = 100
        print(freq)
    if readchar.readkey()=='z':
        freq = 1000
        print(freq)
    if readchar.readkey()=='e':
        freq = 5000
        print(freq)
    if readchar.readkey()=='r':
        freq = 10000
        print(freq)
    if readchar.readkey()=='t':
        freq = 100000
        print(freq)
    if readchar.readkey()=='y':
        freq = 5000000
        print(freq)
    if readchar.readkey()=='q':
        dc = 100000
        print(dc)
    if readchar.readkey()=='s':
        dc = 500000
        print(dc)
    pwm1.hardware_PWM(pin1, freq, dc)
    pwm2.hardware_PWM(pin2, freq, dc)



print("Cleanup and shutting down program")
