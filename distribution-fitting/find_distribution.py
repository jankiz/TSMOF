#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:47:52 2022

@author: jankiz
"""

import scipy.stats as st

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


x_values = [0.161, 0.163, 0.168, 0.17, 0.174, 0.184, 0.191, 0.193, 0.195, 0.199, 0.201, 0.202, 0.203, 0.204, 0.205, 0.206, 0.207, 0.208, 0.209, 0.21, 0.211, 0.212, 0.213, 0.214, 0.215, 0.216, 0.217, 0.218, 0.219, 0.22, 0.221, 0.222, 0.223, 0.224, 0.225, 0.226, 0.227, 0.228, 0.229, 0.23, 0.232, 0.233, 0.234, 0.235, 0.236, 0.237, 0.238, 0.239, 0.24, 0.241, 0.243, 0.244, 0.245, 0.246, 0.247, 0.248, 0.249, 0.25, 0.251, 0.252, 0.253, 0.254, 0.255, 0.256, 0.257, 0.258, 0.259, 0.26, 0.261, 0.262, 0.263, 0.264, 0.265, 0.266, 0.267, 0.268, 0.269, 0.27, 0.271, 0.272, 0.273, 0.274, 0.275, 0.276, 0.277, 0.278, 0.279, 0.28, 0.281, 0.282, 0.283, 0.284, 0.285, 0.286, 0.287, 0.288, 0.289, 0.29, 0.291, 0.292, 0.293, 0.294, 0.295, 0.296, 0.297, 0.298, 0.299, 0.3, 0.301, 0.302, 0.303, 0.304, 0.305, 0.306, 0.307, 0.308, 0.309, 0.31, 0.311, 0.312, 0.313, 0.314, 0.315, 0.316, 0.317, 0.318, 0.319, 0.32, 0.321, 0.322, 0.323, 0.324, 0.325, 0.326, 0.327, 0.328, 0.329, 0.33, 0.331, 0.332, 0.333, 0.334, 0.335, 0.336, 0.337, 0.338, 0.339, 0.34, 0.341, 0.342, 0.343, 0.344, 0.345, 0.346, 0.347, 0.348, 0.349, 0.35, 0.351, 0.352, 0.353, 0.354, 0.355, 0.356, 0.357, 0.358, 0.359, 0.36, 0.361, 0.362, 0.363, 0.364, 0.365, 0.366, 0.367, 0.368, 0.369, 0.37, 0.371, 0.372, 0.373, 0.374, 0.375, 0.376, 0.377, 0.378, 0.379, 0.38, 0.381, 0.382, 0.383, 0.384, 0.385, 0.386, 0.387, 0.388, 0.39, 0.391, 0.392, 0.393, 0.394, 0.395, 0.396, 0.397, 0.398, 0.399, 0.4, 0.401, 0.402, 0.404, 0.405, 0.406, 0.407, 0.408, 0.409, 0.41, 0.411, 0.412, 0.413, 0.414, 0.415, 0.416, 0.417, 0.418, 0.419, 0.42, 0.421, 0.422, 0.423, 0.424, 0.425, 0.426, 0.428, 0.429, 0.43, 0.431, 0.433, 0.434, 0.435, 0.436, 0.437, 0.438, 0.439, 0.44, 0.441, 0.442, 0.443, 0.444, 0.445, 0.446, 0.447, 0.448, 0.449, 0.45, 0.451, 0.452, 0.453, 0.454, 0.455, 0.456, 0.457, 0.458, 0.459, 0.46, 0.461, 0.462, 0.463, 0.464, 0.465, 0.466, 0.467, 0.468, 0.469, 0.47, 0.472, 0.473, 0.474, 0.476, 0.477, 0.478, 0.479, 0.483, 0.485, 0.486, 0.488, 0.492, 0.495, 0.496, 0.498, 0.501, 0.503, 0.504, 0.506, 0.513, 0.529]
y_values = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 5.0, 4.0, 5.0, 5.0, 4.0, 11.0, 4.0, 4.0, 8.0, 4.0, 7.0, 6.0, 5.0, 6.0, 5.0, 7.0, 3.0, 3.0, 5.0, 5.0, 5.0, 4.0, 4.0, 2.0, 2.0, 4.0, 3.0, 1.0, 2.0, 2.0, 1.0, 5.0, 2.0, 3.0, 1.0, 5.0, 5.0, 2.0, 7.0, 6.0, 5.0, 9.0, 2.0, 6.0, 8.0, 7.0, 6.0, 8.0, 5.0, 6.0, 14.0, 9.0, 12.0, 14.0, 13.0, 18.0, 21.0, 14.0, 19.0, 12.0, 15.0, 24.0, 25.0, 28.0, 25.0, 32.0, 30.0, 34.0, 34.0, 31.0, 45.0, 32.0, 46.0, 33.0, 37.0, 32.0, 30.0, 35.0, 35.0, 36.0, 43.0, 32.0, 35.0, 40.0, 48.0, 44.0, 55.0, 51.0, 45.0, 53.0, 59.0, 63.0, 56.0, 71.0, 42.0, 56.0, 59.0, 64.0, 62.0, 56.0, 58.0, 49.0, 64.0, 46.0, 55.0, 60.0, 65.0, 43.0, 60.0, 64.0, 51.0, 63.0, 62.0, 54.0, 41.0, 32.0, 53.0, 40.0, 44.0, 48.0, 38.0, 45.0, 38.0, 39.0, 41.0, 39.0, 45.0, 44.0, 46.0, 29.0, 38.0, 46.0, 39.0, 34.0, 30.0, 37.0, 19.0, 22.0, 24.0, 34.0, 32.0, 39.0, 20.0, 24.0, 29.0, 28.0, 16.0, 22.0, 10.0, 11.0, 19.0, 10.0, 10.0, 13.0, 15.0, 15.0, 10.0, 6.0, 16.0, 17.0, 10.0, 10.0, 12.0, 14.0, 13.0, 6.0, 10.0, 7.0, 11.0, 8.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 9.0, 3.0, 7.0, 2.0, 3.0, 3.0, 7.0, 2.0, 3.0, 4.0, 1.0, 3.0, 4.0, 4.0, 6.0, 4.0, 2.0, 4.0, 6.0, 2.0, 5.0, 1.0, 8.0, 8.0, 1.0, 3.0, 8.0, 5.0, 6.0, 4.0, 3.0, 4.0, 4.0, 5.0, 4.0, 6.0, 3.0, 3.0, 5.0, 3.0, 4.0, 5.0, 2.0, 4.0, 5.0, 2.0, 2.0, 5.0, 3.0, 3.0, 1.0, 2.0, 2.0, 2.0, 2.0, 4.0, 5.0, 4.0, 4.0, 6.0, 5.0, 5.0, 2.0, 3.0, 4.0, 7.0, 6.0, 7.0, 2.0, 3.0, 1.0, 8.0, 5.0, 4.0, 4.0, 4.0, 2.0, 5.0, 2.0, 1.0, 3.0, 2.0, 1.0, 3.0, 2.0, 1.0, 3.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

max_y = max(y_values)
y_values_norm = [(val/max_y) for val in y_values]

data = delay_values
data = y_values_norm

# (-0.40113948173897923, 1.2150348003695126, 0.298013853069249, 0.037811382686445065)


def get_best_distribution(data):
    dist_names = ["norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme"]
    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(st, dist_name)
        param = dist.fit(data)
        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = st.kstest(data, dist_name, args=param)
        print("p value for "+dist_name+" = "+str(p))
        dist_results.append((dist_name, p))

    # select the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value
    
    print(dist_results)

    print("Best fitting distribution: "+str(best_dist))
    print("Best p value: "+ str(best_p))
    print("Parameters for the best fit: "+ str(params[best_dist]))

    return best_dist, best_p, params[best_dist]

import warnings
import numpy as np
import pandas as pd
# import scipy.stats as st
import statsmodels.api as sm
from scipy.stats._continuous_distns import _distn_names
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = (16.0, 12.0)
matplotlib.style.use('ggplot')

# Create models from data
def best_fit_distribution(data, bins=200, ax=None):
    """Model data by finding best fit distribution to data"""
    # Get histogram of original data
    y, x = np.histogram(data, bins=bins, density=True)
    x = (x + np.roll(x, -1))[:-1] / 2.0

    # Best holders
    best_distributions = []

    # Estimate distribution parameters from data
    # for ii, distribution in enumerate([d for d in _distn_names if not d in ['levy_stable', 'studentized_range']]):
    for ii, distribution in enumerate([d for d in _distn_names if d in ['nct', 'johnsonsu', 't', 'tukeylambda', 'burr12']]):

        print("{:>3} / {:<3}: {}".format( ii+1, len(_distn_names), distribution ))

        dist_name = distribution
        distribution = getattr(st, distribution)

        # Try to fit the distribution
        try:
            # Ignore warnings from data that can't be fit
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore')
                
                # fit dist to data
                params = distribution.fit(data)

                # Separate parts of parameters
                arg = params[:-2]
                loc = params[-2]
                scale = params[-1]
                
                # Calculate fitted PDF and error with fit in distribution
                pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
                sse = np.sum(np.power(y - pdf, 2.0))
                
                # if axis pass in add to plot
                try:
                    if ax:
                        pd.Series(pdf, x).plot(ax=ax, legend=True, label=dist_name)
                except Exception:
                    pass

                # identify if this distribution is better
                best_distributions.append((distribution, params, sse))
        
        except Exception:
            pass

    
    return sorted(best_distributions, key=lambda x:x[2])

def make_pdf(dist, params, size=10000):
    """Generate distributions's Probability Distribution Function """

    # Separate parts of parameters
    arg = params[:-2]
    loc = params[-2]
    scale = params[-1]

    # Get sane start and end points of distribution
    start = dist.ppf(0.01, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.01, loc=loc, scale=scale)
    end = dist.ppf(0.99, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.99, loc=loc, scale=scale)

    # Build PDF and turn into pandas Series
    x = np.linspace(start, end, size)
    y = dist.pdf(x, loc=loc, scale=scale, *arg)
    pdf = pd.Series(y, x)

    return pdf

