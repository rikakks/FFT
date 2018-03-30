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


pi = 3.1415926535897932
distance_earth_sun = 149.6 * (10**9)
light_v = 3 * 10**8
frequency = prompt_for_array('frequency')
period = prompt_for_integer('period')
n_of_samples = prompt_for_integer('number of samples')
observer_v = 2.0
source_v = 0
step_size = period / n_of_samples
t = [multiple * step_size for multiple in range(n_of_samples)]


class Wave:
    def __init__(self, originalfrequency):
        self.originalfrequency = originalfrequency
        self.period = period
        self.amplitude = 1 / len(frequency)
        self.function = [
            self.amplitude * np.sin(self.originalfrequency * 2.0 * pi * number)
            for number in t
        ]
        self.dopplerfrequency = (1 + (observer_v - source_v) /
                                 (3 * 10**8)) * self.originalfrequency
        self.dopplerfunction = [
            self.amplitude * np.sin(self.dopplerfrequency * number)
            for number in t
        ]


def waves():
    global originalwave_sum, dopplerwave_sum
    originalwaves = {}
    dopplerwaves = {}
    originalwave_sum = [0] * n_of_samples
    dopplerwave_sum = [0] * n_of_samples
    for a, freq in enumerate(frequency):
        wave = Wave(freq)
        originalwave_sum += np.asarray(wave.function)
        dopplerwave_sum += np.asarray(wave.dopplerfunction)
        originalwaves["wave_{}".format(a)] = wave
        dopplerwaves["wave_{}".format(a)] = wave
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
