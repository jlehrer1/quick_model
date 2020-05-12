import os
from tqdm import tqdm 
from PIL import Image

# Reshapes the images to be fed into the CNN. 

def preprocess_dataset(class_directory, IMG_WIDTH, IMG_HEIGTH):
    tqdm.write('Preprocessing images in {}'.format(class_directory))
    num_files = len(os.listdir(class_directory))
    for file in tqdm(os.listdir(class_directory)):
        try:
            img = Image.open(class_directory + '/{}'.format(file))
        except FileNotFoundError:
            print('{}, continuing...'.format(str(FileNotFoundError)))
        except PIL.UnidentifiedImageError:
            print('Pillow error {}'.format(str(PIL.UnidentifiedImageError)))

        img = img.resize((IMG_WIDTH, IMG_HEIGTH))
        img.save(class_directory + '/{}'.format(file))