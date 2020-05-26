import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import SGD

import numpy as np
from sklearn.model_selection import KFold
import scrape
import preprocessing

import os
import sys
from tqdm import tqdm

IMG_HEIGHT = 256
IMG_WIDTH = 256
BATCH_SIZE = 20

def train_and_write_model(text):
    data_path = os.path.join('..', 'data')
    try:
        os.makedirs(data_path)
    except FileExistsError:
        tqdm.write('data directory exists, continuing...')
    return

if __name__ == "__main__":
    pass