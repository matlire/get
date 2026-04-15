import RPi.GPIO as GPIO
import time

dac_pins      = []
dac_range_max = 3.3
dac_size      = 8

def voltage2number(voltage: float) -> int:
    if (not (0.0 <= voltage <= dac_range_max)):
        printf(f"Voltage is out of range: 0 - {dac_range_max}\nSetting 0.0V")
        return 0
    return int(voltage / dac_range_max * 2**dac_size)

def number2dac(num: int) -> list:
    bits = [int(bit) for bit bit in bin(num)[2:].zfill(dac_size)]
    return bits

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(dac_pins, GPIO.OUT)

def execute():
    try:
        while True:
            try:
                
            except ValueError:
                print("Try again")
    finally:
        GPIO.output(dac_pins, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    init()
    execute()