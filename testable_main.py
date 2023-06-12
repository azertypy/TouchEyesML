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
	input_image = Image.open(path)
	pixels = input_image.load()
	input_pixels = []
	for i in range(input_image.size[1]):
	    for j in range(input_image.size[0]):
	        if(pixels[j, i][0] == 255):
	            input_pixels.append(0)
	        else:
	            input_pixels.append(1)

	matrix = {"0" :  [0, 0, 0, 0],
	          '1' :  [1, 0, 0, 0],
	          '2' :  [0, 1, 0, 0],
	          '3' :  [0, 0, 1, 0],
	          '4' :  [0, 0, 0, 1],
	          '5' :  [1, 1, 0, 0],
	          '6' :  [1, 0, 1, 0],
	          '7' :  [1, 0, 0, 1],
	          '8' :  [0, 1, 1, 0],
	          '9':  [0, 1, 0, 1],
	          'a':  [0, 0, 1, 1],
	          'b':  [1, 1, 1, 0],
	          'c':  [1, 1, 0, 1],
	          'd':  [1, 0, 1, 1],
	          'e':  [0, 1, 1, 1],
	          'f':  [1, 1, 1, 1]}

	nums = {'0' : 0,
	        '1' : 100,
	        '2' : 200,
	        '3' : 300,
	        '4' : 400,
	        '5' : 500,
	        '6' : 600,
	        '7' : 700,
	        '8' : 800,
	        '9' : 900,
	        'a' : 1000,
	        'b' : 1100,
	        'c' : 1200,
	        'd' : 1300,
	        'e' : 1400,
	        'f' : 1500}

	tmp_mass = []
	for i in range(0, 24):
	    for j in range(0, 48, 4):
	        if(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("0")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("1")
	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("2")
	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("3")

	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("4")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("5")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("6")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("7")

	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("8")
	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("9")
	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("a")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 0): tmp_mass.append("b")

	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 0 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("c")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 0 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("d")
	        elif(input_pixels[48 * i + j] == 0 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("e")
	        elif(input_pixels[48 * i + j] == 1 and input_pixels[48 * i + j + 1] == 1 and input_pixels[48 * i + j + 2] == 1 and input_pixels[48 * i + j + 3] == 1): tmp_mass.append("f")

	out_mass = []
	for i in range(24 * 12):
	    data = matrix[tmp_mass[i]]
	    out_mass.append(data[0])
	    out_mass.append(data[1])
	    out_mass.append(data[2])
	    out_mass.append(data[3])

	for i in range(24):
	    s = ""
	    for j in range(12):
	        s += str(out_mass[i * 24 + j])
	    #print(s)

	out_mass_nums = []
	for i in range(24 * 12):
	    #print(out_mass[i])
	    #print(nums["f"])
	    out_mass_nums.append(nums[str(tmp_mass[i])])

	#print(out_mass_nums)
	return out_mass_nums


import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

x_files = os.listdir("./x_train_4824_old/")
y_files = os.listdir("./y_train/")

input_pixels = []
output_pixels = []

import random
def get_input():
	return create_input_pixels("./x_train_4824/" + random.choice(x_files))

def get_output():
	return create_output_pixels("./y_train/" + random.choice(у_files))



model = keras.Sequential([
	keras.Input((1152)),
	keras.layers.Dense(800, activation = tf.nn.relu),
	keras.layers.Dense(450, activation = tf.nn.relu),
	keras.layers.Dense(288, activation = tf.nn.relu)
	])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate = 0.0008),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.load_weights("Weights")

matrix = {"0" :  [0, 0, 0, 0],
		  '1' :  [1, 0, 0, 0],
		  '2' :  [0, 1, 0, 0],
		  '3' :  [0, 0, 1, 0],
		  '4' :  [0, 0, 0, 1],
		  '5' :  [1, 1, 0, 0],
		  '6' :  [1, 0, 1, 0],
		  '7' :  [1, 0, 0, 1],
		  '8' :  [0, 1, 1, 0],
		  '9':  [0, 1, 0, 1],
		  'a':  [0, 0, 1, 1],
		  'b':  [1, 1, 1, 0],
		  'c':  [1, 1, 0, 1],
		  'd':  [1, 0, 1, 1],
		  'e':  [0, 1, 1, 1],
		  'f':  [1, 1, 1, 1]}

np.set_printoptions(threshold=np.sys.maxsize)
image = random.choice(x_files)[:-4]
print(image)
input_p = create_input_pixels("./x_train_4824_old/" + image + ".JPG")
layer = model.predict_step(np.array([input_p]))
print(layer)
for i in range(24):
	string = ""
	for j in range(12):
		x = layer[0][12 * i + j]
		if(x <= 50):
			data = matrix["0"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 50 and x <= 150):
			data = matrix["1"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 150 and x <= 250):
			data = matrix["2"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 250 and x <= 350):
			data = matrix["3"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])

		elif(x > 350 and x <= 450):
			data = matrix["4"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 450 and x <= 550):
			data = matrix["5"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 550 and x <= 650):
			data = matrix["6"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 650 and x <= 750):
			data = matrix["7"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])

		elif(x > 750 and x <= 850):
			data = matrix["8"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 850 and x <= 950):
			data = matrix["9"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 950 and x <= 1050):
			data = matrix["a"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 1050 and x <= 1150):
			data = matrix["b"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])

		elif(x > 1150 and x <= 1250):
			data = matrix["c"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 1250 and x <= 1350):
			data = matrix["d"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 1350 and x <= 1450):
			data = matrix["e"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])
		elif(x > 1450):
			data = matrix["f"]
			string += str(data[0]) + str(data[1]) + str(data[2])+ str(data[3])

	print(string)

print("\n")
