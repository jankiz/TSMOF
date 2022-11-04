#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:27:48 2022

@author: jankiz
"""
import math
import numpy as np

# array = [0, 4, 16, 36, 64]
MULTIPLIER = 25

x_values = [0.161, 0.163, 0.168, 0.17, 0.174, 0.184, 0.191, 0.193, 0.195, 0.199, 0.201, 0.202, 0.203, 0.204, 0.205, 0.206, 0.207, 0.208, 0.209, 0.21, 0.211, 0.212, 0.213, 0.214, 0.215, 0.216, 0.217, 0.218, 0.219, 0.22, 0.221, 0.222, 0.223, 0.224, 0.225, 0.226, 0.227, 0.228, 0.229, 0.23, 0.232, 0.233, 0.234, 0.235, 0.236, 0.237, 0.238, 0.239, 0.24, 0.241, 0.243, 0.244, 0.245, 0.246, 0.247, 0.248, 0.249, 0.25, 0.251, 0.252, 0.253, 0.254, 0.255, 0.256, 0.257, 0.258, 0.259, 0.26, 0.261, 0.262, 0.263, 0.264, 0.265, 0.266, 0.267, 0.268, 0.269, 0.27, 0.271, 0.272, 0.273, 0.274, 0.275, 0.276, 0.277, 0.278, 0.279, 0.28, 0.281, 0.282, 0.283, 0.284, 0.285, 0.286, 0.287, 0.288, 0.289, 0.29, 0.291, 0.292, 0.293, 0.294, 0.295, 0.296, 0.297, 0.298, 0.299, 0.3, 0.301, 0.302, 0.303, 0.304, 0.305, 0.306, 0.307, 0.308, 0.309, 0.31, 0.311, 0.312, 0.313, 0.314, 0.315, 0.316, 0.317, 0.318, 0.319, 0.32, 0.321, 0.322, 0.323, 0.324, 0.325, 0.326, 0.327, 0.328, 0.329, 0.33, 0.331, 0.332, 0.333, 0.334, 0.335, 0.336, 0.337, 0.338, 0.339, 0.34, 0.341, 0.342, 0.343, 0.344, 0.345, 0.346, 0.347, 0.348, 0.349, 0.35, 0.351, 0.352, 0.353, 0.354, 0.355, 0.356, 0.357, 0.358, 0.359, 0.36, 0.361, 0.362, 0.363, 0.364, 0.365, 0.366, 0.367, 0.368, 0.369, 0.37, 0.371, 0.372, 0.373, 0.374, 0.375, 0.376, 0.377, 0.378, 0.379, 0.38, 0.381, 0.382, 0.383, 0.384, 0.385, 0.386, 0.387, 0.388, 0.39, 0.391, 0.392, 0.393, 0.394, 0.395, 0.396, 0.397, 0.398, 0.399, 0.4, 0.401, 0.402, 0.404, 0.405, 0.406, 0.407, 0.408, 0.409, 0.41, 0.411, 0.412, 0.413, 0.414, 0.415, 0.416, 0.417, 0.418, 0.419, 0.42, 0.421, 0.422, 0.423, 0.424, 0.425, 0.426, 0.428, 0.429, 0.43, 0.431, 0.433, 0.434, 0.435, 0.436, 0.437, 0.438, 0.439, 0.44, 0.441, 0.442, 0.443, 0.444, 0.445, 0.446, 0.447, 0.448, 0.449, 0.45, 0.451, 0.452, 0.453, 0.454, 0.455, 0.456, 0.457, 0.458, 0.459, 0.46, 0.461, 0.462, 0.463, 0.464, 0.465, 0.466, 0.467, 0.468, 0.469, 0.47, 0.472, 0.473, 0.474, 0.476, 0.477, 0.478, 0.479, 0.483, 0.485, 0.486, 0.488, 0.492, 0.495, 0.496, 0.498, 0.501, 0.503, 0.504, 0.506, 0.513, 0.529]
x_values = [x_v*MULTIPLIER for x_v in x_values]
y_values = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 5.0, 4.0, 5.0, 5.0, 4.0, 11.0, 4.0, 4.0, 8.0, 4.0, 7.0, 6.0, 5.0, 6.0, 5.0, 7.0, 3.0, 3.0, 5.0, 5.0, 5.0, 4.0, 4.0, 2.0, 2.0, 4.0, 3.0, 1.0, 2.0, 2.0, 1.0, 5.0, 2.0, 3.0, 1.0, 5.0, 5.0, 2.0, 7.0, 6.0, 5.0, 9.0, 2.0, 6.0, 8.0, 7.0, 6.0, 8.0, 5.0, 6.0, 14.0, 9.0, 12.0, 14.0, 13.0, 18.0, 21.0, 14.0, 19.0, 12.0, 15.0, 24.0, 25.0, 28.0, 25.0, 32.0, 30.0, 34.0, 34.0, 31.0, 45.0, 32.0, 46.0, 33.0, 37.0, 32.0, 30.0, 35.0, 35.0, 36.0, 43.0, 32.0, 35.0, 40.0, 48.0, 44.0, 55.0, 51.0, 45.0, 53.0, 59.0, 63.0, 56.0, 71.0, 42.0, 56.0, 59.0, 64.0, 62.0, 56.0, 58.0, 49.0, 64.0, 46.0, 55.0, 60.0, 65.0, 43.0, 60.0, 64.0, 51.0, 63.0, 62.0, 54.0, 41.0, 32.0, 53.0, 40.0, 44.0, 48.0, 38.0, 45.0, 38.0, 39.0, 41.0, 39.0, 45.0, 44.0, 46.0, 29.0, 38.0, 46.0, 39.0, 34.0, 30.0, 37.0, 19.0, 22.0, 24.0, 34.0, 32.0, 39.0, 20.0, 24.0, 29.0, 28.0, 16.0, 22.0, 10.0, 11.0, 19.0, 10.0, 10.0, 13.0, 15.0, 15.0, 10.0, 6.0, 16.0, 17.0, 10.0, 10.0, 12.0, 14.0, 13.0, 6.0, 10.0, 7.0, 11.0, 8.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 9.0, 3.0, 7.0, 2.0, 3.0, 3.0, 7.0, 2.0, 3.0, 4.0, 1.0, 3.0, 4.0, 4.0, 6.0, 4.0, 2.0, 4.0, 6.0, 2.0, 5.0, 1.0, 8.0, 8.0, 1.0, 3.0, 8.0, 5.0, 6.0, 4.0, 3.0, 4.0, 4.0, 5.0, 4.0, 6.0, 3.0, 3.0, 5.0, 3.0, 4.0, 5.0, 2.0, 4.0, 5.0, 2.0, 2.0, 5.0, 3.0, 3.0, 1.0, 2.0, 2.0, 2.0, 2.0, 4.0, 5.0, 4.0, 4.0, 6.0, 5.0, 5.0, 2.0, 3.0, 4.0, 7.0, 6.0, 7.0, 2.0, 3.0, 1.0, 8.0, 5.0, 4.0, 4.0, 4.0, 2.0, 5.0, 2.0, 1.0, 3.0, 2.0, 1.0, 3.0, 2.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

max_y = sum(y_values)
y_values_norm = [(val/max_y) for val in y_values]

print(sum(y_values_norm))

def find_weighted_avg_cut(x_values, y_values, cut_val):
    x_values = np.array(x_values)
    y_values = np.array(y_values)
    cutted_x = []
    cutted_idx = []
    # TODO: https://www.indeed.com/career-advice/career-development/how-to-calculate-weighted-average
    for idx in range(0,len(y_values)):
        if y_values[idx] > cut_val: # weight: y érték
            print(x_values[idx], y_values[idx])
            cutted_x.append(x_values[idx]*y_values[idx])
            cutted_idx.append(idx)
    
    print(sum(cutted_x))
    print(len(cutted_x))
    print(sum(cutted_x)/len(cutted_x))

# print(y_values)

def fitness_func(x):
    global x_values, y_values_norm
    
    p1, p2, p3, p4 = x
    # print(p1, p2)
    ret = 0
    for idx in range(0,len(y_values_norm)):
        # ret=ret+abs((idx*x)**2 - y_values[idx])
        # exp_int = (((x_values[idx]-p1)**2)/p2)
        exp_int = (-p1+p2*(math.asinh((x_values[idx]-p3)/p4))**2)
        # print(abs(exp_int))
        if abs(exp_int) > 600:
            return 100000000.0
        # print(exp_int)
        nom = math.exp(-(1/2)*exp_int)
        # print(nom)
        ret=ret+abs(nom - y_values_norm[idx])
    
    return ret

def check_fitness_func():
    global x_values, y_values_norm
    
    # best_x: -0.43948088 38.17606665  0.310069    0.18750981
    # best_y: 15.47844237
    
    # best_x: -0.43740406 30.          0.31001313  0.1648362
    # best_y: 15.44072127
    
    p1 = -0.43740406 # gamma
    p2 = 30. # delta, must be > 0
    p3 = 0.31001313 # xi
    p4 = 0.1648362 # lambda, must be > 0
    # print(p1, p2)
    ret = 0
    for idx in range(0,len(y_values_norm)):
        # ret=ret+abs((idx*x)**2 - y_values[idx])
        exp_int = (-p1+p2*(math.asinh((x_values[idx]-p3)/p4))**2)
        # if abs(exp_int) > 600:
            # return 100000000.0
        # print(exp_int)
        nom = math.exp(-(1/2)*exp_int)
        # print(nom)
        ret=ret+abs(nom - y_values_norm[idx])
    
    return ret

# find_weighted_avg_cut(x_values, y_values_norm, 0.5)


from sko.GA import GA
from sko.PSO import PSO
from sko.SA import SA
# pso = PSO(func=fitness_func, dim=2, max_iter=10000, lb=[-10, -10], ub=[10, 10])

# ga = GA(func=fitness_func, n_dim=4, max_iter=10000, lb=[-10.0, -40.0, -2.0, -2.0], ub=[10.0, 40.0, 2.0, 2.0])


# BEST
# ga = GA(func=fitness_func, n_dim=4, max_iter=10000, lb=[-1.0, 30.0, 0.0, -1.0], ub=[0.0, 40.0, 1.0, 1.0])
# best_x, best_y = ga.run()
# print('best_x is ', best_x)
# print('best_y is ', best_y)

pso = PSO(func=fitness_func, n_dim=4, max_iter=10000, lb=[MULTIPLIER*-1.0, MULTIPLIER*30.0, MULTIPLIER*0.0, MULTIPLIER*-1.0], ub=[MULTIPLIER*0.0, MULTIPLIER*40.0, MULTIPLIER*1.0, MULTIPLIER*1.0])
print([MULTIPLIER*-1.0, MULTIPLIER*30.0, MULTIPLIER*0.0, MULTIPLIER*-1.0], [MULTIPLIER*0.0, MULTIPLIER*40.0, MULTIPLIER*1.0, MULTIPLIER*1.0])
best_x2, best_y2 = pso.run()
print('best_x2 is ', best_x2)
print('best_y2 is ', best_y2)



# sa = SA(func=fitness_func, x0=[0.5, 35.0, 0.5, 0.0], n_dim=4, max_iter=10000, lb=[-1.0, 30.0, 0.0, -1.0], ub=[0.0, 40.0, 1.0, 1.0])
# best_x3, best_y3 = sa.run()
# print('best_x3 is ', best_x3)
# print('best_y3 is ', best_y3)
# BEST END


# ga = GA(func=fitness_func, n_dim=4, max_iter=10000)
# ga.Chrom = np.array([[0.314, 0.0025]])
# fitness = pso.fit()

# print('best_x is ',pso.gbest_x)
# print('best_y is ',pso.gbest_y)





print('my best_y is: ', check_fitness_func())

# pso.plot_history()



import matplotlib.pyplot as plt

# 100 linearly spaced numbers
x = np.linspace(4,MULTIPLIER*0.6,100)

# the function, which is y = x^2 here
# y = x**2
# exp_int = (((x-pso.gbest_x[0])**2)/pso.gbest_x[1])
# best_x = np.array([-0.43948088, 38.17606665, 0.310069, 0.18750981])
# best_x = best_x.astype(float)
best_x = best_x2
print(type(best_x[2]), type(best_x[3]))


# coefficient = (best_x[1]/(best_x[3]*np.sqrt(2*np.pi))) * (1/math.sqrt(1+((x-best_x[2])/best_x[3])**2))



core_asinh = ((x - float(best_x[2]))/float(best_x[3]))
asinh_expr = np.arcsinh(core_asinh**2)
exp_int = (-best_x[0]+best_x[1]*asinh_expr)
y = np.exp(-(1/2)*exp_int)

print(y)

# setting the axes at the centre
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.spines['left'].set_position(('data', 3.75))
ax1.spines['bottom'].set_position('zero')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# plot the function
# plt.plot(x,y, 'r')
plt.plot(x,y, 'darkred')

# show the plot

plt.xlabel('Delay values')
plt.ylabel('Distribution of delay values')

plt.bar(x_values, y_values_norm, color='goldenrod', width=0.001*MULTIPLIER)

# plt.plot(x_values, y_values_norm, 'g')
plt.show()
