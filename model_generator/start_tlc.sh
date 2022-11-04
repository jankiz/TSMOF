START=1001
END=10000

for i in $( eval echo {$START..$END} )
do
  echo "01 - TLC Model Checker started in ${i}th iteration"
  java -jar /home/jankiz/toolbox/tla2tools.jar -lncheck 'final' \
      -config "/home/jankiz/PhD/tla_tools/Scheduling/Scheduling.cfg" \
      -dump "dot" "/home/jankiz/PhD/outputs/graphs/Model_1_0_2880_${i}" \
      -fpmem 20000 \
      -workers 'auto' /home/jankiz/PhD/tla_tools/Scheduling/Scheduling.tla > "/home/jankiz/PhD/outputs/logs/Model_1_0_2880_${i}_optimized.log"

  # sleep 1
done
