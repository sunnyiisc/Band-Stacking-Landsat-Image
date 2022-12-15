# Band-Stacking-Landsat-Image
Stacking the Bands of Landsat Multi-Spectral Image to create a single TIF file

### Running in Single mode:
- Run the file 'main_single.py' [click here](main_single.py)
- Enter the folder path with slash at the end like 
```bash
  '/home/${USER}/Documents/Prod_Folder/LC09_L2SP_146041_20220514_20220516_02_T1/'
```
- Enter the last band number, if 3 selected then Band1, Band2 and Band3 will be stacked.
- The stacked image will be saved as 
```bash
  '/home/${USER}/Documents/Prod_Folder/LC09_L2SP_146041_20220514_20220516_02_T1/LC09_L2SP_146041_20220514_20220516_02_T1_stacked.TIF'
```


### Running in Batch mode:
- Run the file 'main_batch.py' [click here](main_batch.py)
- Create a working directory like follows, where all the product folders are stored.

```bash
├── Prod_Folder
    ├── Prod1_Folder
    ├── Prod2_Folder
    ├── Prod3_Folder
```

- Select the folder path where all the products are saved 'Prod_Folder' from the gui as follows:

![Screenshot from 2022-12-14 09-52-33_crop](https://user-images.githubusercontent.com/105144544/207774225-2e7fde1b-de3b-49dd-a21f-d9e4bd9a6449.png)

- Select the folder path where you want to save the stacked images from the gui as follows:

![Screenshot from 2022-12-14 09-52-52_crop](https://user-images.githubusercontent.com/105144544/207774254-1e788c02-de7a-48fc-ae0b-5019f35ba28f.png)

- Enter the start and last band number, if 1 and 3 are selected respectively then Band1, Band2 and Band3 will be stacked. Followed by the angles as follows:
  - BAND1
  - BAND2
  - BAND3
  - SZA
  - VZA
  - SAA
  - VAA
  
- The stacked image will be saved as 
```bash
    '/home/${USER}/Documents/Save_Folder/LC09_L2SP_146041_20220514_20220516_02_T1_stacked.TIF'
```
