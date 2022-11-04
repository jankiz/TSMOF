#!/bin/bash
for filename in /home/jankiz/PhD/scheduling/outputs/droplist/Model_1_0_2880_{1..500}_droplist.txt; do
    echo -n "${filename};"; grep -o -i TRUE ${filename} | wc -l;
done
