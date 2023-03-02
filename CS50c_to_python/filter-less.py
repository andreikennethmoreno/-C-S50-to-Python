from PIL import Image
from PIL import Image, ImageFilter

#imports image
original_img = Image.open('name_of_the_img.png')

#turns the image black ang white
black_and_white= original_img.convert('L')

#sepia color filter
sepia_img = original_img.convert('RGB')

width,height  = sepia_img.size

pixels = sepia_img.load()

def sepia(r,g,b):
    newr = int((0.393 * r) + (0.769 * g)  + (0.189 * b))
    newg = int((0.349 * r) + (0.686 * g) + (0.168 * b))
    newb = int((0.272 * r) + (0.534 * g) + (0.131 * b))
    return (newr,newg,newb)

for py in range(height):
    for px in range(width):
        r,g,b = sepia_img.getpixel((px,py))
        pixels[px,py] = sepia(r,g,b)

#blurs the image
blurImage = original_img.filter(ImageFilter.BLUR)

#mirrors the image
hori_flippedImage = original_img.transpose(Image.FLIP_LEFT_RIGHT)


#Outputs
original_img.show()

blurImage.show()

black_and_white.show()

hori_flippedImage.show()

sepia_img.show()
