from PIL import Image, ImageFilter
image = Image.open('testimage.jpeg')

print('Finding the edges in the image')
edges_image = image.filter(ImageFilter.FIND_EDGES)
edges_image.save('testimage_edges.jpeg')