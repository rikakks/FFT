import numpy as np
import matplotlib.pyplot as plt
import readligo as rl

#----------------------------------------------------------------
# Load all LIGO data from a single file
#----------------------------------------------------------------
strain, time, chan_dict = rl.loaddata(
                          'H-H1_LOSC_4_V1-815411200-4096.hdf5', 'H1')

start = 842656000
stop =  842670000
segList = rl.getsegs(start, stop, 'H1', flag='CBCLOW_CAT2')

#-------------------------------------------
# Plot a few seconds of each "good" segment
#-------------------------------------------
N = 10000
for (begin, end) in segList:
    # -- Use the getstrain() method to load the data
    strain, meta, dq = rl.getstrain(begin, end, 'H1')

    # -- Make a plot
    plt.figure()
    ts = meta['dt']
    rel_time = np.arange(0, end-begin, meta['dt'])
    plt.plot(rel_time[0:N], strain[0:N])
    plt.xlabel('Seconds since GPS ' + str(begin) )
plt.show()
