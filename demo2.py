from PIL import Image, ImageFont, ImageDraw
import os
    # loads image
image = Image.open('pattern.png')
red_channel = image.split()[0]
new_image = Image.new("RGB",image.size)
new_image.show()
pixels = image.load()