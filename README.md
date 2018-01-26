# steganography
this is a project for collage final year

# cautions
Note that all our images will be in .png format.
This is because JPEG format compresses the image data,
which means that data encoded into the LSB may be lost.



# sample NOTES

load ------------------->

im.load()

Allocates storage for the image and loads it from the file (or from the source, for lazy operations). 
In normal cases, you don’t need to call this method, since the Image class automatically loads an opened image when it is accessed for the first time.

(New in 1.1.6) In 1.1.6 and later, load returns a pixel access object that can be used to read and modify pixels.
The access object behaves like a 2-dimensional array, so you can do:

pix = im.load()
print pix[x, y]
pix[x, y] = value
Access via this object is a lot faster than getpixel and putpixel.
