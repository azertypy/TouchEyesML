import numpy as np
import os
import random

def activation(x):
	if x >= 0 and x <= 1:
		return x
	elif x < 0:
		return 0.002 * x
	else:
		return 1 + 0.002 * (x - 1)

def deriv_activ(x):
	if x >= 0 and x <= 1:
		return 1
	else:
		return 0.002

images = []
tmp = os.listdir("./y_train/")
print(tmp)
for i in tmp:
	images.append(i[:-4])
print(images)

def get_random_image():
	return random.choice(images)


def get_delta_error(right_out, y_out):
	return (y_out - right_out) * deriv_activ(y_out)

def new_weight(weight, output_n, delta_e, learning_rate):
	return weight - output_n * delta_e * learning_rate

from PIL import Image

def create_input_pixels(path):
	input_image = Image.open(path).convert("L")
	pixels = input_image.load()
	input_pixels = []
	for i in range(input_image.size[1]):
		for j in range(input_image.size[0]):
			input_pixels.append(pixels[j, i] / 255)

	return input_pixels
'''
def create_output_pixels(path):
	image = Image.open(path)
	pixels = image.load()

	output_pixels = []
	for i in range(image.size[1]):
		for j in range(image.size[0]):
			if(pixels[j, i][0] == 255):
				output_pixels.append(0)
			else:
				output_pixels.append(255)

	return output_pixels
'''
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

	return out_mass_nums



l_rate = 0.001
'''
layers = [
			[1, 1],
			[0, 0, 0],
			[0 , 1]
		 ]

#inp-l2
#l2-out
weights = [
		   [
		    [1.4, 0.2], #1-3 2-3
			[0.1, 0.3], #1-4 2-4
			[0.5, 0.2]  #1-5 2-5
		   ],
		   [
		    [0.2, 0.1, 0.3], #3-6 4-6 5-6
		   	[0.1, 0.2, 0.4]
		   ]
		  ]
'''

layers = []

#creating layers. TODO: Optimize this plz
tmp_mass = []
for i in range(1152):
	tmp_mass.append(0)
layers.append(tmp_mass)

tmp_mass = []
for i in range(500):
	tmp_mass.append(0)
layers.append(tmp_mass)

tmp_mass = []
for i in range(350):
	tmp_mass.append(0)
layers.append(tmp_mass)

tmp_mass = []
for i in range(288):
	tmp_mass.append(0)
layers.append(tmp_mass)

print("layers_len:")
for i in range(4):
	print("	", i, len(layers[i]))

weights = []

tmp_mass = []
for i in range(len(layers[1])):
	tmp2_mass = []
	for j in range(len(layers[0])):
		tmp2_mass.append(random.randint(0, 100) / 100)
	tmp_mass.append(tmp2_mass)
weights.append(tmp_mass)

tmp_mass = []
for i in range(len(layers[2])):
	tmp2_mass = []
	for j in range(len(layers[1])):
		tmp2_mass.append(random.randint(0, 100) / 100)
	tmp_mass.append(tmp2_mass)
weights.append(tmp_mass)

tmp_mass = []
for i in range(len(layers[3])):
	tmp2_mass = []
	for j in range(len(layers[2])):
		tmp2_mass.append(random.randint(0, 100) / 100)
	tmp_mass.append(tmp2_mass)
weights.append(tmp_mass)


def layer_evolve(input_layer, current_layer, w):
	for i in range(len(w)):
		summary = 0
		for j in range(len(w[i])):
			summary += input_layer[j] * w[i][j]
			#print(i, j, input_layer[j], w[i][j])
			#print(input_layer[j] * w[i][j])
		#print(summary)
		current_layer[i] = activation(summary)


