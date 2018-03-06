import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

pi = 3.14159265359  #using np.pi causes floating point accuracy error, so we will use a float
sin = np.sin
frequency = [
    5,
    0.5,
    1.0,
]
period = 50
n_of_samples = 20000
step_size = period / n_of_samples
t = []

for multiple in range(n_of_samples):
    t.append(multiple * step_size)


class Wave:
    def __init__(self):
        pass

    def frequency(self, n):
        self.frequency = frequency[n]

    def period(self):
        self.period = period

    def amplitude(self):
        self.amplitude = 1 / len(frequency)

    def function(self):
        self.function = []
        for number in t:
            self.function.append(
                self.amplitude * sin(self.frequency * 2 * pi * number))


waves = {}
a = 0
wave_sum = []
while a < len(frequency):
    wave_a = "wave_{}".format(a)
    waves[wave_a] = Wave()
    waves[wave_a].frequency(a)
    waves[wave_a].period()
    waves[wave_a].amplitude()
    waves[wave_a].function()
    wave_sum += waves[wave_a].function
    a += 1

#plot
yf = scipy.fftpack.fft(wave_sum)
xf = np.linspace(0.0, 1.0 / (2.0 * step_size), n_of_samples / 2)
plt.figure(3)
plt.plot(xf, 2.0 / n_of_samples * np.abs(yf[:n_of_samples // 2]))
plt.show()

print(aaaaa)
plt.figure(1)
plt.clf()
plt.plot(t, f)
plt.title(r'Sin function with frequency w = ' + str(w))
plt.xlabel('time')
plt.ylabel(r'sin(wt)')
plt.show()

################################
################################
################################

# DOPPLER EFFECT

# We asume it is a circular orbit with constant speed

R = 149.6 * (10**9)  #earth-sun distance in meters

c = 3 * (10**8)  #light speed in meters/seconds

t = np.arange(0, T, 1)  #time array

#np.savetxt(
#    "dopplertime.csv", t, header="Doppler time array data: ", delimiter=",")

v_earth = 2 * pi * R / T
v_y_earth = v_earth * np.sin(2 * pi * t / T)
print()
print(v_earth)

v_source = 0  #-275000 #velocity of the source in m/s
w_wave = w

# w_doppler = (1+(v_y_earth-v_source)/c)*w_wave
w_doppler = (1 + (v_y_earth - v_source) / (3 * 10**8)) * w_wave
print(max(w_doppler))
f = np.sin(w_doppler * t)  #function array

#np.savetxt(
#    "dopplerfunction.csv",
#    header="Doppler function array data: ",
#    delimiter=",")

plt.figure(2)
plt.clf()
plt.plot(t, f)
plt.title(r'Sin function with doppler frequency')
plt.xlabel('time')
plt.ylabel(r'sin(w(t)t)')
plt.show()

print(len(f))
print(len(t))
