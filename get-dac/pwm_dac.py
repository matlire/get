import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin: int, pwm_freq: float, dynamic_range: float, verbose = False) -> None:
        self.gpio_pin      = gpio_pin
        self.pwm_freq      = pwm_freq
        self.dynamic_range = dynamic_range
        self.verbose       = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)
        self.pwm.start(0)

    def deinit(self) -> None:
        self.pwm.stop()
        GPIO.cleanup()

    def set_duty(self, duty: float) -> None:
        self.pwm.ChangeDutyCycle(duty)

    def set_voltage(self, voltage: float) -> None:
        if (not (0.0 <= voltage <= self.dynamic_range)):
            print(f"Voltage is out of range: 0 - {self.dynamic_range}\nSetting 0.0V")
            return
        duty = voltage / self.dynamic_range * 100
        self.set_duty(duty)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Enter voltage: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("You entered Nan. Try again.\n")
    finally:
        dac.deinit()