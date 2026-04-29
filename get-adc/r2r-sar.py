import time
import r2r_adc
import adc_plot

if __name__ == "__main__":
    adc = r2r_adc.R2R_ADC(3.293)

    voltage_values = []
    time_values = []
    duration = 5.0
    try:
        begin = time.time()
        while time.time() - begin < duration:
            voltage_values.append(adc.get_sar_voltage())
            time_values.append(time.time() - begin)
        adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.293)
        adc_plot.plot_sampling_period_hist(time_values)
    finally:
        adc.deinit()