from PIL import Image
import os

files = os.listdir("./y_train")
changes = os.listdir("./changes_origin_images_4824")

changes_2 = []
for i in changes:
    changes_2.append(i[:-4])

for i in files:
    print(i)
    if(i[:-4] in changes_2):
        print(22)
        os.remove("./changes_origin_images_4824/" + i[:-4] + ".JPG")
