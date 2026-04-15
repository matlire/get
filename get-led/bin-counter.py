import RPi.GPIO as GPIO
import time

leds        = [24, 22, 23, 27, 17, 25, 12, 16]
button_up   = 9
button_down = 10
delay       = 0.2
num         = 0

def dec2bin(value: int) -> list:
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def clamp(value: int, min_value: int, max_value: int) -> int:
    return max(min_value, min(value, max_value))

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_up, GPIO.IN)
    GPIO.setup(button_down, GPIO.IN)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, 0)

def execute():
    global button_up, button_down, num
    dir = 0
    while True:
        if(GPIO.input(button_up)):
            dir = 1
        elif(GPIO.input(button_down)):
            dir = -1
        num = clamp(num + dir, 0, 255)
        dir = 0
        if num == 255: num = 0
        print(num, dec2bin(num))
        time.sleep(delay)
        GPIO.output(leds, dec2bin(num))

if __name__ == "__main__":
    init()
    execute()
