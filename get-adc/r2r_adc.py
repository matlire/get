import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.001, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose       = verbose
        self.compare_time  = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for value in range(2**8):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return value
        return 255

    def get_sc_voltage(self):
        return (self.sequential_counting_adc() / 255) * self.dynamic_range

    def successive_approximation_adc(self):
        value = 0
        for i in range(7, -1, -1):
            test_value = value | (1 << i)
        
            self.number_to_dac(test_value)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                value = test_value
        return value

    def get_sar_voltage(self):
        return (self.successive_approximation_adc() / 2**8) * self.dynamic_range

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.293)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Out voltage (sc): {voltage:.3f} В")

            voltage = adc.get_sar_voltage()
            print(f"Out voltage (sar): {voltage:.3f} В")
            
            time.sleep(0.5)   
    finally:
        adc.deinit()