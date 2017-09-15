# Python Ver: 2.7.13
#
# Author: Suhaib Al-Tamimi
#
# Purpose: Create an application with a GUI that is able to copy files that end with ".txt" that have been 
#          modified or created within the last 24 hours. The user will be able to selects the folder they wish
#          to transfer from and the folder they wish to transfer to
#
# Tested OS: This code was written and tested to work with mac OS 10.12.6. with files that end with ".rtf"

import os
import shutil
import time
from tkinter import *
from tkinter import messagebox, filedialog
import daily_file_transfer_main
import daily_file_transfer_gui

# Below is the function that transfers created and modified files from folder A
# to folder B 
source = '/Users/suhaibabdul-sahib/desktop/folderA/'
destination = '/Users/suhaibabdul-sahib/desktop/folderB/'


def copy_files(self):
    if (len(self.entry_source.get()) == 0):
        # This section makes sure that the use has both made sure that they didn't leave the section empty and that they have selected the correct fold
        messagebox.showinfo("File path missing", "Please make sure that you have selected the correct transfer from folder")
    if (len(self.entry_destination.get()) == 0):
        # This section makes sure that the use has both made sure that they didn't leave the section empty and that they have selected the correct fold
        messagebox.showinfo("File path missing", "Please make sure that you have selected the correct transfer to folder")
    else:
        src = self.entry_source.get()+'/'
        dest = self.entry_destination.get()+'/'
        for files in os.listdir(src):
           if time.time() - os.path.getmtime(source + files) <= 86400:
               if files.endswith(".txt"):
                   shutil.copy(src +files, dest)
        update_list2(self)
 
                

# This is the function section to open the transfer from folder where a folder is selected
# then the path is printed in the source entry section in the GUI 
def open_src(self):
    self.entry_source.delete(0,'end') # incase there was a previouse folder path in the entry box this command will delete it.
    self.list1.delete(0,'end') # this code is to delete the list box if the user selects a fold and then goes back and selects another folder.
    scr = filedialog.askdirectory()
    self.entry_source.insert(0,scr)
    for files in os.listdir(scr):
        if time.time() - os.path.getmtime(source + files) <= 86400:
            if files.endswith(".txt"):
                self.list1.insert('end', files +'\n')


# This is the function section to open the transfer from folder where a folder is selected
# then the path is printed in the source entry section in the GUI 
def open_dest(self):
    self.entry_destination.delete(0,'end') # incase there was a previouse folder path in the entry box this command will delete it.
    self.list2.delete(0,'end') # this code is to delete the list box if the user selects a fold and then goes back and selects another folder.
    dest = filedialog.askdirectory()
    self.entry_destination.insert(0,dest)
    for files in os.listdir(dest):
        self.list2.insert('end', files +'\n') # will display each file on a new lin in the list



def update_list2(self):
    # this bit of code is so that after the file copy is completed the list2 will get updated with the new added files.
    dest = self.entry_destination.get()+'/'
    for files in os.listdir(dest):
        self.list2.insert('end', files +'\n')
    

# This section is for the close button to fully close the program and makes sure that there isn't any reference to any widgets
def close_prog(self):
    if messagebox.askokcancel("Close daily file transfer", "Do you want to exit Daily File Transfer?"):
        self.master.destroy()
        os._exit(0)     # This takes all of our widgets and fully deletes them to any refrencess in the memory
                        # to prevent a memory leak.


if __name__ == "__main__":
    root = tk.Tk() 
    App = ParentWindow(root) 
    root.mainloop()

