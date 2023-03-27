from PIL import Image

input_image = Image.open("./x_train_4824/IMG_1089.BMP").convert("L")
pixels = input_image.load()
input_pixels = []
for i in range(input_image.size[1]):
    for j in range(input_image.size[0]):
        input_pixels.append(pixels[j, i] / 255)

for i in range(24):
    string = str(i) + " "
    for j in range(48):
        #print(mass[32 * i + j])
        if int(input_pixels[48 * i + j]) != 1.0:
            string += str("1")
        else:
            string += str("0")
    print(string)

print(" ")
for i in range(0, 24, 2):
    '''string = str(i) + " "
    for j in range(48):
        #print(mass[32 * i + j])
        if int(input_pixels[48 * i + j]) != 1.0:
            string += str("1")
        else:
            string += str("0")
    print(string)'''
    string = str(i) + " "
    for j in range(0, 48, 2):
        if(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            string += "1"
        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            string += "2"
    print(string)
