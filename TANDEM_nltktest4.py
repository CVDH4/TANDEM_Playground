'''
TANDEM 0.05 
Playing Around with NLTK
Authors: Stephen Real and Christopher Vitale
Follow CVDH4 and SBReal on Twitter and Github
DH Praxis 14-15 CUNY Graduate Center
'''

__author__ = 'sbr-cv'

import csv

print
print 'Welcome to TANDEM 0.05 - Playing with NLTK'
print


'''
For now, select your own corpus root by typing 
the directory name.

Once the OCR step is completed, it will use the output file 
directory as a corpus root.
'''


from nltk.corpus import PlaintextCorpusReader
corpus_root = raw_input('Select your Corpus: ');
doc_text = PlaintextCorpusReader(corpus_root, '.*');

print 'Your corpus is: %s' % corpus_root;
print
print 'It includes: '
print doc_text.fileids()
print


'''
The next step assigns each file in the directory 
to a variable
'''


print "Files in Corpus"
print

import os

corpus_files = os.listdir(corpus_root)

for files in corpus_files:
	print files

	
	
'''
The next step runs NLTK data queries against 
each variable we defined in the previous step.
'''

data1 = [len(doc_text.words('1_welcometonewyork.txt'))]
data2 = [len(doc_text.words('2_blankspace.txt'))]
data3 = [len(doc_text.words('3_style.txt'))]
data4 = [len(doc_text.words('4_outofthewoods.txt'))]
data5 = [len(doc_text.words('5_allyouhadtodowasstay.txt'))]


'''
The next step prints the results to the terminal.
'''
print
print 'Word Length'
print [len(doc_text.words('1_welcometonewyork.txt'))] 
print [len(doc_text.words('2_blankspace.txt'))]
print [len(doc_text.words('3_style.txt'))]
print [len(doc_text.words('4_outofthewoods.txt'))]
print [len(doc_text.words('5_allyouhadtodowasstay.txt'))]


'''
The final step saves the results to a .csv
'''

out = csv.writer(open('TANDEM_output.csv','w'), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow('w')
out.writerow(data1)
out.writerow(data2)
out.writerow(data3)
out.writerow(data4)
out.writerow(data5)


print
print
print 'Your output is ready in TANDEM_output.csv'
