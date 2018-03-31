from math import pi
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


def prompt_for_integer(description):
    while True:
        try:
            return int(input(f"Enter {description}: "))
        except Exception:
            print("Please enter a valid integer.")


def prompt_for_array(description):
    result = []
    while True:
        result_input = input(f"Enter {description}, otherwise hit return: ")
        if result_input == '':
            return result
        try:
            result.append(float(result_input))
        except ValueError:
            print("Please enter a valid float.")


distance_earth_sun = 149.6 * (10**9)
light_v = 3 * 10**8
frequencies = prompt_for_array('frequency')
period = prompt_for_integer('period')
n_of_samples = prompt_for_integer('number of samples')
observer_v = 200000000
source_v = 0
step_size = period / n_of_samples
t = [multiple * step_size for multiple in range(n_of_samples)]


class Wave:
    def __init__(self, frequency):
        self.frequency = frequency
        self.amplitude = 1 / len(frequencies)
        self.function = [
            self.amplitude * np.sin(self.frequency * 2.0 * pi * number)
            for number in t
        ]

    def shift(self, v):
        dopplerfrequency = (1 + v / (3 * 10**8)) * self.frequency
        return Wave(dopplerfrequency)


def waves():
    global originalwave_sum, dopplerwave_sum
    originalwave_sum = [0] * n_of_samples
    dopplerwave_sum = [0] * n_of_samples
    for a, freq in enumerate(frequencies):
        wave = Wave(freq)
        doppler_wave = wave.shift(observer_v - source_v)
        originalwave_sum += np.asarray(wave.function)
        dopplerwave_sum += np.asarray(doppler_wave.function)
    return


def plot():
    plt.figure("FFT Plot")
    plt.title("FFT on Sum of Original Waves and Sum of Doppler Waves")
    x = np.linspace(0.0, 1.0 / (2.0 * step_size), n_of_samples / 2)
    y1 = scipy.fftpack.fft(originalwave_sum)
    y2 = scipy.fftpack.fft(dopplerwave_sum)
    plt.plot(
        x,
        2.0 / n_of_samples * np.abs(y1[:n_of_samples // 2]),
        color="#11b9db",
        label="Original")
    plt.plot(
        x,
        2.0 / n_of_samples * np.abs(y2[:n_of_samples // 2]),
        color="#093987",
        label="Doppler")
    plt.legend(('Original Wave Sum', 'Doppler Wave Sum'))
    plt.show()
    return


waves()
plot()
