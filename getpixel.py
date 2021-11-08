import numpy as np
import PIL
from PIL import Image

image = PIL.Image.open('./frames/frame0.jpg')

image_rgb = image.convert("RGB")
print(np.shape(image_rgb))

rgb_pixel_value = image_rgb.getpixel((330,390))
print(rgb_pixel_value)