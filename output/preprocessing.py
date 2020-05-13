import os
from tqdm import tqdm
from PIL import Image

# Reshapes the images to be fed into the CNN.


def preprocess_dataset(class_directory, IMG_WIDTH, IMG_HEIGTH):
    """Preprocesses images for use in the classifier
        Usage:
            class_directory: path to the image folder
            IMG_WIDTH: width to change image to
            IMG_HEIGTH: heigth to change image to
    """
    tqdm.write('Preprocessing images in {}'.format(class_directory))
    for file in tqdm(os.listdir(class_directory)):
        try:
            img = Image.open(class_directory + '/{}'.format(file))
        except FileNotFoundError:
            print('{}, continuing...'.format(str(FileNotFoundError)))
        except PIL.UnidentifiedImageError:
            print('Pillow error {}'.format(str(PIL.UnidentifiedImageError)))

        img = img.resize((IMG_WIDTH, IMG_HEIGTH))
        img.save(class_directory + '/{}'.format(file))
