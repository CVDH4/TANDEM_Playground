__author__ = 'sr-cv'
'''
TANDEM 0.05 - Image Extraction
Authors: Stephen Real and Christopher Vitale
Follow CVDH4 and SBReal on Twitter and Github
DH Praxis 14-15 CUNY Graduate Center
'''
import os
import cv2
import numpy as np
import glob
from PIL import Image
import csv

#initialize output file open switch
outputopen = False


print
print 'Welcome to TANDEM 0.05 - Feature Extraction'
print

'''***********************************************
***                                              *
*** NOW DEFINE ALL THE IMAGE EXTRACTION FUNCTIONS*
***                                              *
***********************************************'''

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
	image_size = image_input.size
	image_shape = image_input.shape
	image_rgbmean = cv2.mean(image_input)
	return image_size, image_shape, image_rgbmean
	
# Run Feature Extraction
def feature_extract(fullpath, file):
	print ("Feature Extraction: " + file)
	fullpath = infolder + file
	ofile = os.path.splitext(file)[0]
	outfile = infolder + outfolder + '/' + ofile + '.csv'
	temp = open(outfile, 'w')
	temp.write(str(image_extract(fullpath)))
	temp.close()
	
	
	
def write_first_row(outname):               #write the first row of the main output file
    global outputopen, file, resultspath

    print outname
    with open(outname, 'wb') as csvfile:
            tandemwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            tandemwriter.writerow(['File','Image Shape', 'Image Size', 'Image Mean RGB'])
            tandemwriter.writerow([file]+[image_shape]+[image_size]+[image_rgbmean])

    outputopen = True
    write_the_lists()

def write_the_rest(outname):                #write subsequent rows of main output file
    global file
    with open(outname, 'a') as csvfile:
            tandemwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            tandemwriter.writerow([file]+[image_shape]+[image_size]+[image_rgbmean])
    write_the_lists()

#Convert PDF to TXT	
def pdfconvert(fullpath, file, pages=None):     
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fullpath, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()

    ofile = os.path.splitext(file)[0]
    outfile = outpath + outfolder + '/' + ofile + '.txt'
    text = output.getvalue()
    output.close
    temp = open(outfile, 'w')
    temp.write (text)
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
            print "could not create folder ", x + outname, "...retrying..."
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
    print ("Processing " + file)
    fullpath = infolder + file
    if os.path.splitext(file)[1] == '.tiff':
        feature_extract(fullpath, file)
        outcount += 1
    elif os.path.splitext(file)[1] == '.jpg':
        feature_extract(fullpath, file)
        outcount += 1
    elif os.path.splitext(file)[1] == '.png':
        feature_extract(fullpath, file)
        outcount += 1
    elif os.path.splitext(file)[1] == '.pdf':
        pdfconvert(fullpath, file)
    else:
       print "\n", file + " is not an image file. Skipped... "

    #write the results of nltk process to csv files
    resultspath = './'
    outfile = resultspath + 'tandem' + 'image.csv'
    if outputopen:
        write_the_rest(outfile)
    else:
        write_first_row(outfile)
