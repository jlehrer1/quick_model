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

# Size of images to be fed into CNN
IMG_HEIGHT = 256
IMG_WIDTH = 256
BATCH_SIZE = 20

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Use case: {} <params file> <search term> <model write location>'.format(
            sys.argv[0]))
        quit()

    data_path = os.path.join('..', 'data')
    try:
        os.makedirs(data_path)
    except FileExistsError:
        tqdm.write('data directory exists, continuing...')

    # generate dataset for training
    scrape.generate_dataset(sys.argv[1], sys.argv[2], data_path)

    # preprocess data
    preprocessing.preprocess_dataset(os.path.join(
        data_path, sys.argv[2]), IMG_WIDTH, IMG_HEIGHT)
    preprocessing.preprocess_dataset(os.path.join(
        data_path, 'NOT-{}'.format(sys.argv[2])), IMG_WIDTH, IMG_HEIGHT)

    # define datasets
    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        validation_split=0.3,
    )

    train_generator = image_generator.flow_from_directory(directory=data_path,
                                                          target_size=(
                                                              IMG_HEIGHT, IMG_WIDTH),
                                                          classes=[
                                                              sys.argv[2], 'NOT-{}'.format(sys.argv[2])],
                                                          subset='training',
                                                          shuffle=True)

    validation_generator = image_generator.flow_from_directory(directory=data_path,
                                                               target_size=(
                                                                   IMG_HEIGHT, IMG_WIDTH),
                                                               classes=[
                                                                   sys.argv[2], 'NOT-{}'.format(sys.argv[2])],
                                                               subset='validation',
                                                               shuffle=True)

    # define model
    model = keras.models.Sequential([
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(32, 2, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(256, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    opt = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(optimizer=opt,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # train model
    model.fit(
        train_generator,
        # steps_per_epoch = train_generator.samples // BATCH_SIZE,
        validation_data=validation_generator,
        # validation_steps = validation_generator.samples // BATCH_SIZE,
        epochs=30,
        callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    )

    # save to folder
    try:
        os.makedirs('model')
    except FileExistsError:
        tqdm.write('Directory exists, continuing...')
    model.save('model', overwrite=True, save_format='tf')