# Load data from statsmodels datasets
# data = pd.Series(sm.datasets.elnino.load_pandas().data.set_index('YEAR').values.ravel())
data = pd.Series(delay_values)

# Plot for comparison
plt.figure(figsize=(12,8))
ax = data.plot(kind='hist', bins=50, density=True, alpha=0.5, color=list(matplotlib.rcParams['axes.prop_cycle'])[1]['color'])

# Save plot limits
dataYLim = ax.get_ylim()

# Find best fit distribution
best_distributions = best_fit_distribution(data, 200, ax)
print(best_distributions)
best_dist = best_distributions[1]

# Update plots
ax.set_ylim(dataYLim)
ax.set_title(u'ECG algorithm delay values\n All Fitted Distributions')
ax.set_xlabel(u'Delay values (ms)')
ax.set_ylabel('Frequency')

# Make PDF with best params 
pdf = make_pdf(best_dist[0], best_dist[1])

# Display
plt.figure(figsize=(12,8))
ax = pdf.plot(lw=2, label='PDF', legend=True)
data.plot(kind='hist', bins=50, density=True, alpha=0.5, label='Data', legend=True, ax=ax)

param_names = (best_dist[0].shapes + ', loc, scale').split(', ') if best_dist[0].shapes else ['loc', 'scale']
param_str = ', '.join(['{}={:0.2f}'.format(k,v) for k,v in zip(param_names, best_dist[1])])
dist_str = '{}({})'.format(best_dist[0].name, param_str)

ax.set_title(u'ECG algorithm delay values with best fit distribution \n' + dist_str)
ax.set_xlabel(u'Delay values (ms)')
ax.set_ylabel('Frequency')

plt.show()


# get_best_distribution(delay_values)