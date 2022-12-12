# Band-Stacking-Landsat-Image
Stacking the Bands of Landsat Multi-Spectral Image to create a single TIF file

### Running in Single mode:
- Run the file 'main_single.py' [click here](main_single.py)
- Enter the folder path with slash at the end like '/home/${USER}/Documents/Prod_Folder/LC09_L2SP_146041_20220514_20220516_02_T1/'
- Enter the last band number, if 3 selected then Band1, Band2 and Band3 will be stacked.
- The stacked image will be saved as '/home/${USER}/Documents/Prod_Folder/LC09_L2SP_146041_20220514_20220516_02_T1/LC09_L2SP_146041_20220514_20220516_02_T1_stacked.TIF'


### Running in Batch mode:
- Run the file 'main_batch.py' [click here](main_batch.py)
- Create a working directory like follows, where all the product folders are stored.
- Enter the folder path with slash at the end like '/home/${USER}/Documents/Prod_Folder/'
- Enter the start and last band number, if 1 and 3 are selected respectively then Band1, Band2 and Band3 will be stacked.
- The stacked image will be saved as '/home/${USER}/Documents/Prod_Folder/LC09_L2SP_146041_20220514_20220516_02_T1_stacked.TIF'