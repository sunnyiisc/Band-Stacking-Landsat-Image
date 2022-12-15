"""
Created on 02 Jun, 2022 at 15:29
    Title: main.py - Band Stacking
    Description:
        -   Stacking all the bands that are available in the path provided and make a single TIF file
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import glob

# Importing Custom Modules
import browse_gui
from stack_band_function import stack_band

...
i = 'n'
while i == 'n':
    path = browse_gui.browse_folder('Folder containing all the bands of the product')
    path_save = browse_gui.browse_folder('Folder to save the stacked image')

    folder_path = path + '/' + path.rsplit('/', 1)[1]

    print('Name of products to be stacked:')
    print(folder_path)

    num_bands_start = input('Enter the start bands you want to merge: ')
    num_bands_end = input('Enter the end bands you want to merge: ')

    stack_band(path_save, folder_path, num_bands_start, num_bands_end)

    i = input('Want to End (y) or Start another stacking (n) : ')