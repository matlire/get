import RPi.GPIO as GPIO
import time

led    = 26
period = 1.0

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

def execute():
    state  = 0
    while True:
        GPIO.output(led, state)
        state = not state
        time.sleep(period)

if __name__ == "__main__":
    init()
    execute()
