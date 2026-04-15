import RPi.GPIO as GPIO
import time

led      = 26
photoreg = 6
period   = 0.01

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(photoreg, GPIO.IN)

def execute():
    while True:
        GPIO.output(led, not GPIO.input(photoreg))
        time.sleep(period)

if __name__ == "__main__":
    init()
    execute()
