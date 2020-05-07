import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from tqdm import tqdm 
from sklearn.model_selection import KFold

import scrape, preprocessing

# Size of images to be fed into CNN
IMG_HEIGHT = 256
IMG_WIDTH = 256
BATCH_SIZE=20

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Use case: {} <params file> <search term> <write location>'.format(sys.argv[0]))
        quit()
    
    
    # generate dataset for training
    scrape.generate_dataset(sys.argv[1], sys.argv[2], sys.argv[3])

    # preprocess data
    preprocessing.preprocess_dataset(sys.argv[3] + '/{}'.format(sys.argv[2]), IMG_WIDTH, IMG_HEIGHT)
    preprocessing.preprocess_dataset(sys.argv[3] + '/NOT-{}'.format(sys.argv[2]), IMG_WIDTH, IMG_HEIGHT)

    # define datasets 
    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.3)

    train_generator = image_generator.flow_from_directory(directory=sys.argv[3],
                                                        target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                        classes = [sys.argv[2]], 
                                                        subset='training') 
    validation_generator = image_generator.flow_from_directory(directory=sys.argv[3],
                                                            target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                            classes= [sys.argv[2]],
                                                            subset='validation')

    # define model
    model = keras.models.Sequential([
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(128, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(32, 2, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    opt = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(optimizer=opt,
                loss='binary_crossentropy',
                metrics=['accuracy'])
    
    # train model
    model.fit_generator(
        train_generator,
        steps_per_epoch = train_generator.samples // BATCH_SIZE,
        validation_data = validation_generator, 
        validation_steps = validation_generator.samples // BATCH_SIZE,
        epochs = 5,
    )

    try:
        os.makedirs('models/')
    except FileExistsError:
        print('Directory exists, continuing...')
        
    model.save('models/', overwrite = False, save_format = 'tf')


