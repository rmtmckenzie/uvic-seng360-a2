#!/usr/bin/python

import sys
import os

def verify_all(path):
	L = os.listdir(path)
	for d in L:
		q_dir = os.path.join(path,d)
		if not os.path.isdir(q_dir):
			continue
		if os.path.isfile(os.path.join(q_dir,'types.py')):
			# check question type
			exec(open(os.path.join(q_dir,'types.py'),'r').read())
			if product_family == 'codeact':
				cmd = 'python question_verifier.py '+q_dir
				os.system(cmd)
			elif product_family == 'crc':
				print 'question verifier not available'
			elif product_family == 'hamming':
				print 'question verifier not available'
			else:
				print 'unknown question type'
		else:
			verify_all(q_dir)

# check command line arguments
if len(sys.argv) != 2:
	print 'Usage: '+sys.argv[0]+' question_library_path'
	sys.exit(-1)

# chech if question library exists
q_lib_path = sys.argv[1]
if not os.path.isdir(q_lib_path):
	print q_lib_path+' does not exist'
	sys.exit(-2)

# verify all questions in q_lib_path
verify_all(q_lib_path)
