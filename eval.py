import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

plot_color = {
	'gt': [0, 0, 0],
	'dr': [0.8627, 0.2980, 0.2745],
	'opt': [0.8471, 0.6824, 0.2784],
	'lmk': [0.2633, 0.4475, 0.7086],  # navy
	'prlmk': [0.0000, 0.5490, 0.3765], # spruce
    'nrlmk': [0.1, 0.1490, 0.3765], # ?
}


fig_width = 11.326
fig_height = 7.0

# keyframe has larger time range than ground truth

gt_data = pd.read_csv("../slam_demo/build/test/trajectory.csv")
dr_data = pd.read_csv("../slam_demo/build/test/trajectory_dr.csv")
opt_data = pd.read_csv("../slam_demo/build/test/trajectory_opt.csv")
lmk_data = pd.read_csv("../slam_demo/build/test/landmarks.csv")
# prlmk_data = pd.read_csv("../slam_demo/build/test/prot_landmarks.csv")
# nrlmk_data = pd.read_csv("../slam_demo/build/test/nrot_landmarks.csv")


# offset initial time
init_time = gt_data['timestamp'][0]
dr_data['timestamp'] = dr_data['timestamp'] - init_time
opt_data['timestamp'] = opt_data['timestamp'] - init_time

fig = plt.figure(1)
fig.set_size_inches(fig_width, fig_height)

ax = fig.gca(projection='3d')

# ax.scatter(landmark_data['p_x'], landmark_data['p_y'], landmark_data['p_z'])
ax.plot(gt_data['p_x'], gt_data['p_y'], gt_data['p_z'], color = plot_color['gt'], label='gt')
ax.plot(dr_data['p_x'], dr_data['p_y'], dr_data['p_z'], color = plot_color['dr'], label='dr')
ax.plot(opt_data['p_x'], opt_data['p_y'], opt_data['p_z'], color = plot_color['opt'], label='opt')
ax.plot(lmk_data['p_x'], lmk_data['p_y'], lmk_data['p_z'],'.', color = plot_color['lmk'], label='lmk')
# ax.plot(prlmk_data['p_x'], prlmk_data['p_y'], prlmk_data['p_z'],'.', color = plot_color['prlmk'], label='prlmk')
# ax.plot(nrlmk_data['p_x'], nrlmk_data['p_y'], nrlmk_data['p_z'],'.', color = plot_color['nrlmk'], label='nrlmk')
# for i in range(0,len(prlmk_data['p_x'])):
# 	x_values = [gt_data['p_x'][0], prlmk_data['p_x'][i]]
# 	y_values = [gt_data['p_y'][0], prlmk_data['p_y'][i]]
# 	z_values = [gt_data['p_z'][0], prlmk_data['p_z'][i]]
# 	ax.plot(x_values, y_values, z_values, color = plot_color['prlmk'])

ax.view_init(39, 3)


# trajectory only
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-3,3)


ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')

ax.legend()

plt.savefig('result/result_2.pdf')  

plt.show()

# rotation plot
fig = plt.figure(2)
fig.set_size_inches(fig_width, fig_height)

ax_q_w = plt.subplot(411)
plt.plot(gt_data['timestamp'], gt_data['q_w'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['q_w'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['q_w'], color = plot_color['opt'], label='opt')
plt.ylabel('q_w')
plt.setp(ax_q_w.get_xticklabels(), visible=False)

plt.legend()

ax_q_x = plt.subplot(412)
plt.plot(gt_data['timestamp'], gt_data['q_x'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['q_x'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['q_x'], color = plot_color['opt'], label='opt')


plt.ylabel('q_x')
plt.setp(ax_q_x.get_xticklabels(), visible=False)


ax_q_y = plt.subplot(413)
plt.plot(gt_data['timestamp'], gt_data['q_y'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['q_y'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['q_y'], color = plot_color['opt'], label='opt')


plt.ylabel('q_y')
plt.setp(ax_q_y.get_xticklabels(), visible=False)


ax_q_z = plt.subplot(414)
plt.plot(gt_data['timestamp'], gt_data['q_z'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['q_z'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['q_z'], color = plot_color['opt'], label='opt')


plt.ylabel('q_z')
plt.xlabel('time [s]')

plt.savefig('result/rotation.pdf')  

plt.show()


# velocity plot
fig = plt.figure(3)
fig.set_size_inches(fig_width, fig_height)


ax_v_x = plt.subplot(311)
plt.plot(gt_data['timestamp'], gt_data['v_x'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['v_x'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['v_x'], color = plot_color['opt'], label='opt')


plt.ylabel('v_x')
plt.setp(ax_v_x.get_xticklabels(), visible=False)
plt.legend()


ax_v_y = plt.subplot(312)
plt.plot(gt_data['timestamp'], gt_data['v_y'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['v_y'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['v_y'], color = plot_color['opt'], label='opt')

plt.ylabel('v_y')
plt.setp(ax_v_y.get_xticklabels(), visible=False)

ax_v_z = plt.subplot(313)
plt.plot(gt_data['timestamp'], gt_data['v_z'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['v_z'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['v_z'], color = plot_color['opt'], label='opt')

plt.ylabel('v_z')

plt.xlabel('time [s]')

plt.savefig('result/velocity.pdf')  

plt.show()


# position plot
fig = plt.figure(4)
fig.set_size_inches(fig_width, fig_height)


ax_p_x = plt.subplot(311)
plt.plot(gt_data['timestamp'], gt_data['p_x'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['p_x'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['p_x'], color = plot_color['opt'], label='opt')

plt.ylabel('p_x')
plt.setp(ax_p_x.get_xticklabels(), visible=False)
plt.legend()


ax_p_y = plt.subplot(312)
plt.plot(gt_data['timestamp'], gt_data['p_y'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['p_y'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['p_y'], color = plot_color['opt'], label='opt')

plt.ylabel('p_y')
plt.setp(ax_p_y.get_xticklabels(), visible=False)

ax_p_z = plt.subplot(313)
plt.plot(gt_data['timestamp'], gt_data['p_z'], color = plot_color['gt'], label='gt')
plt.plot(dr_data['timestamp'], dr_data['p_z'], color = plot_color['dr'], label='dr')
plt.plot(opt_data['timestamp'], opt_data['p_z'], color = plot_color['opt'], label='opt')

plt.ylabel('p_z')

plt.xlabel('time [s]')

plt.savefig('result/position.pdf')  

plt.show()


# error plot
fig = plt.figure(5)
fig.set_size_inches(fig_width, fig_height)

traj_error = np.zeros_like(gt_data['p_x'])
opt_error = np.zeros_like(gt_data['p_x'])

for i in range(len(gt_data['p_x'])):
    traj_error[i] = math.sqrt( (gt_data['p_x'][i]-dr_data['p_x'][i])**2 + (gt_data['p_y'][i]-dr_data['p_y'][i])**2 + (gt_data['p_z'][i]-dr_data['p_z'][i])**2)
    opt_error[i] = math.sqrt((gt_data['p_x'][i] - opt_data['p_x'][i]) ** 2 + (gt_data['p_y'][i] - opt_data['p_y'][i]) ** 2 + (gt_data['p_z'][i] - opt_data['p_z'][i]) ** 2)


plt.plot(dr_data['timestamp'], traj_error, color = plot_color['dr'], label='dr')
plt.plot(dr_data['timestamp'], opt_error, color = plot_color['opt'], label='opt')


plt.legend()

plt.xlabel('time [s]')
plt.ylabel('error [m]')
plt.ylim([0,2])

plt.savefig('result/error.pdf')

plt.show()


print(np.mean(traj_error))
print(np.mean(opt_error))
