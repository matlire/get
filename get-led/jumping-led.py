import RPi.GPIO as GPIO
import time

leds   = [24, 22, 23, 27, 17, 25, 12, 16]
period = 0.2

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, 0)

def execute():
    while True:
        for i in leds:
            GPIO.output(i, 1)
            time.sleep(period)
            GPIO.output(i, 0)
        for i in reversed(leds):
            GPIO.output(i, 1)
            time.sleep(period)
            GPIO.output(i, 0)

if __name__ == "__main__":
    init()
    execute()
