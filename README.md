ManyCellsAverageCapacity
=========================

To allow for statistics in cell cycling testing experiments, this script averages cycling data files of multiple cells for the same cycling protocol using the discharge or charge capacity in a given number of cycles. The script discards the first two and last two cycles as our group carries on testing cycles before and after the experiments. The python program works with text files from MACCOR cyclers.

INSTALLATION
---
To use the script, it is advisable to create a python virtual environment and run "py -m pip install -r Libraries_names.txt" or "pip install -r Libraries_names.txt" after the environment is activated.

HOW TO RUN THE SCRIPT
---
+Please, move the maccor text files in the same directory where the script 'Average.py' is installed.\
+Run the script.\
+You will be asked to specific two numbers (columns of the MACCOR text file to work out the average).\
+You will get the average of charge the discharge values at a given cycle number for multiple cells.\


Example
---
Try: py Averarge.py 2 3\
Here 2 refers to the second column (cycle number) and 3 to the third column (the discharge capacity values).
