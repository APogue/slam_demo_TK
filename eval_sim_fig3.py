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
fig = plt.figure(3)


# set number of points per file
num_traj = 10
# set the number of realizations
num_realizations = 20
est_opt_pt = np.zeros(num_traj)
traj_len = range(50, 500, 50)

gt_data = pd.read_csv("result/sim/exp_win_w_time/gt.csv")
mc_ave_error = np.zeros((20, 10))
process_time = np.zeros_like(mc_ave_error)
ave_error = []
process_time_array = []
time_array = []
for i in range(num_realizations):
	h = 0
	opt_time_data = pd.read_csv("result/sim/exp_win_w_time/process_time_%s.csv" % (i,))
	process_time[i] = opt_time_data['process_time'].transpose()
	for k in range(50, 550, 50):
		opt_data = pd.read_csv("result/sim/exp_win_w_time/opt_%s_%s.csv" % (i, k))
		opt_error = np.zeros_like(opt_data['p_x'])
		for m in range(len(opt_data['p_x'])):
			opt_error[m] = math.sqrt((gt_data['p_x'][m] - opt_data['p_x'][m]) ** 2 + (gt_data['p_y'][m] - opt_data['p_y'][m]) ** 2 + (gt_data['p_z'][m] - opt_data['p_z'][m]) ** 2)
		mc_ave_error[i, h] = np.mean(opt_error, dtype=np.float64)
		h += 1

for k in range(50, 550, 50):
	opt_time_data = pd.read_csv("result/sim/exp_win_w_time/opt_%s_%s.csv" % (0, k))
	time_array.append(opt_time_data['timestamp'][len(opt_time_data)-1])


ave_error.extend(np.mean(mc_ave_error, axis=0, dtype=np.float64))

process_time_array.extend(np.mean(process_time, axis=0, dtype=np.float64))
print('error',ave_error)
print('process_time',process_time_array)
print('time', time_array)



fig, (ax1, ax2) = plt.subplots(2)
fig_width = 5.84
fig_height = 4.38
fig.set_size_inches(fig_width, fig_height)
line_width = 1.2

ax1.plot(time_array, ave_error, color = plot_color['opt'], linewidth=line_width, label='opt.')

ax1.set(ylabel='ave error [m]')
ax1.set_ylim(0.0, .5)
ax1.legend(loc = 1)


ax2.plot(time_array, process_time_array, color = plot_color['opt'], linewidth=line_width, label='opt.')

ax2.set(ylabel='process time [s]')
ax2.set(xlabel='time [s]')
ax2.set_ylim(0.0, 20)
plt.show()