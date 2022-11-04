#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:46:23 2022

@author: jankiz
"""

import numpy as np
import matplotlib.pyplot as plt

MULTIPLIER = 25

# data_file = open('./data/all_o1_50.txt', 'r')
data_file = open('/home/jankiz/PhD/scheduling/outputs/evaluation5/all_in_one.txt', 'r')
delay_values = []
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
    if float(line) <= 20.0 and float(line) > 0.1:
        delay_values.append(float(line))
    if float(line) < 0.2:
        low_counter += 1
    print("Line{}: {}".format(count, line.strip()))
 
data_file.close()

delay_values = [MULTIPLIER*v for v in delay_values]

bins = np.arange(MULTIPLIER*0.0, MULTIPLIER*1.0, 0.001)
# print(bins)
# print(delay_values)
# print(len(delay_values))
# print(low_counter)


# OWN SOLUTION
x = np.linspace(MULTIPLIER*0.2,MULTIPLIER*0.4,100)
# p1 = 0.314
# p2 = 0.0025
p1 = 0.30992244
p2 = 0.00144891

# GA SOLUTION
# x = np.linspace(-5,5,100)
# p1 = -1.66693934
# p2 = 1.66183896

coefficient_gauss = (1/p2*np.sqrt(2*np.pi))
exp_int = (((x-p1)**2)/p2)
y = np.exp(-exp_int)*70


# y = coefficient_gauss * np.exp(-exp_int)



r1 = -0.43948088
r2 = 38.17606665
r3 = 0.310069
r4 = 0.18750981

coefficient_johnson = (r2/(r4*np.sqrt(2*np.pi))) * (1/np.sqrt(1+((x-r3)/r4)**2))
core_asinh = ((x - float(r3))/float(r4))
asinh_expr = np.arcsinh(core_asinh**2)
exp_int = (-r1+r2*asinh_expr)
y2 = coefficient_johnson*np.exp(-(1/2)*exp_int)

hist_obj = plt.hist(delay_values, bins=bins, edgecolor = 'goldenrod', range = (-0,100))
print(hist_obj)
plt.xlabel('delay_values')
plt.ylabel('distribution of delay_values')
# plt.plot(x, y)
# plt.plot(x, y2)
plt.show()


