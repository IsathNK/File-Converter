#Imports
from PIL import Image
import os
import re

#Convert PNG to JPG
def png_jpg(name , replace):
    im1 = Image.open(name)
    im1.save(replace + ".jpg") 

#Convert JPG to PNG
def jpg_png(name , replace):
    im1 = Image.open(name)
    im1.save(replace + '.png') 

#List Directories
dir = os.listdir()
for files in dir:
    print(files)

#User Inputs
name = input("Enter File Name: ")
replace = input("Enter Name For New File: ")

result = name.split('.')

#Calling Functions
if result[-1] == "jpg":
    jpg_png(name, replace)
elif result[-1] == "png":
    png_jpg(name, replace)
else:
    print("Unknown File")