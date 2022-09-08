"""
Created on 30 Aug, 2022 at 11:24
    Title: browse_gui.py - Browsing GUI for selecting Folders and Files
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
from tkinter import filedialog

# Importing Custom Modules
...

...

def browse_folder():
    directory = filedialog.askdirectory(initialdir = '/',
                                        title = 'Select the Path Folder'
                                       )
    return directory


def browse_file():
    filename = filedialog.askopenfilename(initialdir = '/',
                                          title = 'Select the File',
                                          filetypes = (('all files','*.*'), ('text files', '*.txt*'))
                                         )
    return filename