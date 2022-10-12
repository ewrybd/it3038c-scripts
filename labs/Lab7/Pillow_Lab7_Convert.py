from PIL import Image, ImageFilter
image = Image.open('testimage.jpeg')

print('Converting image from .jpeg to png')
image.save('testimage.png')