import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import LombScargle
import scipy.fftpack

# FIXED FREQUENCY
w = 5  #frequency in Hz
T = 50  # 365 * 12 * 24 * 60 #* 60  #period in seconds
N = 2000  #number of samples
t = np.linspace(0, T, N)  #time array
amps = [.5, 1.0]
print(len(t))
sa_sp = T / N
print(sa_sp)
#np.savetxt("fixedtime.csv", t, header="Fixed time array data: ", delimiter=",")

f = .5 * np.sin(w * 2.0 * np.pi * t)  #function array

w2 = .5
f2 = np.sin(w2 * 2.0 * np.pi * t)

f_sum = f + f2
#np.savetxt(
#    "fixedfunction.csv",
#    f,
#    delimiter=",")

#plot
yf = scipy.fftpack.fft(f_sum)
xf = np.linspace(0.0, 1.0 / (2.0 * sa_sp), N / 2)
plt.figure(3)
plt.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
plt.show()

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

v_earth = 2 * np.pi * R / T
v_y_earth = v_earth * np.sin(2 * np.pi * t / T)
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
