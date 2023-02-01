ManyCellsAverageCapacity
------------------------

To allow for statistics in cell cycling testing experiments, this script averages the discharge or charge capacity in a given number of cycles of multiples cells. The scripts discards the first two and last two cycles as our group carry on testing cycles before and after the experiments. The script works with text file from MACCOR cyclers.

INSTALLATION
==============
To use the script, it is advisable to create a python virtual environment and run "py -m pip install -r Libraries_names.txt" or "pip install -r Libraries_names.txt" after the environment is activated.

HOW TO RUN THE SCRIPT
======================
Please, move the mpr files in the same directory where the script 'Read_EIS.py' is installed. Run the script. You will get text files with the data needed. 
