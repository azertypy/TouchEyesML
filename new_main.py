import numpy as np

def activation(x):
	return 1/(1 + np.exp(-x))

def deriv_activ(y):
	return y * (1 - y)

def get_delta_error(right_out, y_out):
	return (y_out - right_out) * deriv_activ(y_out)

def new_weight(weight, output_n, delta_e, learning_rate):
	return weight - output_n * delta_e * learning_rate


l_rate = 0.1

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


def layer_evolve(input_layer, current_layer, w):
	for i in range(len(w)):
		summary = 0
		for j in range(len(w[i])):
			summary += input_layer[j] * w[i][j]
		current_layer[i] = activation(summary)

layer_evolve(layers[0], layers[1], weights[0])
layer_evolve(layers[1], layers[2], weights[1])
print(layers)

# обратное распространение ошибки весов 3-2(weights[1]). Ожидаемый ответ при [1, 1] - 0, 1
d_error = get_delta_error(0, layers[2][0])
print(d_error)

for i in range(len(layers[1])):
	weights[1][0][i] = weights[1][0][i] - layers[1][i] * d_error * l_rate

d_error = get_delta_error(1, layers[2][1])
print(d_error)

for i in range(len(layers[1])):
	weights[1][0][i] = weights[1][1][i] - layers[1][i] * d_error * l_rate

print(layers)
print("\n")
print(weights)

for i in range(len(layers[1])):
	d_error = weights[1][0][i] * d_error * deriv_activ(layers[1][i])
	print(d_error)
	for j in range(len(layers[0])):
		weights[0][i][j] = weights[0][i][j] - layers[0][j] * d_error * l_rate

print(weights)
print(layers)

