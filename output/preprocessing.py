from skimage import color
from skimage import io
import numpy as np
import os
from tqdm import tqdm 
from PIL import Image

# Reshapes the images to be fed into the CNN. 

def preprocess_dataset(class_directory):
    num_files = len(os.listdir(class_directory))
    for file in tqdm(os.listdir(class_directory)):
        try:
            img = Image.open(class_directory + '/{}'.format(file))
        except:
            raise FileNotFoundError()
        img = img.resize((256, 256))
        img.save(class_directory + '/{}'.format(file))