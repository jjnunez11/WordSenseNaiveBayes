import re
from pathlib import Path
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:05:23 2019

@author: jjnun
"""
# Function that pre-processes the text files with the examples
# Removes the tag, renames file to include label, and collects into one folder


# Five folders corresponding to the five derives
def pre_process(raw_data_folder, proc_data_folder):
    for folder in raw_data_folder.iterdir():
        # Each folder then contains many files
        for file in folder.iterdir():
            f = open(file, 'r')
            # Remove the tag
            clean_text = re.sub(r'<tag.*</>', ' ', f.read())
            # Produce a new file name for the processed file
            clean_filename = file.stem + '-' + folder.stem
            clean_filepath = proc_data_folder / clean_filename
            # Write cleaned text to file
            f2 = open(clean_filepath,'w')
            f2.write(clean_text)
        

        