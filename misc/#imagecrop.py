

from PIL import Image


im = Image.open(r'W:\TEST\smallpubg.mp4frames\\1265.jpg')


xmin= 1475
ymax = 277
xmax= 1911
ymin = 0
			

im1 = im.crop((xmin, ymin, xmax,ymax ))
 
# Shows the image in image viewer

im1.show('W:\TEST\smallpubg.mp4frames\\1265.jpg')


