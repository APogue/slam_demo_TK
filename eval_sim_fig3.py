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
ave_error = []
mc_ave_error = np.zeros((20, 10))
for i in range(num_realizations):
	h = 0
	for k in range(50, 550, 50):
		opt_data = pd.read_csv("result/sim/exp_win_w_time/opt_%s_%s.csv" % (i, k))
		opt_error = np.zeros_like(opt_data['p_x'])
		for m in range(len(opt_data['p_x'])):
			opt_error[m] = math.sqrt((gt_data['p_x'][m] - opt_data['p_x'][m]) ** 2 + (gt_data['p_y'][m] - opt_data['p_y'][m]) ** 2 + (gt_data['p_z'][m] - opt_data['p_z'][m]) ** 2)
		mc_ave_error[i, h] = np.mean(opt_error, dtype=np.float64)
		h += 1

ave_error.extend(np.mean(mc_ave_error, axis=0, dtype=np.float64))

print(ave_error)


#
#
# for i in range(len(est_opt_pt)):
# 	est_opt_time_list = []
# 	est_em_time_list = []
# 	est_boem_time_list = []
# 	for k in range(0,num_realizations):
# 		est_opt_data = pd.read_csv("result/sim/vis/opt_time_%s.csv" %k)
# 		est_em_data = pd.read_csv("result/sim/vis/em_time_%s.csv" %k)
# 		est_boem_data = pd.read_csv("result/sim/vis/boem_time_%s.csv" %k)
# 		est_opt_time_list.append(est_opt_data["process_time"][i])
# 		est_em_time_list.append(est_em_data["process_time"][i])
# 		est_boem_time_list.append(est_boem_data["process_time"][i])
# 	est_opt_pt[i] = (sum(est_opt_time_list)/len(est_opt_time_list))
# 	est_em_pt[i] = (sum(est_em_time_list)/len(est_em_time_list))
# 	est_boem_pt[i] = (sum(est_boem_time_list)/len(est_boem_time_list))
#
#
#
# fig, (ax1, ax2) = plt.subplots(2)
# fig_width = 5.84
# fig_height = 4.38
# fig.set_size_inches(fig_width, fig_height)
# line_width = 1.2
#
# plt.plot(traj_len, est_opt_pt, color = plot_color['opt'], linewidth=line_width, label='opt.')
# plt.plot(traj_len, est_em_pt, color = plot_color['em'], linewidth=line_width, label='EM')
# plt.plot(traj_len, est_boem_pt, color = plot_color['boem'], linewidth=line_width, label='BOEM')
#
# plt.legend()
#
# plt.xlabel('trajectory length [max index]')
# plt.ylabel('time [s]')
# # plt.ylim([0,1.31])
#
# plt.show()