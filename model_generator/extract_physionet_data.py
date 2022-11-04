#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:15:18 2022

@author: jankiz
"""

import datetime

# data_file = open('./data/all_o1_50.txt', 'r')
data_file = open('/home/jankiz/PhD/scheduling/artial-fibrillation/Savvy-PF/python-Ervin/evaluation/test4_7/sample.txt', 'r')
extracted_data_file = open('/home/jankiz/PhD/scheduling/artial-fibrillation/Savvy-PF/python-Ervin/evaluation/test4_7/sample_savvy_format.txt', 'w')
count = 0

ecg_values = ''

start_date = datetime.datetime(2000,1,1,0,0).timestamp()
 
while True:
    count += 1
    
    line = data_file.readline()
    
    if not line:
        break
    
    # Get next line from file
    line_splitted = line.split(',')
    timestamp = line_splitted[0]
    ecg_value = line_splitted[1].strip()
    
    ecg_values += str(float(ecg_value) + 500.0) + ','
    
    if count % 14 == 0:
        ecg_values += str(start_date + float(timestamp))
        extracted_data_file.write(ecg_values + '\n')
        extracted_data_file.flush()
        ecg_values = ''
 
    # if line is empty
    # end of file is reached
    
    print("Line{}: {}".format(count, line.strip()))
 
data_file.close()
extracted_data_file.close()
