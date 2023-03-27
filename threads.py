import numpy as np
import os
import random
import multiprocessing


def activation(x):
	if x >= 0 and x <= 1:
		return x
	elif x < 0:
		return 0.005 * x
	else:
		return 1 + 0.005 * (x - 1)

def deriv_activ(x):
	if x >= 0 and x <= 1:
		return 1
	else:
		return 0.005

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




l_rate = 0.01
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
for i in range(1500):
	tmp_mass.append(0)
layers.append(tmp_mass)

tmp_mass = []
for i in range(500):
	tmp_mass.append(0)
layers.append(tmp_mass)

tmp_mass = []
for i in range(1152):
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

print(len(weights))
print(len(weights[0]))
print(len(weights[0][0]))

def layer_evolve(input_layer, current_layer, w, start, step):
    for i in range(start, len(w), step):
        summary = 0
        #if(start == 1):
        #    print(start, i)
        for j in range(len(w[i])):
            summary += input_layer[j] * w[i][j]
            #print(i, j, input_layer[j], w[i][j])
            #print(input_layer[j] * w[i][j])
            #print(summary)
        current_layer[i] = activation(summary)
        #print(start)

def create_threads(num, input_layer, current_layer, w):
    processes = []
    for i in range(num):
        processes.append(multiprocessing.Process(target=layer_evolve, args=(input_layer, current_layer, w, i, num)))

    for thread in processes:
        thread.start()  # каждый поток должен быть запущен
    for thread in processes:
        thread.join()



def back_evolve(right_out):
	#right_out = [0, 1]
	weights_out_delta = []

	for i in range(len(layers[3])):
		weights_out_delta.append((layers[3][i] - right_out[i]) * deriv_activ(layers[3][i]))

	#print(weights_out_delta)
	#print(weights_out_delta)
	#input()
	for i in range(len(weights[2])):
		for j in range(len(weights[2][i])):
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
		for j in range(len(weights[1][i])):
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
		for j in range(len(weights[0][i])):
			#print(layers[0][j])
			weights[0][i][j] = weights[0][i][j] - layers[0][j] * delta_w_layer_2[i] * l_rate

for i in range(100):
	print(i)
	image = get_random_image()
	print(image)
	layers[0] = create_input_pixels("./changes_origin_images_4824/IMG_1089.JPG")#("./x_train_4824_old/"+image+".JPG")
	#print("layer 0", layers[0])

	#layer_evolve(layers[0], layers[1], weights[0])
	#print("layer 0 after evolve", layers[0])
	#print("layer 1", layers[1])
	#layer_evolve(layers[1], layers[2], weights[1])
	#print("layer 1 after evolve", layers[1])
	#print("layer 2", layers[2])
	#layer_evolve(layers[2], layers[3], weights[2])

	create_threads(10,layers[0], layers[1], weights[0])
	create_threads(10,layers[1], layers[2], weights[1])
	create_threads(10,layers[2], layers[3], weights[2])
	print("layer 3", layers[3][0])

	#print(layers[2])
	#print(create_output_pixels("./x_train_4824/IMG_1089.BMP"))
	back_evolve(create_output_pixels("./x_train_4824/IMG_1089.BMP"))
	print(weights[0][1][0])
	if(i % 10 == 0):
		#print(layers[3])
		for i in range(24):
			string = ""
			for j in range(48):
				#print(mass[32 * i + j])
				if float(layers[3][48 * i + j]) >= 128:
					string += str("1")
				else:
					string += str("0")
			print(string)

layers[0] = create_input_pixels("./changes_origin_images_4824/IMG_1089.JPG")
layer_evolve(layers[0], layers[1], weights[0])
layer_evolve(layers[1], layers[2], weights[1])
layer_evolve(layers[2], layers[3], weights[2])

print(layers[3])
for i in range(24):
	string = ""
	for j in range(48):
		#print(mass[32 * i + j])
		if float(layers[3][48 * i + j]) >= 128:
			string += str("1")
		else:
			string += str("0")
	print(string)

print("\n")
