import RPi.GPIO as GPIO
import time

led    = 26
button = 13
delay  = 0.2

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(button, GPIO.IN)

def execute():
    state  = 0
    while True:
        if GPIO.input(button):
            state = not state
            GPIO.output(led, state)
            time.sleep(delay)

if __name__ == "__main__":
    init()
    execute()
