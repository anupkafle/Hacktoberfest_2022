import os
from os import listdir
from PIL import Image
import requests
import shutil
 
# get the path/directory
folder_dir = "D:\Major Project on CBIR and Recommendation\Scrapping\DataSet\Daraz"

for images in os.listdir(folder_dir):
 
    filename = images
    # splitting the file name after the last '.'
    separator = '.'
    filename = filename.rsplit(separator, 1)[0]
    
    images = Image.open(f'D:\Major Project on CBIR and Recommendation\Scrapping\DataSet\Daraz\{images}')
    
    file_name = filename + '_30' + '.jpg'
    rotate_30 = images.rotate(30).save(file_name)
    
    file_name = filename + '_45' + '.jpg'
    rotate_45 = images.rotate(45).save(file_name)
    
    file_name = filename + '_60' + '.jpg'
    rotate_60 = images.rotate(60).save(file_name)

    