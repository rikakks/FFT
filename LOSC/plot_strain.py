#----------------------
# Import needed modules
#----------------------
import numpy as np
import matplotlib.pyplot as plt
import h5py

#-------------------------
# Open the File
#-------------------------
fileName = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
dataFile = h5py.File(fileName, 'r')

#----------------------
# Explore the file
#----------------------
for key in dataFile.keys():
    print(key)

#---------------------
# Read in strain data
#---------------------
strain = dataFile['strain']['Strain'].value
ts = dataFile['strain']['Strain'].attrs['Xspacing']

#-----------------------
# Print out some meta data
#-----------------------
print("\n\n")
metaKeys = dataFile['meta'].keys()
meta = dataFile['meta']
for key in metaKeys:
    print(key, meta[key].value)

#---------------------------
# Create a time vector
#---------------------------
gpsStart = meta['GPSstart'].value
duration = meta['Duration'].value
gpsEnd   = gpsStart + duration

time = np.arange(gpsStart, gpsEnd, ts)

#----------------------
# Plot the time series
#----------------------
numSamples = 10000
plt.plot(time[0:numSamples], strain[0:numSamples])
plt.xlabel('GPS Time (s)')
plt.ylabel('H1 Strain')
plt.show()
