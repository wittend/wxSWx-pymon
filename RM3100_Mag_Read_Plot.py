#============================================================================================
# RM3100_MagReadPlot.py
# 
# This routine reads ascii file data from HamSCI DASI magnetometers (RM3100) and plot graphs. 
# 
# Hyomin Kim, New Jersey Institute of Technology, hmkim@njit.edu 
# 02/01/2021
#============================================================================================
from matplotlib.pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.dates as mdate
import sys
from datetime import date
import datetime
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from moving_average import *
import csv
import bisect
#from Ground_FGM_Subroutines import *
#from DataRead_Kim import generate_datestrings


# ===== Input Parameters ========================================================
date = '2021/01/16'
t_start = '00:00:00'
t_stop = '23:59:59'
station_code = 'YOUR STATION CODE'
data_dir = 'YOUR DIRECTORY WHERE DATA FILES ARE LOCATED'
plot_dir = 'YOUR DIRECTORY WHERE GENERATED PLOTS WILL BE SAVED'
# ============================================================================


year = date[0:4]
month = date[5:7]
day = date[8:10]
hour_start = t_start[0:2]
minute_start = t_start[3:5]
second_start = t_start[6:8]
hour_stop = t_stop[0:2]
minute_stop = t_stop[3:5]
second_stop = t_stop[6:8]
date_time = datetime.datetime(int(year), int(month), int(day), int(hour_start), int(minute_start), int(second_start))
doy = date_time.timetuple().tm_yday
filename = station_code + '-' + year+month+day + '-runmag.log'
f=open(data_dir+filename)
header_index = 0
csv_f = csv.reader(f, delimiter=",")
fgm_data = []
for row in csv_f:
    fgm_data.append(row)
date_time_array = np.array([year+'-'+month+'-'+day + ' ' + fgm_data[i][0][19:27] for i in range(header_index, len(fgm_data))])
pattern = '%Y-%m-%d %H:%M:%S'
epoch_temp = np.array([datetime.datetime.strptime(x, pattern) for x in date_time_array])
Bx_temp = np.array([float(fgm_data[i][3][4:11]) for i in range(header_index, len(fgm_data))])
By_temp = np.array([float(fgm_data[i][4][4:11]) for i in range(header_index, len(fgm_data))])
Bz_temp = np.array([float(fgm_data[i][5][4:11]) for i in range(header_index, len(fgm_data))])
#Array slicing/indexing
start = datetime.datetime(int(year), int(month), int(day), int(hour_start), int(minute_start), int(second_start))
stop = datetime.datetime(int(year), int(month), int(day), int(hour_stop), int(minute_stop), int(second_stop))
start_index = bisect.bisect_left(epoch_temp, start)
stop_index = bisect.bisect_left(epoch_temp, stop)
Epoch = epoch_temp[start_index:stop_index]
Bx = 1000*Bx_temp[start_index:stop_index]  #*1000: uT to nT
By = 1000*By_temp[start_index:stop_index]
Bz = 1000*Bz_temp[start_index:stop_index]


# Specify date_str/time range for x-axis range
ep_start = datetime.datetime(int(year), int(month), int(day), int(hour_start), int(minute_start), int(second_start))
ep_stop = datetime.datetime(int(year), int(month), int(day), int(hour_stop), int(minute_stop), int(second_stop))


#This is for Pi magnetometer (PNI)
Bx[np.where(Bx[:] >= 999999.0)] = np.nan
By[np.where(By[:] >= 999999.0)] = np.nan
Bz[np.where(Bz[:] >= 999999.0)] = np.nan


#Moving average
N = 10 #WindowWidth in sec
Bx = np.array(moving_average(Bx, N))
By = np.array(moving_average(By, N))
Bz = np.array(moving_average(Bz, N))
Epoch = np.array(Epoch[0:len(Bx)])  #to match the new array size with the moving averaged array. 
Bt = np.sqrt(Bx**2+By**2+Bz**2)


