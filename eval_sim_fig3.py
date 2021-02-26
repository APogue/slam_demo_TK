import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


plot_color = {
	'gt': [0, 0, 0],
	'dr': [0.0000, 0.5490, 0.3765],
	'opt': [0.8627, 0.2980, 0.2745],
	'em': [0.8471, 0.6824, 0.2784],
	'boem': [0.2633, 0.4475, 0.7086],
	'lmk': [0.1, 0.1490, 0.3765],
}

gt_data = pd.read_csv("result/sim/exp_win_w_time/gt.csv")

# set number of files
num_files = 10
# set the number of realizations
num_realizations = 20

# optimization containers
opt_mc_ave_error = np.zeros((20, 10))
opt_process_time = np.zeros_like(opt_mc_ave_error)
opt_ave_error_array = []
opt_process_time_array = []

# time array corresponding to figure x-axis
time_array = []
for k in range(50, 550, 50):
	opt_time_data = pd.read_csv("result/sim/exp_win_w_time/opt_%s_%s.csv" % (0, k))
	time_array.append(opt_time_data['timestamp'][len(opt_time_data)-1])

# arrays corresponding to average error and processing time across MC
for i in range(num_realizations):
	h = 0
	opt_time_data = pd.read_csv("result/sim/exp_win_w_time/process_time_%s.csv" % (i,))
	opt_process_time[i] = opt_time_data['process_time'].transpose()
	for k in range(50, 550, 50):
		opt_data = pd.read_csv("result/sim/exp_win_w_time/opt_%s_%s.csv" % (i, k))
		opt_error = np.zeros_like(opt_data['p_x'])
		for m in range(len(opt_data['p_x'])):
			opt_error[m] = math.sqrt((gt_data['p_x'][m] - opt_data['p_x'][m]) ** 2 + (gt_data['p_y'][m] - opt_data['p_y'][m]) ** 2 + (gt_data['p_z'][m] - opt_data['p_z'][m]) ** 2)
		opt_mc_ave_error[i, h] = np.mean(opt_error, dtype=np.float64)
		h += 1


opt_ave_error_array.extend(np.mean(opt_mc_ave_error, axis=0, dtype=np.float64))
opt_process_time_array.extend(np.mean(opt_process_time, axis=0, dtype=np.float64))

print('error',opt_ave_error_array)
print('process_time',opt_process_time_array)
print('time', time_array)



fig, (ax1, ax2) = plt.subplots(2)
fig_width = 5.84
fig_height = 4.38
fig.set_size_inches(fig_width, fig_height)
line_width = 1.2

ax1.plot(time_array, opt_ave_error_array, color = plot_color['opt'], linewidth=line_width, label='opt.')

ax1.set(ylabel='ave error [m]')
ax1.set_ylim(0.0, .5)
ax1.legend(loc = 1)


ax2.plot(time_array, opt_process_time_array, color = plot_color['opt'], linewidth=line_width, label='opt.')

ax2.set(ylabel='process time [s]')
ax2.set(xlabel='time [s]')
ax2.set_ylim(0.0, 20)
plt.show()