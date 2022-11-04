
START=655
END=700

for i in $( eval echo {$START..$END} )
do
  echo "02 - Find leaves started in ${i}th iteration"
  python3.9 find_leaves.py --dot_filepath=/home/jankiz/PhD/scheduling/outputs/graphs/Model_1_0_2880_${i}.dot \
                         --leaves_txt=/home/jankiz/PhD/scheduling/outputs/leaves/Model_1_0_2880_${i}_leaves.txt
# done

# sleep 5

# for i in $( eval echo {$START..$END} )
# do
  echo "03 - Extract leaves data started in ${i}th iteration"
  python3.9 extract_leaves_data.py --leaves_txt=/home/jankiz/PhD/scheduling/outputs/leaves/Model_1_0_2880_${i}_leaves.txt \
                                 --dot_filepath=/home/jankiz/PhD/scheduling/outputs/graphs/Model_1_0_2880_${i}.dot \
                                 --leaves_data_txt=/home/jankiz/PhD/scheduling/outputs/leaves_data/Model_1_0_2880_${i}_leaves_data.txt
# done
  
# sleep 5

# for i in $( eval echo {$START..$END} )
# do
  echo "04 - Extract droplists started in ${i}th iteration"
  python3.9 extract_dropLists.py --leaves_data_txt=/home/jankiz/PhD/scheduling/outputs/leaves_data/Model_1_0_2880_${i}_leaves_data.txt \
                               --droplist_txt=/home/jankiz/PhD/scheduling/outputs/droplist/Model_1_0_2880_${i}_droplist.txt
# done

# sleep 5

# for i in $( eval echo {$START..$END} )
# do
  echo "05 - Predictor started in ${i}th iteration"
  python3.9 -W ignore /home/jankiz/PhD/scheduling/artial-fibrillation/Savvy-PF/python-Ervin/evaluation/savvy_predictor_mtla.py --droplist_txt=/home/jankiz/PhD/scheduling/outputs/droplist/Model_1_0_2880_${i}_droplist.txt \
                    --model_file=/home/jankiz/PhD/scheduling/artial-fibrillation/Savvy-PF/python-Ervin/evaluation/test/rfc2.obj \
                    --csv_folder=/home/jankiz/PhD/scheduling/artial-fibrillation/Savvy-PF/python-Ervin/evaluation/test/ > /home/jankiz/PhD/scheduling/outputs/evaluation/${i}.txt
done


