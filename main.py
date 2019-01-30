#!/usr/bin/env python

"""
Author: Vaibhav Kandwal
Website: www.vaibhavkandwal.com
Description: This script allows you to Square Fit an image, by adding white boders to deficient side! For usage and info, refer to Github Repo
"""

from PIL import Image
import ctypes
import os, os.path

if os.name == "nt":
    clearkey = "cls"
    ctypes.windll.kernel32.SetConsoleTitleA("Image 1:1 Resizer")
else:
    clearkey = "clear"

color = (255, 255, 255)  # background color, change (this is in rgb format)

term_width = os.get_terminal_size().columns

os.system(clearkey)
print("-" * term_width)
print("Image 1:1 Resizer".center(term_width))
print("-" * term_width)
print(
    "\nI will resize all your images to square shape automatically in a particular directory (no need to enter any width or height). I can also add colored background if shape is rectangular (Yay!). Happy Resizing! :D \n\n"
)


def squarefit(filename):
    old_im = Image.open(filename)  # open image file  
    sizew, sizeh = (
        old_im.size 
    )  # since size method gives a tuple, split result into two variables
    newbig = max(sizew, sizeh)
    new_im = Image.new("RGB", (newbig, newbig), color)  # create a new image with new size
    new_im.paste(old_im, (int((newbig - sizew) / 2), int((newbig - sizeh) / 2))) # paste image opened in first line onto the newly created image
    convertname = "converted/" + filename  # set filename with converted directory
    new_im.save(convertname)  # save the image


filelist = (
    []
)  # an array, that will contain list of all files to be converted. autopopulated below
validext = [".jpg", ".gif", ".png", ".tga", ".jpeg"]  # valid extensions to search for
loc = (
    input("Enter Directory Containing Images [Enter for current Directory]: ")
    or os.getcwd()
)


os.chdir(loc)  # changedir
for file in os.listdir(loc):  # find files which have valid extension
    ext = os.path.splitext(file)[1]
    if ext.lower() not in validext:
        continue
    filelist.append(file)  # add to filelist array

if len(filelist) != 0:
    if not os.path.exists("converted"):  # create directory if does not exist
        os.makedirs("converted")
    print("Working...")
    for i in range(0, len(filelist)):
        squarefit(filelist[i])  # run the function over list of files on loop
    os.system(clearkey)
    print('All Done! Check "converted" folder!')
else:
    os.system(clearkey)
    print(
        "Ummm, looks like directory does not contain any images! Did you type the correct path?\n\nPlease run the script again!"
    )
input("\nPress Enter to continue ...")
exit()
