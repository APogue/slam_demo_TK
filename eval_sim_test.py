import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plot_color = {
    'gt': [0, 0, 0],
    'opt_test': [0.8627, 0.2980, 0.2745],
    'opt': [0.8471, 0.6824, 0.2784],
    # 'lmk': [0.2633, 0.4475, 0.7086],  # navy
    # 'prlmk': [0.0000, 0.5490, 0.3765], # spruce
    # 'nrlmk': [0.1, 0.1490, 0.3765], # ?
}


fig_width = 5.84
fig_height = 4.38

# keyframe has larger time range than ground truth

gt_data = pd.read_csv("result/sim/exp_win_w_time/gt.csv")
est_opt_data = pd.read_csv("result/sim/exp_win_w_time/opt.csv")
est_opt_test = pd.read_csv("result/sim/exp_win_w_time/opt_test.csv")




# error plot
fig = plt.figure(5)
fig.set_size_inches(fig_width, fig_height)

opt_error = np.zeros_like(gt_data['p_x'])
opt_test_error = np.zeros_like(gt_data['p_x'])

for i in range(len(gt_data['p_x'])):
    opt_error[i] = math.sqrt( (gt_data['p_x'][i]-est_opt_data['p_x'][i])**2 + (gt_data['p_y'][i]-est_opt_data['p_y'][i])**2 + (gt_data['p_z'][i]-est_opt_data['p_z'][i])**2)
    opt_test_error[i] = math.sqrt((gt_data['p_x'][i] - est_opt_test['p_x'][i]) ** 2 + (gt_data['p_y'][i] - est_opt_test['p_y'][i]) ** 2 + (gt_data['p_z'][i] - est_opt_test['p_z'][i]) ** 2)


plt.plot(est_opt_data['timestamp'], opt_error, color = plot_color['opt'], label='opt')
plt.plot(est_opt_test['timestamp'], opt_test_error, color = plot_color['opt_test'], label='opt_test')


plt.legend()

plt.xlabel('time [s]')
plt.ylabel('error [m]')
# plt.ylim([0,2])

plt.show()

