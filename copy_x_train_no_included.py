import os
y_train_base = os.listdir("./y_train/")

x_train_base = os.listdir("./x_train_4824/")

y_train = []
x_train = []


not_included_x = []

for i in y_train_base:
	y_train.append(i[:-4])

for i in x_train_base:
	x_train.append(i[:-4])

for i in y_train:
	if i not in x_train:
		not_included_x.append(i)

print(not_included_x)

for i in not_included_x:
	os.popen("cp ./changes_origin_images_4824/" + i + ".JPG ./x_train_4824/" + i + ".JPG")