'''
TANDEM 0.05 
Playing Around with Image Feature Extraction
Authors: Stephen Real and Christopher Vitale
Follow CVDH4 and SBReal on Twitter and Github
DH Praxis 14-15 CUNY Graduate Center
'''
import os
import cv

corpus_root = raw_input('Select your Corpus: ');

corpus_files = os.listdir(corpus_root)

for files in corpus_files:
	print files