

from PIL import Image


im = Image.open(r'W:\TEST\frames\3681.jpg')


xmin= 1
ymax = 1500
xmax= 1500
ymin = 310

im1 = im.crop((xmin, ymin, xmax,ymax ))
 
# Shows the image in image viewer

im1.show('W:\TEST/frames_cropped\966.jpg')