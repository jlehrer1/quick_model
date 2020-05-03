import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from tqdm import tqdm 
from sklearn.model_selection import KFold
import scrape

IMG_HEIGHT = 256
IMG_WIDTH = 256

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Use case: scrape.py <params file> <search term> <write location>')
        quit()
    
    # generate dataset for training
    scrape.generate_dataset(sys.argv[1], sys.argv[2], sys.argv[3])

    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.3)

    train_generator = image_generator.flow_from_directory(directory=sys.argv[3],
                                                        target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                        classes = [sys.argv[2]], #should come from script parameter
                                                        subset='training') 
    validation_generator = image_generator.flow_from_directory(directory=sys.argv[3],
                                                            target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                            classes= [sys.argv[2]],
                                                            subset='validation')

