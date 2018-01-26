from PIL import Image, ImageFilter
import os
    # loads image
image1 = Image.open('sample_image.jpg')
image2 = Image.open('dandelion.jpg')

    # shows iamge
#image2.show()
#image1.show()
    #saves the file in different format
#image1.save('sample_image.png')

# this lists all the files in the current folder.
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        print(f)
image2.convert(mode='L').save('modified_image2.jpg')
blurred_image = image1.filter(ImageFilter.GaussianBlur(15))
#blurred_image.show()
