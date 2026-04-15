import RPi.GPIO as GPIO
import time

led      = 26
period   = 0.01
duty     = 0.0

def init():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    pwm = GPIO.PWM(led, 200)
    pwm.start(duty)

def execute():
    global duty
    while True:
        pwm.ChangeDutyCycle(duty)
        time.sleep(period)
        duty += 1
        if duty >= 100:
            duty = 0

if __name__ == "__main__":
    init()
    execute()
