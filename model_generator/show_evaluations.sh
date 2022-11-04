#!/bin/bash
for filename in /home/jankiz/PhD/scheduling/outputs/evaluation/{1..500}.txt; do
    echo -n "${filename};"; tail -n 3 ${filename} | tr '\n' ';'; echo ""
done

# tail -n 3 /home/jankiz/PhD/outputs/evaluation/*.txt
