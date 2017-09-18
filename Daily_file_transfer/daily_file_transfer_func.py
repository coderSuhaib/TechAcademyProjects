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
import time, datetime
from tkinter import *
from tkinter import messagebox, filedialog
import sqlite3
import daily_file_transfer_main
import daily_file_transfer_gui

# Below is the function that transfers created and modified files from folder A
# to folder B 

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
           if time.time() - os.path.getmtime(src+files) <= 86400:
               if files.endswith(".rtf"):
                   shutil.copy(src +files, dest)
        create_db(self)
        record_timestamp(self)
        update_entry(self)
        update_list2(self)
 
                

# This is the function section to open the transfer from folder where a folder is selected
# then the path is printed in the source entry section in the GUI 
def open_src(self):
    try:
        self.entry_source.delete(0,'end') # incase there was a previouse folder path in the entry box this command will delete it.
        self.list1.delete(0,'end') # this code is to delete the list box if the user selects a fold and then goes back and selects another folder.
        scr = filedialog.askdirectory()
        self.entry_source.insert(0,scr)
        for files in os.listdir(scr):
            sourceFile = os.path.join(scr,files)
            if time.time() - os.path.getmtime(sourceFile) <= 86400:
                if files.endswith(".rtf"):
                    self.list1.insert('end', files +'\n')
    except:
        pass  # This try and except is so that when the users cancels the program will not through an error.


# This is the function section to open the transfer from folder where a folder is selected
# then the path is printed in the source entry section in the GUI 
def open_dest(self):
    try:
        self.entry_destination.delete(0,'end') # incase there was a previouse folder path in the entry box this command will delete it.
        self.list2.delete(0,'end') # this code is to delete the list box if the user selects a fold and then goes back and selects another folder.
        dest = filedialog.askdirectory()
        self.entry_destination.insert(0,dest)
        for files in os.listdir(dest):
            self.list2.insert('end', files +'\n') # will display each file on a new lin in the list
    except:
        pass  


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



# This section is the function that creates a database and a table if it doesn't already exsist
def create_db(self):
    conn = sqlite3.connect('transfer_record.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_file_transfer(ID INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp TEXT);")
    conn.commit()
    conn.close()

# This function is to insert the timestamp of the last time the files where copied
def record_timestamp(self):
    last_update = datetime.datetime.now().strftime('%m-%d-%Y, %H:%M:%S') 
    conn = sqlite3.connect('transfer_record.db')
    with conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO tbl_file_transfer (Timestamp) VALUES(?)''', (last_update,))
    conn.commit()
    conn.close()


def update_entry(self):
    try:
        conn = sqlite3.connect('transfer_record.db')
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT MAX(timestamp) FROM tbl_file_transfer;")
            varTimestamp = cur.fetchone()[0]
            self.lbl_ltransfer.config(text = "Last update was: {}".format(varTimestamp))
        conn.close()
    except:
        pass

if __name__ == "__main__":
    root = tk.Tk() 
    App = ParentWindow(root) 
    root.mainloop()
