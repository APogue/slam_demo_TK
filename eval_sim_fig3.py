import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig_width = 5.84
fig_height = 4.38
plot_color = {
	'gt': [0, 0, 0],
	'dr': [0.0000, 0.5490, 0.3765],
	'opt': [0.8627, 0.2980, 0.2745],
	'em': [0.8471, 0.6824, 0.2784],
	'boem': [0.2633, 0.4475, 0.7086],
	'lmk': [0.1, 0.1490, 0.3765],
}
fig = plt.figure(3)
fig.set_size_inches(fig_width, fig_height)
line_width = 1.5
# set number of points per file
num_traj = 10
est_opt_pt = np.zeros(num_traj)
est_em_pt = np.zeros(num_traj)
est_boem_pt = np.zeros(num_traj)
traj_len = range(100,600,50)
# set the number of realizations
num_realizations = 20
for i in range(len(est_opt_pt)):
	est_opt_time_list = []
	est_em_time_list = []
	est_boem_time_list = []
	for k in range(0,num_realizations):
		est_opt_data = pd.read_csv("result/sim/vis/opt_time_%s.csv" %k)
		est_em_data = pd.read_csv("result/sim/vis/em_time_%s.csv" %k)
		est_boem_data = pd.read_csv("result/sim/vis/boem_time_%s.csv" %k)
		est_opt_time_list.append(est_opt_data["process_time"][i])
		est_em_time_list.append(est_em_data["process_time"][i])
		est_boem_time_list.append(est_boem_data["process_time"][i])
	est_opt_pt[i] = (sum(est_opt_time_list)/len(est_opt_time_list))
	est_em_pt[i] = (sum(est_em_time_list)/len(est_em_time_list))
	est_boem_pt[i] = (sum(est_boem_time_list)/len(est_boem_time_list))


plt.plot(traj_len, est_opt_pt, color = plot_color['opt'], linewidth=line_width, label='opt.')
plt.plot(traj_len, est_em_pt, color = plot_color['em'], linewidth=line_width, label='EM')
plt.plot(traj_len, est_boem_pt, color = plot_color['boem'], linewidth=line_width, label='BOEM')

plt.legend()

plt.xlabel('trajectory length [max index]')
plt.ylabel('time [s]')
# plt.ylim([0,1.31])

plt.show()