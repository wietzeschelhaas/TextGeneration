# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:09:53 2020

@author: wietz
"""

import regex as re    
def save_doc(filename,data):
	file = open(filename, 'w')
	file.write(data)
	file.close()

def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r', encoding='utf8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

in_filename = 'qoutes.txt'
doc = load_doc(in_filename)
print(doc[:200])

test = re.sub("[^\P{P}]", "", doc)
test = test.lower()
save_doc("quotesClean.txt",test)

s = 0
k = doc.split("\n")
m = 0
for x in doc.split("\n"):
    if len(x.split()) > m:
        m = len(x.split())
    s += len(x.split())




in_filename = 'smaller.txt'
doc = load_doc(in_filename)

counter = 0
for x in sequences:
    if len(x) != 27:
        print(x)
        print(counter)
        break
    counter = counter +1