# Plot graph
fig = plt.figure(1, figsize=(6, 8))  #Plot window size
               
# Graph 1
ax1 = fig.add_subplot(411)
box = ax1.get_position()
plt.subplots_adjust(left=box.x0, right=box.x1-0.08, top=box.y1, bottom=0.1, hspace=0.1)
ax1.plot(Epoch, Bx, label='Bx', linewidth=0.5)
ax1.set_xlim([ep_start, ep_stop]) #without this, the time range will not show up properly because there are missing data.
title = station_code + ' HamSCI Mag '  + date + ' ' + t_start + ' - ' + t_stop
ax1.set_title(title)
ax1.set_ylabel('Bx (nT)')
ax1.get_xaxis().set_ticklabels([])
ax1.tick_params(axis='x', direction='out', top='on')
ax1.tick_params(axis='y', direction='out', right='on')
ax1.minorticks_on()
ax1.tick_params(axis='x', which ='minor', direction='out', top='on')
ax1.tick_params(axis='y', which ='minor', direction='out', right='on')
ax1.set_ylim(47600, 47800)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax2 = fig.add_subplot(412)
ax2.plot(Epoch, By, label='By', linewidth=0.5)
ax2.set_xlim([ep_start, ep_stop]) #without this, the time range will not show up properly because there are missing data.
ax2.set_ylabel('By (nT)')
ax2.get_xaxis().set_ticklabels([])
ax2.tick_params(axis='x', direction='out', top='on')
ax2.tick_params(axis='y', direction='out', right='on')
ax2.minorticks_on()
ax2.tick_params(axis='x', which ='minor', direction='out', top='on')
ax2.tick_params(axis='y', which ='minor', direction='out', right='on')
ax2.set_ylim(-100, 100)
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax3 = fig.add_subplot(413)
ax3.plot(Epoch, Bz, label='Bz', linewidth=0.5)
ax3.set_xlim([ep_start, ep_stop]) #without this, the time range will not show up properly because there are missing data.
ax3.set_ylabel('Bz (nT)')
ax3.get_xaxis().set_ticklabels([])
ax3.tick_params(axis='x', direction='out', top='on')
ax3.tick_params(axis='y', direction='out', right='on')
ax3.minorticks_on()
ax3.tick_params(axis='x', which ='minor', direction='out', top='on')
ax3.tick_params(axis='y', which ='minor', direction='out', right='on')
ax3.set_ylim(-15400, -15200)
ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

ax4 = fig.add_subplot(414)
ax4.plot(Epoch, Bt, label='Bt', linewidth=0.5)
ax4.set_xlim([ep_start, ep_stop]) #without this, the time range will not show up properly because there are missing data.
ax4.set_ylabel('Bt (nT)')
ax4.get_xaxis().set_ticklabels([])
ax4.tick_params(axis='x', direction='out', top='on')
ax4.tick_params(axis='y', direction='out', right='on')
ax4.minorticks_on()
ax4.tick_params(axis='x', which ='minor', direction='out', top='on')
ax4.tick_params(axis='y', which ='minor', direction='out', right='on')
ax4.set_ylim(50000, 50200)
ax4.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

   
# X-axis
ax4.set_xlabel('UT (hh:mm)')
date_fmt = '%H:%M'  #'%d-%m-%y %H:%M:%S'  #Choose your xtick format string
date_formatter = mdate.DateFormatter(date_fmt)
ax4.xaxis.set_major_formatter(date_formatter)
 

# ====== Save figure
t_start_str = t_start[0:2] + t_start[3:5]
t_stop_str = t_stop[0:2] + t_stop[3:5]
filename_plot = station_code + '_' + year+month+day + '_' + t_start_str + '_' + t_stop_str + '_MovingAve.jpg'
plt.savefig(plot_dir + filename_plot, format='jpg', bbox_inches='tight', dpi=600)
plt.close()
