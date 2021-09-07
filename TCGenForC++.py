'''
		Aashutosh Rathi
https://github.com/aashutoshrathi/
Testcase Generator for HackerRank

'''


import os
import random
import sys
import zipfile
import math
import time
import shutil

try:
	os.mkdir('input')
	os.mkdir('output')
except OSError:
	pass

pwr = math.pow
rint = random.randint

tf = 10 # number of test files, change it according to you.


for i in range(0, tf + 1):
	print ('Generating:', i, file=sys.stderr)
	sys.stdout = open('input/input%02d.txt' % i, 'w')
	
	'''
	Input area will start here,
	everything that you print out here will be taken as input in your logic file.
	You can set difficulty of test cases all by you.
	'''

	### Input File Printing Start
	x = rint(1, 10) # number of test cases in (1,100)
	print(x) # Prints x into input file
	l = ""
	for i in range(0, x):
		l += str(rint(-100, 100)) + " "
	print(l) # Prints x into input file
	sys.stdout.close()
	### Input File Printing Ends


with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
	for i in range(0, tf + 1):
		print('Zipping:', i, file=sys.stderr)
		start = time.time()
		os.system('g++ -o logic logic.cpp')
		os.system('logic < input/input%02d.txt > output/output%02d.txt' % (i, i))
		end = time.time()
		print('Time taken to execute this TC %02f' %(end - start), file=sys.stderr)
		zf.write('input/input%02d.txt' % i)
		zf.write('output/output%02d.txt'% i)

shutil.rmtree('input')
shutil.rmtree('output')
