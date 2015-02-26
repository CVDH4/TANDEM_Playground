#
# TANDEM 0.05 
# Playing Around with NLTK
# Follow CVDH4 and SBReal
#

__author__ = 'sbr'

import csv

print
print "Welcome to TANDEM 0.05 - Playing with NLTK"
print

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'tessyout'
doc_text = PlaintextCorpusReader(corpus_root, '.*')



print doc_text.fileids()
print

#
# Let's write a loop to go through and print these instead.
#


print doc_text.words('1_welcometonewyork.txt')
print doc_text.words('2_blankspace.txt')
print doc_text.words('3_style.txt')
print doc_text.words('4_outofthewoods.txt')
print doc_text.words('5_allyouhadtodowasstay.txt')
print
print "Your output is ready in TANDEM_output.csv"

#
# Let's write a loop to go through and generate these instead.
#

data1 = [len(doc_text.words('1_welcometonewyork.txt'))]
data2 = [len(doc_text.words('2_blankspace.txt'))]
data3 = [len(doc_text.words('3_style.txt'))]
data4 = [len(doc_text.words('4_outofthewoods.txt'))]
data5 = [len(doc_text.words('5_allyouhadtodowasstay.txt'))]


#
# Let's write a loop to go through and generate these instead.
#

out = csv.writer(open("TANDEM_output.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow("w")
out.writerow(data1)
out.writerow(data2)
out.writerow(data3)
out.writerow(data4)
out.writerow(data5)