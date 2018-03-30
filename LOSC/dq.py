import numpy as np
import matplotlib.pyplot as plt
import h5py

filename = 'DATA/H-H1_LOSC_4_V1-815411200-4096.hdf5'
dataFile = h5py.File(filename, 'r')
gpsStart = dataFile['meta']['GPSstart'].value

dqInfo = dataFile['quality']['simple']
bitnameList = dqInfo['DQShortnames'].value
nbits = len(bitnameList)

for bit in range(nbits):
    print(bit, bitnameList[bit])

qmask = dqInfo['DQmask'].value

sci = (qmask >> 0) & 1
burst1 = (qmask >> 9) & 1

goodData_1hz = sci & burst1

plt.plot(goodData_1hz + 4, label='Good_Data')
plt.plot(burst1 + 2, label='BURST_CAT1')
plt.plot(sci, label='DATA')
plt.axis([0, 4096, -1, 8])
plt.legend(loc=1)
plt.xlabel('Time (s)')
plt.show()

dummy = np.zeros(goodData_1hz.shape)
masked_dummy = np.ma.masked_array(dummy, np.logical_not(goodData_1hz))
segments = np.ma.flatnotmasked_contiguous(masked_dummy)
segList = [(int(seg.start + gpsStart), int(seg.stop + gpsStart))
           for seg in segments]
