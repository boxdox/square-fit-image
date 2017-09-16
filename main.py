#!/usr/bin/env python

'''
Author: Vaibhav Kandwal
Website: www.vaibhavkandwal.com
Description: This script allows you to Square Fit an image, by adding white boders to deficient side! For usage and info, refer to Github Repo
'''

from PIL import Image
import os, os.path

if os.name == 'nt':
	clearkey = 'cls'
else:
	clearkey = 'clear'

os.system(clearkey)
print '\n'+'{:^80}'.format('Image 1:1 Resizer')
print '-'*80
print '\nI will resize all your images to square shape automatically in a particular directory (no need to enter any width or height). I can also add colored background if shape is rectangular (Yay!). Happy Resizing! :D \n\n'



def squarefit(filename):
	old_im = Image.open(filename)
	old_size = old_im.size
	sizew, sizeh = old_im.size
	if (sizew>sizeh):
		newbig = sizew
	else:
		newbig = sizeh
	new_size = (newbig, newbig)
	new_im = Image.new("RGB", new_size, coll)
	new_im.paste(old_im, ((new_size[0]-old_size[0])/2,(new_size[1]-old_size[1])/2))
	convertname = 'converted/'+filename
	new_im.save(convertname)


filelist = []
validext = [".jpg",".gif",".png",".tga",".jpeg"]
loc = raw_input("Enter Directory Containing Images [Enter for current Directory]: ") or os.getcwd()
coll = (255,255,255)

os.chdir(loc)
for file in os.listdir(loc):
	ext = os.path.splitext(file)[1]
	if ext.lower() not in validext:
		continue
	filelist.append(file)

if (len(filelist)!=0):
	if not os.path.exists('converted'):
		os.makedirs('converted')
	print "Working..."
	for i in range(0, len(filelist)):
		squarefit(filelist[i])
	os.system(clearkey)
	print 'All Done! Check "converted" folder!'
else:
	os.system(clearkey)
	print 'Ummm, looks like directory does not contain any images! Did you type the correct path?\n\nPlease run the script again!'
raw_input("\nPress Enter to continue ...")
exit()
