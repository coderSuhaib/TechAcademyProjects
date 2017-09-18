# Python Ver: 2.7.13
#
# Author: Suhaib Al-Tamimi
#
# Purpose: Create an application with a GUI that is able to copy files that end with ".txt" that have been 
#          modified or created within the last 24 hours. The user will be able to selects the folder they wish
#          to transfer from and the folder they wish to transfer to
#
# Tested OS: This code was written and tested to work with mac OS 10.12.6. with files that end with ".rtf"

from tkinter import *
import tkinter as tk
import daily_file_transfer_main
import daily_file_transfer_func


def load_gui(self):
    # This section is for the labels GUI
    self.label_source = tk.Label(self.master, text = 'Transfer from folder: ')
    self.label_source.grid(row = 0, column = 0, columnspan = 2, padx=(30,0),pady=(10,0), sticky=N+W)

    self.label_destination = tk.Label(self.master, text = "Transfer to folder: ")
    self.label_destination.grid(row = 0, column = 4, columnspan = 2, padx=(30,0),pady=(10,0), sticky = N+W)

    # This section is for the entries GUI
    self.entry_source = tk.Entry(self.master, text = "")
    self.entry_source.grid(row = 1, column = 0, columnspan = 2, padx=(10,0), pady=(5,0), sticky= N+E+W)

    self.entry_destination = tk.Entry(self.master, text = "")
    self.entry_destination.grid(row = 1, column = 4, columnspan = 2, padx=(10,0), pady=(5,0), sticky= N+E+W)

    # This section is for the open buttons GUI
    self.btn_source = tk.Button(self.master, width = 6, height = 2, text = "Open", command = lambda: daily_file_transfer_func.open_src(self))
    self.btn_source.grid(row= 1, column= 3, sticky= W)

    self.btn_destination = tk.Button(self.master, width = 6, height = 2, text = "Open", command = lambda: daily_file_transfer_func.open_dest(self))
    self.btn_destination.grid(row = 1, column = 7, sticky = W)

    # This section is for the left listbox and scrollbar GUI
    self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
    self.list1 = Listbox(self.master, exportselection = 0, yscrollcommand=self.scrollbar1.set)
    self.scrollbar1.config(command = self.list1.yview)
    self.scrollbar1.grid(row = 2, column =2 , rowspan = 3, padx=(0,0), pady=(5,10), sticky = N+E+S)
    self.list1.grid(row = 2, column = 0, rowspan = 3, columnspan = 2, padx=(10,0), pady=(5,10), sticky= N+E+S+W)

    # This section is for the right listbox and scrollbar GUI 
    self.scrollbar2 = Scrollbar(self.master, orient = VERTICAL)
    self.list2 = Listbox(self.master, exportselection = 0, yscrollcommand=self.scrollbar2.set)
    self.scrollbar2.config(command = self.list2.yview)
    self.scrollbar2.grid(row = 2, column =6 , rowspan = 3, padx=(0,0),pady=(5,10), sticky= N+E+S)
    self.list2.grid(row = 2, column = 4, rowspan = 3, columnspan = 2, padx=(10,0), pady=(5,10), sticky= N+E+S+W)

    # This section is for the label and the entry box of the last file transfer
    self.lbl_ltransfer = tk.Label(self.master, text = "")
    self.lbl_ltransfer.grid(row = 5, column = 0, columnspan = 5, padx = (10,0), pady = (5,0), sticky = N+W)



    # This section is for the copy and close buttons GUI 
    self.btn_copy = tk.Button(self.master, width = 6, height = 2, text = "Copy", command = lambda: daily_file_transfer_func.copy_files(self))
    self.btn_copy.grid(row = 5, column = 5, sticky = N+E)

    self.btn_close = tk.Button(self.master, width = 6, height = 2, text = "Close", command = lambda: daily_file_transfer_func.close_prog(self))
    self.btn_close.grid(row = 5, column = 7, sticky = N+W)
