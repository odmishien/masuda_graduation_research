from PIL import Image
import numpy as np
import os

images = os.listdir('./images')
for img in images:
    image = Image.open('./images/' + img, mode="r")
    image = image.resize((100,100))
    image.convert("L").save('./resized_images/' + img)