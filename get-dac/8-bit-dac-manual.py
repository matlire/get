import RPi.GPIO as GPIO

dac_pins      = [16, 20, 21, 25, 26, 17, 27, 22]
dac_range_max = 3.3
dac_size      = 8

def voltage2number(voltage: float) -> int:
    if (not (0.0 <= voltage <= dac_range_max)):
        print(f"Voltage is out of range: 0 - {dac_range_max:.2f}\nSetting 0.0V")
        return 0
    return int(voltage / dac_range_max * (2**dac_size - 1))

def number2dac(num: int) -> list:
    bits = [int(bit) for bit in bin(num)[2:].zfill(dac_size)]
    return bits

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac_pins, GPIO.OUT)

def execute():
    try:
        while True:
            try:
                voltage = float(input("Enter number: "))
                number = voltage2number(voltage)
                bits = number2dac(number)
                GPIO.output(dac_pins, bits)
            except ValueError:
                print("You entered Nan. Try again.\n")
    finally:
        GPIO.output(dac_pins, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    init()
    execute()