from PIL import Image


im = Image.open(r'W:\TEST\frames\out-4988.jpg')


xmin= 1341
ymax = 1052
xmax= 1896
ymin = 737

im1 = im.crop((xmin, ymin, xmax,ymax ))
 
# Shows the image in image viewer
im1.show('checking.jpg')