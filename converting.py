from PIL import Image
import os

files = os.listdir("./y_train")

print(files)
for i in files:
    img = Image.open("./y_train/" + i)
    print(i[:-4])
    img.save("./y_train/" + i[:-4] + ".BMP")
