from PIL import Image

def create_input_pixels(path):
	input_image = Image.open(path).convert("L")
	pixels = input_image.load()
	input_pixels = []
	for i in range(input_image.size[1]):
		for j in range(input_image.size[0]):
			input_pixels.append(pixels[j, i] / 255)

	return input_pixels

def create_output_pixels(path):
	image = Image.open(path)
	pixels = image.load()

	output_pixels = []
	for i in range(image.size[1]):
		for j in range(image.size[0]):
			if(pixels[j, i][0] == 255):
				output_pixels.append(0)
			else:
				output_pixels.append(1)

	return output_pixels

import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

x_files = os.listdir("./x_train_4824/")
y_files = os.listdir("./y_train/")

input_pixels = []
output_pixels = []

#for i in x_files:
#	file_name = i[:-4]
#	print(file_name)
#	input_pixels.append(create_input_pixels("./x_train_4824/" + file_name + ".JPG"))
#	output_pixels.append(create_output_pixels("./y_train/" + file_name + ".bmp"))

import random
def get_input():
	return create_input_pixels("./x_train_4824/" + random.choice(x_files) + ".JPG")

def get_output():
	return create_output_pixels("./y_train/" + random.choice(x_files) + ".bmp")

model = keras.Sequential([
	keras.Input((1152)),
	keras.layers.Dense(10000, activation = tf.nn.relu),
	keras.layers.Dense(500, activation = tf.nn.relu),
	keras.layers.Dense(1152, activation = tf.nn.relu)
	])

model.compile(optimizer=tf.keras.optimizers.Adam(), 
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#model.fit(np.array(input_pixels), np.array(output_pixels), epochs = 2500)

model.fit(lambda: get_input(), lambda: output_pixels(), epochs = 100)

input_image = Image.open("changes_origin_images_4824/IMG_1144.JPG").convert("L")
pixels = input_image.load()
input_pixels = []
for i in range(input_image.size[1]):
	for j in range(input_image.size[0]):
		input_pixels.append(pixels[j, i] / 255)

np.set_printoptions(threshold=np.sys.maxsize)
print(model.predict_step(np.array([input_pixels]))[0])
model.save_weights("./Weights")