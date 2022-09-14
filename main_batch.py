"""
Created on 02 Jun, 2022 at 15:29
    Title: main.py - Band Stacking
    Description:
        -   Stacking all the bands that are available in the path provided and make a single TIF file
        -   Doing it in batch mode
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import glob


# Importing Custom Modules
import browse_gui
from stack_band_function import *

...
#path = input('Enter the complete Path of the Folder (Working Dir & Products stored) (with slash at end): ') #'/home/nrsc/Documents/DATA_Products/2022_05_26_L9_OLI_monthly_dec21_may22/'
path = browse_gui.browse_folder('Folder where all the product folders are stored')
#path_save = input('Enter the Complete Path of the Folder where you want to save (with slash at end): ')
path_save = browse_gui.browse_folder('Folder where the stacked images to be saved')

folder_path = glob.glob(path+'/**/')
#folder_path = glob.glob(path)
print('List of products to be stacked:')
print(*folder_path, sep='\n')

num_bands_start = input('Enter the start bands you want to merge: ')
num_bands_end = input('Enter the end bands you want to merge: ')

for folder in folder_path:
    stack_band(path_save, folder, num_bands_start, num_bands_end)
