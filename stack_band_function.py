"""
Created on 30 Aug, 2022 at 12:49
    Title: stack_band_function.py - ...
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import rasterio
import glob

# Importing Custom Modules
...

...
def stack_band(path, folder_path, num_bands_start, num_bands_end):
    # Specifying list of tif files to be stacked

    path_tif = sorted(glob.glob(folder_path + '*_B['+num_bands_start+'-'+num_bands_end+'].TIF')) \
               + glob.glob(folder_path + '*_ZA.TIF') \
               + glob.glob(folder_path + '*_AA.TIF')

    print('List of Band TIFs to be Merged:')
    print(*path_tif, sep='\n')

    print('Band Stacking Started ...')

    # Updating the meta for number of bands
    img = rasterio.open(path_tif[0])
    meta = img.meta
    meta.update(count=len(path_tif))

    # Naming the Stacked Image File
    file_name = folder_path.split('/')[-2]
    stacked_img_name = path + '/' + file_name + '_' + 'stacked.TIF'

    # Reading each layer and writing it into a stack
    stack_img = rasterio.open(stacked_img_name, 'w', **meta)

    for id, layer in enumerate(path_tif, start=1):
        print('Importing Band', layer, '...')
        band = rasterio.open(layer)
        stack_img.write_band(id, band.read(1))

    print('Stacked TIF path: ', stacked_img_name)
    print('Bands Stacking Completed.')