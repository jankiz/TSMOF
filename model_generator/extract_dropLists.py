#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:56:26 2022

@author: jankiz
"""

import multiprocessing
# import ast
# import re
import argparse

parser = argparse.ArgumentParser(description='Process data in leaves.')
parser.add_argument('--leaves_data_txt', type=str, help='use the absolute path of the txt file that contains the data of leaves')
parser.add_argument('--droplist_txt', type=str, help='use the absolute path of the txt file that will contain the droplist')

args = parser.parse_args()

leaves_filepath = args.leaves_data_txt # source: '/home/jankiz/PhD/Model_1_0_2880_7_leaves_data.txt'

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
        
        # for 2 processes
        # outcomes = ((line.split('dropList = ( 0 :> ')[1]).split(' )\\n/\\\\ now1')[0].strip()).split(' @@\\n  1 :> ')
        # for outcome in outcomes:
        #     print(outcome)
        #     new_outcome = outcome.replace('<<', '["').replace('>>', '"]').replace(', ', '", "')
        #     print(new_outcome)
        #     print(ast.literal_eval(new_outcome))
        
        # for 1 process
        line = line.replace('\\n', '').replace(' ', '')
        outcome = (line.split('dropList=(0:>')[1].split(')/\\\\now1')[0].strip())
        new_outcome = outcome.replace('<<', '["').replace('>>', '"]').replace(',', '", "')
        # print(new_outcome)
        # print(len(new_outcome))
        # print(ast.literal_eval(new_outcome))
        full_list.append(new_outcome)

numthreads = 1
numlines = 1

lines = open(leaves_filepath).readlines()
worker(lines)

# out: "/home/jankiz/PhD/Model_1_0_2880_7_droplist.txt"
with open(args.droplist_txt, "w") as text_file:
    for element in full_list:
        text_file.write(str(element))
        text_file.flush()


# create the process pool
# pool = multiprocessing.Pool(processes=numthreads)

# map the list of lines into a list of result dicts
# result_list = pool.map(worker, (lines[line:line+numlines] for line in range(0,len(lines),numlines)))
# print('DONE')