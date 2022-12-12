"""
Created on 02 Jun, 2022 at 15:29
    Title: main.py - Band Stacking in batch mode
    Description:
        -   Stacking all the bands that are available in the path provided and make a single TIF file
        -   Doing it in batch mode
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import rasterio
import numpy as np
import glob


def stack_band(path, folder_path, num_bands_start, num_bands_end):
    # Specifying list of tif files to be stacked
    path_tif = sorted(glob.glob(folder_path + '*_B['+num_bands_start+'-'+num_bands_end+'].TIF')) + glob.glob(folder_path + '*_SZA.TIF')

    print('List of Band TIFs to be Merged:')
    print(*path_tif, sep='\n')

    print('Band Stacking Started ...')

    # Updating the meta for number of bands
    img = rasterio.open(path_tif[0])
    meta = img.meta
    meta.update(count=len(path_tif))

    # Naming the Stacked Image File
    file_name = folder_path.split('/')[-2]
    stacked_img_name = path + file_name + '_' + 'stacked.TIF'

    # Reading each layer and writing it into a stack
    stack_img = rasterio.open(stacked_img_name, 'w', **meta)

    for id, layer in enumerate(path_tif, start=1):
        print('Importing Band', layer, '...')
        band = rasterio.open(layer)
        stack_img.write_band(id, band.read(1))

    print('Stacked TIF path: ', stacked_img_name)
    print('Bands Stacking Completed.')


path = input('Enter the complete Path of the Folder (Working Dir & Products stored) (with slash at end): ')
path_save = input('Enter the Complete Path of the Folder where you want to save (with slash at end): ')

folder_path = glob.glob(path+'**/')
print('List of products to be stacked:')
print(*folder_path, sep='\n')

num_bands_start = input('Enter the start bands you want to merge: ')
num_bands_end = input('Enter the end bands you want to merge: ')

for folder in folder_path:
    stack_band(path_save, folder, num_bands_start, num_bands_end)
