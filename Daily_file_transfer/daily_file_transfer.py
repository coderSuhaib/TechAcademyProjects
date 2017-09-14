# Python Ver: 2.7.13
#
# Author: Suhaib Al-Tamimi
#
# Purpose: Create an application that is able to copy files that end with ".txt" that have been 
#          modified or created within the last 24 hours from folderA to folderB.
#
# Tested OS: This code was written and tested to work with mac OS 10.12.6.

import os
import shutil
from datetime import datetime
import time

source = '/Users/suhaibabdul-sahib/desktop/folderA/'
destination = '/Users/suhaibabdul-sahib/desktop/folderB/'

def copy_files():
    for files in os.listdir(source):
        if time.time() - os.path.getmtime(source + files) <= 86400:
            if files.endswith(".txt"):
                shutil.copy(source + files,destination)
                print("{} file has been moved ".format(files))


            
copy_files()
