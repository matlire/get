import pwm_dac
import signal_generator as sg

ampl   = 3.2
freq   = 10
s_freq = 1000

if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(12, 5000, 3.290, True)
        tm = 0

        while True:
            try:
                voltage = ampl * sg.get_triag_wave(freq, tm)
                dac.set_voltage(voltage)
                tm += sg.wait_for_sampling_period(s_freq)
            except ValueError:
                print("You entered Nan. Try again.\n")
    finally:
        dac.deinit()
