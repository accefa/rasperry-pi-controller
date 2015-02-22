# coding=utf-8
'''
Created on 21.02.2015

@author: Fabian Wüthrich
'''

from PIL import Image

img = Image.open("image.png")
height = 400
width = img.size[0]
threshold = 30

for x in range(0, width):
    xy = (x, height)
    rgb = img.getpixel(xy)

    if(rgb[0] < threshold):
        # Langsam!
        img.putpixel(xy, (255,0,0))
    
img.show()


if __name__ == '__main__':
    pass
