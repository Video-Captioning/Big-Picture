# Adapted from https://gist.github.com/npenzin/f884aa0258db6cc76639
from PIL import Image, ImageOps
#from wand.image import Image as wimage
import os
import sys
import glob
import zlib

import numpy as np
 
PATH = './img/'
IMAGES = glob.glob(PATH+'*.png')
COLS = 2
ROWS = 2
DEFAULT_SIZE = 600
DEFAULT_PADDING = 60
DEFAULT_BACKGOUND_COLOR = '#fafafa'

class Collage(object):
    def __init__(self, args):
        """initialize"""
        self.path = args['path']
        self.images = args['images']
        self.cols = args['cols']
        self.rows = args['rows']
        self.def_size = args['def_size']
        self.def_pad = args['def_pad']
        self.def_bg_color = args['def_bg_color']
        self.canvas_size = (
            self.def_size*self.cols + ((self.cols + 1) * self.def_pad),
            self.def_size*self.rows + ((self.rows + 1) * self.def_pad))
        self._create()

    def _create(self):
        """Build a collage"""
        self.canvas = Image.new('RGB', self.canvas_size, self.def_bg_color)
        for img_n, img_fn in enumerate(self.images):
            # open img
            temp_img = Image.open(img_fn)
            # crop if not square
            temp_img = self._crop_img(temp_img)
            # resize to default size square
            temp_img = temp_img.resize((DEFAULT_SIZE, DEFAULT_SIZE), Image.ANTIALIAS)
            # doing layout math
            left_margin = img_n % self.cols * (self.def_size + self.def_pad) + self.def_pad
            top_margin = img_n // self.cols * (self.def_size + self.def_pad) + self.def_pad
            box = (left_margin, top_margin)
            self.canvas.paste(temp_img, box)

    def _crop_img(self, image_to_crop):
        """Crop the given image"""
        temp_img = image_to_crop

        # if image is not square, then crop center
        if temp_img.width != temp_img.height:
            if temp_img.width > temp_img.height:
                left = temp_img.width/2 - temp_img.height/2
                upper = 0
                right = temp_img.width/2 + temp_img.height/2
                lower = temp_img.height
                box = (left, upper, right, lower)
                temp_img = temp_img.crop(box)
            else:
                left = 0
                upper = temp_img.height/2 - temp_img.width/2
                right = temp_img.width
                lower = temp_img.height/2 + temp_img.width/2
                box = (left, upper, right, lower)
                temp_img = temp_img.crop(box)

        return temp_img

    def show(self):
        """Show the collage"""
        self.canvas.show()
        return

    def save_to_file( self, file_name ):
        """Save the collage to a file"""
        img = self.canvas
        img.save( file_name )
        img.close()
        return

if __name__ == '__main__':
    params = {
        'path': PATH,
        'images': IMAGES,
        'cols': COLS,
        'rows': ROWS,
        'def_size': DEFAULT_SIZE,
        'def_pad': DEFAULT_PADDING,
        'def_bg_color': DEFAULT_BACKGOUND_COLOR
    }
    collage = Collage(params)
    collage.show()
