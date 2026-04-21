import numpy as np
from scipy import signal
import time

def get_sin_wave_ampl(freq: float, time: float) -> float:
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_freq: float) -> float:
    delay = 1/sampling_freq
    time.sleep(delay)
    return delay

def get_triag_wave(freq: float, time: float) -> float:
    return (signal.sawtooth(4* np.pi * freq * time, 0.5) + 1) / 2
