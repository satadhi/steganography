from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="hidden.png"):
    """Decodes the hidden message in an image
    file_location: the location of the image file to decode. By default is the provided encoded image in the images folder
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0,0,0)
    decoded_image.save("decoded_image.png")

    
if __name__ == '__main__':
    decode_image()    