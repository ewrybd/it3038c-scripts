from PIL import Image, ImageFilter
image = Image.open('testimage.jpeg')

print('Creating a thumbnail')
image.thumbnail((200, 200))
image.save('testimage_thumbnail.jpeg')