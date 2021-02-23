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


fig_width = 5.84
fig_height = 4.38

# keyframe has larger time range than ground truth


gt_data = pd.read_csv("result/sim/vis/gt.csv")

gt_traj_len = []
for i in range(len(gt_data['p_x'])-1):
	gt_traj_len.append(math.sqrt((gt_data['p_x'][i]-gt_data['p_x'][i+1])**2+ (gt_data['p_y'][i]-gt_data['p_y'][i+1])**2+ (gt_data['p_z'][i]-gt_data['p_z'][i+1])**2))

print('the trajectory length is ', sum(gt_traj_len))

dr_data = pd.read_csv("result/sim/vis/dr_6.csv")
est_opt_data = pd.read_csv("result/sim/vis/opt_6.csv")
est_em_data = pd.read_csv("result/sim/vis/em_6.csv")
est_boem_data = pd.read_csv("result/sim/vis/boem_6.csv")
lmk_data = pd.read_csv("result/sim/vis/lmk.csv")


fig = plt.figure(1)
fig.set_size_inches(fig_width, fig_height)

#ax = fig.gca(projection='3d')
ax = Axes3D(fig, rect=(0.0, 0.05, 1, 0.9))


# ax = fig.add_axes((0.1, 0.1, 0.1, 0.1))


line_width = 1.2

ax.plot(gt_data['p_x'], gt_data['p_y'], gt_data['p_z'], color = plot_color['gt'], linewidth=line_width, label='gt')
ax.plot(dr_data['p_x'], dr_data['p_y'], dr_data['p_z'], color = plot_color['dr'], linewidth=line_width, label='dr')
ax.plot(est_opt_data['p_x'], est_opt_data['p_y'], est_opt_data['p_z'], color = plot_color['opt'], linewidth=line_width, label='opt.')
ax.plot(est_em_data['p_x'], est_em_data['p_y'], est_em_data['p_z'], color = plot_color['em'], linewidth=line_width, label='EM')
ax.plot(est_boem_data['p_x'], est_boem_data['p_y'], est_boem_data['p_z'], color = plot_color['boem'], linewidth=line_width, label='BOEM')
ax.plot(lmk_data['p_x'], lmk_data['p_y'], lmk_data['p_z'],'.', color = plot_color['lmk'], label='lmk')

ax.view_init(15, 45)


# trajectory only
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-3, 3)

ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')


ax.legend()

#plt.savefig("result/" + dataset + "/trajectory.pdf")

plt.show()


