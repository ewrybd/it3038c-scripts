from PIL import Image, ImageFilter
image = Image.open('testimage.jpeg')

print('Blurring the image')
blurimage = image.filter(ImageFilter.GaussianBlur(5))
blurimage.save('testimage_blur.jpeg')