#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:44:10 2022

@author: jankiz
"""

from scipy import stats
import numpy as np
import pylab

# data_file = open('./data/all_o1_50.txt', 'r')
data_file = open('/home/jankiz/PhD/scheduling/outputs/evaluation5/all_in_one.txt', 'r')
delay_values = []
count = 0

low_counter = 0

ALPHA = 0.05 # threshold value for rejecting the null hypothesis
ALPHA = 1e-3
 
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
    # print("Line{}: {}".format(count, line.strip()))
 
data_file.close()

data = np.random.normal(loc=20, scale=5, size=150)

# Normality tests: https://towardsdatascience.com/normality-tests-in-python-31e04aa4f411

# STATS.PROBPLOT
"""stats.probplot(data, dist='norm', plot=pylab)
pylab.show()"""

# D'AGOSTINO K^2 TEST
# SKEWNESS: symmetry
# KURTOSIS: heavy-tailed or light-tailed
k2, p = stats.normaltest(delay_values)

print("p = {:g}".format(p))
print("k2 = {:g}".format(k2))

if p > ALPHA:  # null hypothesis: x comes from a normal distribution
    print('It is Gaussian.')
else:
    print('It is not Gaussian.')

# Shapiro-Wilk Test
print(data)
stat_shapiro, p_shapiro = stats.shapiro(delay_values)
print(stat_shapiro, p_shapiro)
if (p_shapiro > ALPHA):
    print('It is Gaussian.')
else:
    print('It is not Gaussian.')
    
# Anderson-Darling Normality Test
res_anderson = stats.anderson(delay_values)
print('statistic: ', res_anderson.statistic)
for i in range(0,len(res_anderson.critical_values)):
    sig_lev, crit_val = res_anderson.significance_level[i], res_anderson.critical_values[i]
    if res_anderson.statistic < crit_val:
        print('It is Gaussian.', crit_val, sig_lev)
    else:
        print('It is not Gaussian.', crit_val, sig_lev)

# CHI^2 NORMALITY TEST
chi_stat, chi_p = stats.chisquare(delay_values)
print('CHI^2: ', chi_stat, chi_p)
if chi_p > ALPHA:
    print('It is Gaussian.')
else:
    print('It is not Gaussian.')
    
    
# JARQUE-BERA TEST
jb_stat, jb_p = stats.jarque_bera(delay_values)
print('JARQUE-BERA: ', jb_stat, jb_p)
if jb_p > ALPHA:
    print('It is Gaussian.')
else:
    print('It is not Gaussian.')
    
# KOLMOGROV-SMIRNOV TEST
ks_stat, ks_p = stats.kstest(delay_values, 'norm')
print('KOLMOGROV-SMIRNOV: ', ks_stat, ks_p)
if ks_p > ALPHA:
    print('It is Gaussian.')
else:
    print('It is not Gaussian.')
    
# NCT TEST
