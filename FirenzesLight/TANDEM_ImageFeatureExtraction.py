'''
TANDEM 0.05 
Playing Around with Image Feature Extraction
Authors: Stephen Real and Christopher Vitale
Follow CVDH4 and SBReal on Twitter and Github
DH Praxis 14-15 CUNY Graduate Center
'''

import os
import cv2
import numpy as np

print
print 'Welcome to TANDEM 0.05 - Playing with Feature Extraction'
print

'''
Feature Extraction begins here

Let's find the mean values for each color channel as per PyImageSearch.

For now we will focus on global features and basic computer vision.
'''

img = cv2.imread('Firenzes-Light_Page_01.jpg')

print "Image Shape:"
print img.shape
print
print "Number of pixels:"
print img.size

'''
Color mean as per py image search
'''

print
print "RGB:"

means = cv2.mean(img)
print means

'''
Color mean and standard deviation of each channel
'''

print
print "Color Mean and Std Dev:"

(means, stds) = cv2.meanStdDev(img)

stats = np.concatenate([means,stds]).flatten()

print stats

