'''
TANDEM 0.05 
Playing Around with Image Feature Extraction
Authors: Stephen Real and Christopher Vitale
Follow CVDH4 and SBReal on Twitter and Github
DH Praxis 14-15 CUNY Graduate Center
'''
import csv
import os
import cv2
import numpy as np
import glob
from PIL import Image

print
print 'Welcome to TANDEM 0.05 - Playing with Feature Extraction'
print

#function captures location of image files
def get_input_folder():
    global good_input
    folder = raw_input('Enter the folder that contains your images: ');
    if os.path.isdir(folder):
        good_input = True
        return folder
    else:
        print ("Folder does not exist!")
        
#Feature Extraction Grunt Work
def image_extract(file):
	image_input = cv2.imread(file)
	image_output = image_input.shape
	return image_output
	
# Run Feature Extraction
def feature_extract(file):
	print ("Feature Extraction: " + file)
	fullpath = infolder + file
	ofile = os.path.splitext(file)[0]
	outfile = infolder + outfolder + '/' + ofile + '.csv'
	temp = open(outfile, 'w')
	temp.write(str(image_extract(fullpath)))
	temp.close()
	
# Make Feature Folder
def make_feature_folder(x):
    outname = 'features'
    count = 1
    while True:
        try:
            os.mkdir(x + outname)
            break
        except(OSError):
            outname = 'features' + str(count)
            count += 1
    return outname
        

#capture the folder that contains image files.
good_input = False
while good_input == False:
    infolder = get_input_folder()

#create the output folder
outfolder = make_feature_folder(infolder)

#loop through the user's input folder and find image files
#for testing purposes only work with PNG files now
outcount = 1
print
print ("processing image files in " + infolder)
print


files = [ f for f in os.listdir(infolder) if os.path.isfile(os.path.join(infolder,f)) ]
for file in files:
    if os.path.splitext(file)[1] == '.tiff':
        feature_extract(file)
        outcount += 1
    elif os.path.splitext(file)[1] == '.jpg':
        feature_extract(file)
        outcount += 1
    elif os.path.splitext(file)[1] == '.png':
        feature_extract(file)
        outcount += 1
    else:
       print
       print (file + " is not an image file. Skipped... ")