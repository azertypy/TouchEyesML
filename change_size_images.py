import os
images = os.listdir("./origin_images")

from PIL import Image
for i in images:
	image = Image.open("./origin_images/" + i)
	new_image = image.resize((48, 24))
	new_image.save("./changes_origin_images_4824/" + i)
