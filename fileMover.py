# Python Ver: 2.7.13
#
# Author: Suhaib Al-Tamimi
#
# Purpose: Create an application that is able to move files that end with ".txt"
#          from folderA to folderB anf print the name of each file that was moved
#
# Tested OS: This code was written and tested to work with mac OS 10.12.6.


import shutil
import os

source = '/Users/suhaibabdul-sahib/desktop/folderA/'
destination = '/Users/suhaibabdul-sahib/desktop/folderB/'


for files in os.listdir(source):
    if files.endswith(".txt"):
        shutil.move(source + files,destination)
        print(files)
