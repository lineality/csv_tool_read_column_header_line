"""
Script to print first lines of files in same directory

e.g.
Step 1. Put df_head.py file into a folder with you .csv file(s)
Step 2. open a terminal and type(and hit return): python3 df_head.py

vanilla python only, no installs needed:
This should work for even big files on any computer
where you can run a python script. no env or package
installs should be needed


v2 2022.08.04
"""

# import python packages and libraries 
import glob  # to get file names
import time
import zipfile

# helper function
def check_for_zip_files():

    # get list of .csv files in current working directory
    zip_list = glob.glob('*.zip')

    if len( zip_list ) > 0:

        for this_zip_file in zip_list:
            #open file 
            with zipfile.ZipFile( this_zip_file, "r" ) as z_file:
                z_file.extractall()
    
    return None

# # helper function: get lines version 1
# def read_first_line(this_file):
#     with open( this_file ) as f:
#         lines = f.read() 
#         first_line = lines.split('\n', 1)[0]

#     return first_line


# helper function get lines version 2
def read_first_line(this_file):
    with open( this_file ) as f:
        firstline = f.readlines()[0].rstrip()
        
    return firstline

# get files, get lines
def print_file_first_lines():

    # Print Legend
    print( f"[File] -> [Column Names Header]\n" )

    # get list of .csv files in current working directory
    file_list = glob.glob('*.csv')

    # iterate through list of files; get first lines; print
    for i in file_list:
      print( f"{i} -> {read_first_line(i)}" )

      # print a new-line
      print("\n")

    return None

# get start time
start_time = time.time()

# check for any ziped file (unzip if found)
check_for_zip_files()

###################################
# Print first line(s) from file(s)
###################################
print_file_first_lines()

#####################
# Get Execution Time
#####################
execution_time = time.time() - start_time
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(execution_time)))

