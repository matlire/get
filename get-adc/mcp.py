import time
import mcp3021_driver as MCP
import adc_plot

if __name__ == "__main__":
    mcp = MCP.MCP3021(5.217)

    voltage_values = []
    time_values = []
    duration = 5.0
    try:
        begin = time.time()
        while time.time() - begin < duration:
            voltage_values.append(mcp.get_voltage())
            time_values.append(time.time() - begin)
        adc_plot.plot_voltage_vs_time(time_values, voltage_values, 5.217)
        adc_plot.plot_sampling_period_hist(time_values)
    finally:
        mcp.deinit()