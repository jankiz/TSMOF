#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:32:55 2022

@author: jankiz
"""

import multiprocessing
import argparse

parser = argparse.ArgumentParser(description='Process leaves.')
parser.add_argument('--leaves_txt', type=str, help='use the absolute path of the txt file that contains leaves')
parser.add_argument('--dot_filepath', type=str, help='use the absolute path of the dot file that contain the simulation graph')
parser.add_argument('--leaves_data_txt', type=str, help='use the absolute path of the txt file that will contain the data of leaves')

args = parser.parse_args()

leaves_filepath = args.leaves_txt # source: '/home/jankiz/PhD/Model_1_0_2880_7_leaves.txt'
dot_filepath = args.dot_filepath # source: '/home/jankiz/PhD/Model_1_0_2880_7.dot'

parsedString = ''
leaves = set()

manager = multiprocessing.Manager()
full_list = manager.list()

def worker(lines):
    cnt = 0
    for line in lines:
        # print(line)
        cnt += 1
        # print(cnt)
        if 'dropList' in line and line.split('[label')[0].strip() in leaves:
            # print(line)
            full_list.append(str(line))
            # print(leaves)
            # print(type(line.split('[label')[0].strip()))

# out: "/home/jankiz/PhD/Model_1_0_2880_7_leaves_data.txt"
with open(args.leaves_data_txt, "w") as text_file:
    with open(leaves_filepath) as leaves_file:
        line = leaves_file.readline()
        cnt = 1
        while line:
            leaves.add(line.strip())
            cnt += 1
            line = leaves_file.readline()
        # with open(dot_filepath) as dot_file:
        
        numthreads = 10
        numlines = 55429
    
        lines = open(dot_filepath).readlines()
    
        # create the process pool
        pool = multiprocessing.Pool(processes=numthreads)
    
        # map the list of lines into a list of result dicts
        result_list = pool.map(worker, (lines[line:line+numlines] for line in range(0,len(lines),numlines)))
        print('DONE')
            
        """line2 = dot_file.readline()
        cnt2 = 1
        while line2:
            if 'dropList' in line and line.split('[label')[0].strip() in leaves:
                print(line)
            line = dot_file.readline()
            cnt2 += 1"""
            
        
        for element in full_list:
            text_file.write(str(element))
            text_file.flush()
                
            
                
                
                
        text_file.close()
        leaves_file.close()