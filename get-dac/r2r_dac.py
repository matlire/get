import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits: list, dynamic_range: float, verbose: False) -> None:
        self.gpio_bits     = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose       = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number: float) -> list:
        
        bits = [int(bit) for bit in bin(number)[2:].zfill(len(self.gpio_bits))]
        return bits

    def set_voltage(self, voltage: float) -> None:
        if (not (0.0 <= voltage <= self.dynamic_range)):
            print(f"Voltage is out of range: 0 - {self.dynamic_range}\nSetting 0.0V")
            return []
        number = int(voltage / self.dynamic_range * 2**len(self.gpio_bits))

        bits = self.set_number(number)
        GPIO.output(dac_pins, bits)

dac_pins      = [16, 20, 21, 25, 26, 17, 27, 22]
dac_range_max = 3.3

if __name__ == "__main__":
    try:
        dac = R2R_DAC(dac_pins, dac_range_max, True)

        while True:
            try:
                voltage = float(input("Enter number: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("You entered Nan. Try again.\n")
    finally:
        dac.deinit()

