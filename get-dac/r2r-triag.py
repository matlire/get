import r2r_dac as r2r
import signal_generator as sg

ampl   = 3.2
freq   = 10
s_freq = 1000

dac_pins      = [16, 20, 21, 25, 26, 17, 27, 22]
dac_range_max = 3.3

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC(dac_pins, dac_range_max, True)
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
