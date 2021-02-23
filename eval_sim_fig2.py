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

# error plot
gt_data = pd.read_csv("result/sim/vis/gt.csv")

fig = plt.figure(2)
fig.set_size_inches(fig_width, fig_height)

line_width = 1.5

dr_error = np.zeros_like(gt_data['p_x'])
est_opt_error = np.zeros_like(gt_data['p_x'])
est_em_error = np.zeros_like(gt_data['p_x'])
est_boem_error = np.zeros_like(gt_data['p_x'])

for i in range(len(gt_data['p_x'])):
	dr_error_list = []
	est_opt_error_list = []
	est_em_error_list = []
	est_boem_error_list = []
	for k in range(0,5):
		dr_data = pd.read_csv("result/sim/vis/dr_%s.csv" %k)
		est_opt_data = pd.read_csv("result/sim/test/opt_%s.csv" %k)
		est_em_data = pd.read_csv("result/sim/vis/em_%s.csv" %k)
		est_boem_data = pd.read_csv("result/sim/vis/boem_%s.csv" %k)
		dr_error_list.extend([(gt_data['p_x'][i]-dr_data['p_x'][i])**2, (gt_data['p_y'][i]-dr_data['p_y'][i])**2, (gt_data['p_z'][i]-dr_data['p_z'][i])**2])
		est_opt_error_list.extend([(gt_data['p_x'][i]-est_opt_data['p_x'][i])**2, (gt_data['p_y'][i]-est_opt_data['p_y'][i])**2, (gt_data['p_z'][i]-est_opt_data['p_z'][i])**2])
		est_em_error_list.extend([(gt_data['p_x'][i]-est_em_data['p_x'][i])**2, (gt_data['p_y'][i]-est_em_data['p_y'][i])**2, (gt_data['p_z'][i]-est_em_data['p_z'][i])**2])
		est_boem_error_list.extend([(gt_data['p_x'][i]-est_boem_data['p_x'][i])**2, (gt_data['p_y'][i]-est_boem_data['p_y'][i])**2, (gt_data['p_z'][i]-est_boem_data['p_z'][i])**2])
	dr_error[i] = math.sqrt(sum(dr_error_list)/len(dr_error_list))
	est_opt_error[i] = math.sqrt(sum(est_opt_error_list)/len(est_opt_error_list))
	est_em_error[i] = math.sqrt(sum(est_em_error_list)/len(est_em_error_list))
	est_boem_error[i] = math.sqrt(sum(est_boem_error_list)/len(est_boem_error_list))


plt.plot(gt_data['timestamp'], dr_error, color = plot_color['dr'], linewidth=line_width, label='dr')
plt.plot(gt_data['timestamp'], est_opt_error, color = plot_color['opt'], linewidth=line_width, label='opt.')
plt.plot(gt_data['timestamp'], est_em_error, color = plot_color['em'], linewidth=line_width, label='EM')
plt.plot(gt_data['timestamp'], est_boem_error, color = plot_color['boem'], linewidth=line_width, label='BOEM')


plt.legend()

plt.xlabel('time [s]')
plt.ylabel('RMSE [m]')
plt.ylim([0,.8])
# plt.savefig("result/" + dataset + "/error.pdf")

plt.show()

