import mcp4725_driver as mcp
import signal_generator as sg

ampl   = 3.2
freq   = 10
s_freq = 1000

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(4.95, verbose=False)
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
