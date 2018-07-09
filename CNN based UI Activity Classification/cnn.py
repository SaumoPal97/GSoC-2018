import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Flatten, Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt

train_path = '/home/saumo/Desktop/screenshots/train/'
valid_path = '/home/saumo/Desktop/screenshots/valid/'
test_path = '/home/saumo/Desktop/screenshots/test/'

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224,224),classes=['login','onboarding','settings'],batch_size=5)
valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224,224),classes=['login','onboarding','settings'],batch_size=5)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224,224),classes=['login','onboarding','settings'],batch_size=27)

#simple model
model = Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(224,224,3)),
    Flatten(),
    Dense(3,activation='softmax'),
])

model.compile(Adam(lr=.0001),loss='categorical_crossentropy',metrics=['accuracy'])
model.fit_generator(train_batches,steps_per_epoch=720,validation_data=valid_batches,validation_steps=30,epochs=5,verbose=2)

#vgg16 model
vgg16_model = keras.applications.vgg16.VGG16()
model = Sequential()
for layer in vgg16_model.layers:
    model.add(layer)
model.layers.pop()
for layer in model.layers:
    layer.trainable = False
model.add(Dense(3,activation='softmax'))
model.compile(Adam(lr=.0001),loss='categorical_crossentropy',metrics=['accuracy'])
model.fit_generator(train_batches,steps_per_epoch=720,validation_data=valid_batches,validation_steps=30,epochs=5,verbose=2)

