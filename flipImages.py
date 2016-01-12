#!/usr/bin/python
'''
flipImages.py v0.01
=================
Flip images top and bottom
'''

import numpy as np
from PIL import Image
import glob, os, sys

def help():
    print "Usage : flipImages.py source_path dest_path"
    print "source_path : path of contains source images"
    print "dest_path : path for save result of fliped images"
    print "version : v0.01"
    print "Author : leorez <leorez@gmx.com>"

def flipImagesInCurDir(sub):
    root = sys.argv[2]+sub
    if not os.path.exists(root):
        os.makedirs(root)
        
    for file in glob.glob("*.bmp"):
        try:
            im = Image.open(file)
            print "%s, format: %s  mode: %s palette: %s" % (file, im.format, im.mode, im.palette)
            width, height =im.size
            print "The image size is %d x %d" % (width, height)
            
            out = im.transpose(Image.FLIP_TOP_BOTTOM)
            out.save(root+file)    
        except:
            print "Unable to open %s" % file
            exit(-1)

if len(sys.argv) < 3:
    help()
    exit(-1)

dataRoot = sys.argv[1]
os.chdir(dataRoot)
flipImagesInCurDir("/")
os.chdir(dataRoot+"/side")
flipImagesInCurDir("/side/")
