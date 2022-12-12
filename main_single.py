"""
Created on 02 Jun, 2022 at 15:29
    Title: main.py - Band Stacking
    Description:
        -   Stacking all the bands that are available in the product folder provided and make a single TIF file
        -   Start and End bands can be selected
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import rasterio
import numpy as np
import glob


def stack_band(path):
    file_name = input('Enter Product Folder (with slash at end): ')  # 'LC09_L2SP_146041_20220514_20220516_02_T1'
    num_bands = input('Enter the total number of bands you want to merge: ')

    # Specifying list of tif files to be stacked
    path_tif = glob.glob(path + file_name + file_name[:-1] + '*_B[1-' + num_bands + '].TIF')

    print('List of Band TIFs to be Merged:')
    print(*path_tif, sep='\n')

    print('Band Stacking Started ...')

    # Updating the meta for number of bands
    img = rasterio.open(path_tif[0])
    meta = img.meta
    meta.update(count=len(path_tif))

    # Naming the Stacked Image File
    stacked_img_name = path + file_name[:-1] + '_' + 'stacked.TIF'

    # Reading each layer and writing it into a stack
    stack_img = rasterio.open(stacked_img_name, 'w', **meta)

    for id, layer in enumerate(path_tif, start=1):
        print('Importing Band', layer, '...')
        band = rasterio.open(layer)
        stack_img.write_band(id, band.read(1))

    print('Stacked TIF path: ', stacked_img_name)
    print(layer, 'Bands Stacking Completed.')


path = input('Enter the complete Path of the Folder (Working Dir & Products stored) (with slash at end): ')

i = 'n'
while i == 'n':
    stack_band(path)
    i = input('Want to End (y) or Start another stacking (n) : ')