from skimage import color
from skimage import io
import numpy as np
import os
from tqdm import tqdm 
from PIL import Image

# Reshapes the images to be fed into the CNN. 

def preprocess_dataset(class_directory):
    tqdm.tqdm.write('Preprocessing images in {}'.format(class_directory))
    num_files = len(os.listdir(class_directory))
    for file in tqdm(os.listdir(class_directory)):
        try:
            img = Image.open(class_directory + '/{}'.format(file))
        except FileNotFoundError:
            print('File not found... continuing')
        except PIL.UnidentifiedImageError:
            print('Pillow error {}'.format(str(PIL.UnidentifiedImageError)))
            
        img = img.resize((256, 256))
        img.save(class_directory + '/{}'.format(file))