from PIL import Image

input_image = Image.open("./test_output.BMP")
pixels = input_image.load()
input_pixels = []
for i in range(input_image.size[1]):
    for j in range(input_image.size[0]):
        if(pixels[j, i][0] == 255):
            input_pixels.append(0)
        else:
            input_pixels.append(1)
print(input_pixels)

for i in range(24):
    string = str(i) + " "
    for j in range(48):
        string += str(input_pixels[48 * i + j])

    print(string)

matrix = {"1" :  [0, 0, 0, 0],
          '2' :  [1, 0, 0, 0],
          '3' :  [0, 1, 0, 0],
          '4' :  [0, 0, 1, 0],
          '5' :  [0, 0, 0, 1],
          '6' :  [1, 1, 0, 0],
          '7' :  [1, 0, 1, 0],
          '8' :  [1, 0, 0, 1],
          '9' :  [0, 1, 1, 0],
          'a':  [0, 1, 0, 1],
          'b':  [0, 0, 1, 1],
          'c':  [1, 1, 1, 0],
          'd':  [1, 1, 0, 1],
          'e':  [1, 0, 1, 1],
          'f':  [0, 1, 1, 1],
          'g':  [1, 1, 1, 1]}

print(" ")
tmp_mass = []
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
    for j in range(0, 48, 2): #TODO finish changing coords. Start From 5 point
        if(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[(i * 48 + j + 2]) == 0 and int(input_pixels[i * 48 + j + 3]) == 0):
            tmp_mass.append("1")
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[(i * 48 + j + 2]) == 0 and int(input_pixels[i * 48 + j + 3]) == 0):
            tmp_mass.append('2')
        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48 * i + j + 1]) == 1 and int(input_pixels[(i * 48 + j + 2]) == 0 and int(input_pixels[(i * 48 + j + 3]) == 0):
            tmp_mass.append('3')
        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[i * 48 + j + 2]) == 1 and int(input_pixels[i * 48 + (j + 3]) == 0):
            tmp_mass.append('4')

        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[i * 48 + j + 2]) == 0 and int(input_pixels[i * 48 + j + 3]) == 1):
            tmp_mass.append('5')
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[i * 48 + j + 2]) == 0 and int(input_pixels[(i+1) * 48 + (j+1)]) == 0):
            tmp_mass.append('6')
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 0):
            tmp_mass.append('7')
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[(i+1) * 48 + j]) == 0 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('8')

        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 0):
            tmp_mass.append('9')
        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 0 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('a')
        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('b')
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 0):
            tmp_mass.append('c')

        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 0 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('d')
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 0 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('e')
        elif(int(input_pixels[48 *i + j]) == 0 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('f')
        elif(int(input_pixels[48 *i + j]) == 1 and int(input_pixels[48* i + j + 1]) == 1 and int(input_pixels[(i+1) * 48 + j]) == 1 and int(input_pixels[(i+1) * 48 + (j+1)]) == 1):
            tmp_mass.append('g')


    print(string)

for i in range(12):
    s = ""
    for j in range(24):
        s += str(tmp_mass[i * 24 + j])
    print(s)

print(len(tmp_mass) / 24)
print(len(tmp_mass))
def decrypt(in_mass):
    out_mass = []
    for i in range(48 * 24):
        out_mass.append(0)

    for i in range(12):
        for j in range(24):
            current_comb = matrix[tmp_mass[24 * i + j]]
            out_mass[24 * (2 * i) + 2 * j] = current_comb[0]
            out_mass[24 * (2 * i) + 2 * (j + 1)] = current_comb[1]
            out_mass[24 * (2 * (i + 1)) + 2 * j] = current_comb[2]
            out_mass[24 * (2 * (i + 1)) + 2 * (j + 1)] = current_comb[3]
    print(out_mass)
    for i in range(24):
        string = str(i) + " "
        for j in range(48):
            string += str(out_mass[48 * i + j])

        print(string)
decrypt(tmp_mass)