def back_evolve(right_out):
	#right_out = [0, 1]
	weights_out_delta = []

	for i in range(len(layers[3])):
		weights_out_delta.append((layers[3][i] - right_out[i]) * deriv_activ(layers[3][i]))

	#print(weights_out_delta)
	#print(weights_out_delta)
	#input()
	for i in range(len(weights[2])):
		for j in range(len(layers[3])):
			#print(j)
			#print(len(weights[2][i]))
			#print(layers[3][j])
			weights[2][i][j] = weights[2][i][j] - layers[3][j] * weights_out_delta[i] * l_rate
	'''
	print("\n weights")
	for i in weights:
		for j in i:
			print(j)
		print("\n")
	'''

	delta_w_layer_3 = []
	for i in range(len(layers[2])):
		tmp_error = 0
		for j in range(len(weights_out_delta)):
			tmp_error += weights[2][j][i] * weights_out_delta[j]
		delta_w_layer_3.append(tmp_error * deriv_activ(layers[2][i]))

	#print("delta w 3 layer")
	#print(delta_w_layer_3)
	#input()
	for i in range(len(weights[1])):
		for j in range(len(layers[2])):
			#print(layers[0][j])
			weights[1][i][j] = weights[1][i][j] - layers[1][j] * delta_w_layer_3[i] * l_rate

	delta_w_layer_2 = []
	for i in range(len(layers[1])):
		tmp_error = 0
		for j in range(len(delta_w_layer_3)):
			tmp_error += weights[1][j][i] * delta_w_layer_3[j]
		delta_w_layer_2.append(tmp_error * deriv_activ(layers[1][i]))

	#print("delta w 2 layer")
	#print(delta_w_layer_2)
	#input()
	for i in range(len(weights[0])):
		for j in range(len(layers[1])):
			#print(layers[0][j])
			weights[0][i][j] = weights[0][i][j] - layers[0][j] * delta_w_layer_2[i] * l_rate

import time
import math
epoches = int(input("SET NUM OF EPOCHES"))
last_weights = weights
pre_last_weights = weights
weights_backup = []
num_of_nan = 0
for i in range(epoches):
	#print(i)
	image = get_random_image()
	#print(image)
	layers[0] = create_input_pixels("./x_train_4824_old/"+image+".JPG")
	#print("layer 0", layers[0])
	s_t = time.time()
	layer_evolve(layers[0], layers[1], weights[0])
	#print("layer 0 after evolve", layers[0])
	#print("layer 1", layers[1])
	layer_evolve(layers[1], layers[2], weights[1])
	#print("layer 1 after evolve", layers[1])
	#print("layer 2", layers[2])
	layer_evolve(layers[2], layers[3], weights[2])

	if num_of_nan == 2:
		print("ERROR: Double NaN found. Load pre-last numeric weights")
		weights = pre_last_weights
		print("layer 3 0", layers[3][0])
		for i in range(0, len(weights_backup), -1):
			if(not(math.nan in weights_backup[i])):
				weights = weights_backup[i]
		continue
	if(math.isnan(layers[3][0]) or layers[3][0] > 1700 or layers[3][0] < -100):
		print("ERROR: Weights is NaN or over 3000 found. Load last numeric weights")
		for i in range(0, len(weights_backup), -1):
			if(not(math.nan in weights_backup[i])):
				weights = weights_backup[i]
		continue
		num_of_nan += 1
		print("layer 3 0", layers[3][0])
		continue

	num_of_nan = 0
	pre_last_weights = last_weights
	last_weights = weights
	if(i % 100 == 0):
		weights_backup.append(weights)
	t_s = time.time()- s_t
	#print(layers[2])
	#print(create_output_pixels("./x_train_4824/IMG_1089.BMP"))
	back_evolve(create_output_pixels("./y_train/" + image + ".BMP"))
	#print("complete", i / epoches * 100, "%")
	print("\n", i, image, ", evole time = ", t_s, ", back_evolve time = ", time.time() - s_t, ", complete", i / epoches * 100, "%")
	print("	layer 3 0", layers[3][0])
	if(i % 10 == 0):
		pass#print(layers[3])
		'''for i in range(24):
			string = ""
			for j in range(48):
				#print(mass[32 * i + j])
				if float(layers[3][48 * i + j]) >= 128:
					string += str("1")
				else:
					string += str("0")
			print(string)'''

def test_neural(path):
	layers[0] = create_input_pixels(path)
	layer_evolve(layers[0], layers[1], weights[0])
	layer_evolve(layers[1], layers[2], weights[1])
	layer_evolve(layers[2], layers[3], weights[2])

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
	print(layers[3])
	for i in range(24):
		string = ""
		for j in range(12):
			x = layers[3][12 * i + j]
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

img = get_random_image()
print(img)
test_neural("./x_train_4824_old/" + img + ".JPG")
print("\n")
img = get_random_image()
print(img)
test_neural("./x_train_4824_old/" + img + ".JPG")
print("\n")
img = get_random_image()
print(img)
test_neural("./x_train_4824_old/" + img + ".JPG")
print("\n")
