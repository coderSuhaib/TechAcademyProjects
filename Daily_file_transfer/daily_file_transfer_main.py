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
import daily_file_transfer_gui
import daily_file_transfer_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(560,300)
        self.master.maxsize(560,300)
        self.master.title('The Daily File Transfer')
        self.master.configure(bg='#404040')




        # load in the GUI widgets from a separate module
        daily_file_transfer_gui.load_gui(self)









if __name__ == "__main__":
    root = tk.Tk()  # This is the syntax that we use to create a window with tkinter 
    App = ParentWindow(root) # we call the class the App and attached the root in order to create the window and pass it to our class. 
    root.mainloop() #this takes the first window root and fire it over and over other wise it would
                    # display and then disapear right away. so we put it in a loop.
