#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:28:02 2022

@author: jankiz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:46:23 2022

@author: jankiz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.pyplot import figure
import json
import math

from matplotlib.patches import Rectangle
from matplotlib.legend_handler import HandlerBase
import matplotlib.patches as mpatches

class HandlerColormap(HandlerBase):
    def __init__(self, cmap, num_stripes=8, **kw):
        HandlerBase.__init__(self, **kw)
        self.cmap = cmap
        self.num_stripes = num_stripes
    def create_artists(self, legend, orig_handle, 
                       xdescent, ydescent, width, height, fontsize, trans):
        stripes = []
        for i in range(self.num_stripes):
            s = Rectangle([xdescent + i * width / self.num_stripes, ydescent], 
                          width / self.num_stripes, 
                          height, 
                          fc=self.cmap((2 * i + 1) / (2 * self.num_stripes)), 
                          transform=trans)
            stripes.append(s)
        return stripes

# data_file = open('./data/all_o1_50.txt', 'r')
data_file = open('/home/jankiz/PhD/scheduling/outputs/evaluation5/test5_601.txt', 'r')
delay_values = []
afs = []
afs_num = []
dropped_windows = []
file_infos = []

count = 0

low_counter = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = data_file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    lat = line.split(';')[0]
    af_det = line.split(';')[1]
    af_det_num = line.split(';')[2]
    dropped = line.split(';')[7] # 3
    file_size = line.split(';')[8] # 4
    if float(lat) <= 20.0 and float(lat) > 0.1:
        delay_values.append(float(lat))
        afs.append(json.loads((af_det).lower()))
        afs_num.append(int(af_det_num))
        dropped_windows.append(int(dropped))
        file_infos.append(file_size)
    if float(lat) < 0.2:
        low_counter += 1
    # print("Line{}: {}".format(count, line.strip()))
    
data_file.close()

print('MIN: ', min(delay_values))
print('MAX: ', max(delay_values))

af_delays = []
af_nums = []
non_af_delays = []
af_dropped_win_nums = []
non_af_dropped_win_nums = []

af_file_sizes = []
non_af_file_sizes = []

for dv_index in range(0, len(delay_values)):
    if afs[dv_index] == True:
        af_delays.append(delay_values[dv_index])
        af_nums.append(afs_num[dv_index])
        af_dropped_win_nums.append(dropped_windows[dv_index])
        af_file_sizes.append(int(file_infos[dv_index])/1024)
    else:
        non_af_dropped_win_nums.append(dropped_windows[dv_index])
        non_af_delays.append(delay_values[dv_index])
        non_af_file_sizes.append(int(file_infos[dv_index])/1024)

print('AF DELAYS AVG: ', np.mean(af_delays))
print('NON AF DELAYS AVG: ', np.mean(non_af_delays))

print('AF DELAYS STD: ', np.std(af_delays))
print('NON AF DELAYS STD: ', np.std(non_af_delays))

s = [n for n in range(len(afs_num))]


cmap_af = matplotlib.colors.LinearSegmentedColormap.from_list('', ['yellow', 'red'])
cmap_non_af = matplotlib.colors.LinearSegmentedColormap.from_list('', ['white','black'])


figure(figsize=(10, 8), dpi=150)


sc_non_af = plt.scatter(non_af_delays, np.arange(0,math.ceil(len(non_af_delays)/2),0.5), s=50.0, c=non_af_dropped_win_nums, label='non_af', edgecolors='black', cmap=cmap_non_af)
plt.colorbar(sc_non_af)
cmaps = [cmap_non_af]  # set of colormaps 
cmap_labels = ['Non AF windows']
cmap_handles = [Rectangle((0, 0), 1, 1) for _ in cmaps]
handler_map = dict(zip(cmap_handles, 
                       [HandlerColormap(cm, num_stripes=10) for cm in cmaps]))

legend1 = plt.legend(handles=cmap_handles, 
           labels=cmap_labels, 
           handler_map=handler_map, 
           fontsize=12)

plt.show()


figure(figsize=(10, 8), dpi=150)

sc_af = plt.scatter(af_delays, np.arange(0,math.ceil(len(af_delays)/2),0.5), s=np.array(af_nums)*50.0, c=af_dropped_win_nums, label='af', edgecolors='black', cmap=cmap_af)
sc_non_af = plt.scatter(non_af_delays, np.arange(0,math.ceil(len(non_af_delays)/2),0.5), s=50.0, c=non_af_dropped_win_nums, label='non_af', edgecolors='black', cmap=cmap_non_af)

cb_af = plt.colorbar(sc_af)
cb_af.ax.get_yaxis().labelpad = 15
cb_af.ax.set_ylabel('Exposure', rotation=90)
plt.colorbar(sc_non_af)

af_nums_set = set(af_nums)
legend_labels = list(af_nums_set)


cmaps = [cmap_af, cmap_non_af]  # set of colormaps 
                                        # (as many as there are groups of lines)
cmap_labels = ['AF windows', 'Non AF windows']
# create proxy artists as handles:
cmap_handles = [Rectangle((0, 0), 1, 1) for _ in cmaps]
handler_map = dict(zip(cmap_handles, 
                       [HandlerColormap(cm, num_stripes=10) for cm in cmaps]))

legend1 = plt.legend(handles=cmap_handles, 
           labels=cmap_labels, 
           handler_map=handler_map, 
           fontsize=12)

"""kw = dict(prop="sizes", num=5, fmt="$ {x:.2f}", func=lambda s: 50 / np.sqrt(s),)
legend2 = plt.legend(*sc_af.legend_elements(sc_af, **kw), loc="lower right", title="Price")"""

    
handles, _ = sc_af.legend_elements(prop='sizes')
legend2 = plt.legend(handles=handles, labels=legend_labels, loc='lower left', title="# of AFs", labelspacing=1)

plt.gca().add_artist(legend1)

# To show the plot
plt.show()


"""bins = np.arange(0.5, 1.0, 0.0001)
hist_obj = plt.hist(af_delays, bins=bins, edgecolor = 'r', range = (0.5,100))
print(hist_obj)

hist_obj2 = plt.hist(non_af_delays, bins=bins, edgecolor = 'b', range = (0.5,100))

plt.show()"""
