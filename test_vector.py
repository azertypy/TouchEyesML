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
print(out_mass_nums)
