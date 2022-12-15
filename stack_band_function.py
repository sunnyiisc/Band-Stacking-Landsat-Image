"""
Created on 30 Aug, 2022 at 12:49
    Title: stack_band_function.py - Function to stack the bands
    Description:
        -   Stack the bands in a selected folder to a single TIF file
        -   Start and end bands are specified followed by SAA, VAA, SZA, VZA
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import rasterio
import glob


def stack_band(path, folder_path, num_bands_start, num_bands_end):
    # Specifying list of tif files to be stacked
    if int(num_bands_end) < 10:
        path_tif = sorted(glob.glob(folder_path + '*B['+num_bands_start+'-'+num_bands_end+'].TIF')) + \
                   sorted(glob.glob(folder_path + '*A.TIF'))
    elif int(num_bands_end) >= 10:
        path_tif = sorted(glob.glob(folder_path + '*B[' + num_bands_start + '-9].TIF')) + \
                   sorted(glob.glob(folder_path + '*B1[0-' + num_bands_end[1] + '].TIF')) + \
                   sorted(glob.glob(folder_path + '*A.TIF'))

    print('List of Band TIFs to be Merged:')
    print(*path_tif, sep='\n')

    print('Band Stacking Started ...')

    # Updating the stacked image meta with first band meta
    img = rasterio.open(path_tif[0])
    meta = img.meta
    # Updating the stacked image meta with number of bands and datatype
    meta.update(count=len(path_tif))
    meta.update(dtype='float32')

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