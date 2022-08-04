"""
### csv_tool_read_column_header_line
["Save link as" to download] https://raw.githubusercontent.com/lineality/csv_tool_read_column_header_line/main/df_head.py 

# df_head.py

This is a python script that reads 
the first line of .csv files.
e.g. 
df_head.py mimics the pandas operation: df.head()

## Instruction Steps:

#### Step 1. 
- Put df_head.py file into a folder 
with your .csv file(s)

#### Step 2. 
- open a terminal and type (and hit return): 
```
python3 df_head.py
```

## No Python Environment or Installs Needed
This script uses only vanilla python and so
should not require any additional environments,
libraries, packages or set up. Just run in a folder 
along with the .csv files.

This method should work for larger files 
(hundreds of megs or a few gigs in size)  
on any computer or device where you can run 
a python script.

## Zipped Archived Handled
if .csv files are in a zipped archive, the function will
automatically find and unzip the archive and then handle each file.


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
