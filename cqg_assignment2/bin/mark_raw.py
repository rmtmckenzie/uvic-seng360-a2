#!/usr/bin/python

import os
import sys
sys.path.append('./codeAct')
import log_analysis
import glob

def create_raw(quiz_dir,quiz_name):
	'''
	Purpose
		Create the following file by using quiz_dir:
			quiz_name_raw.txt:	contains student marks for each
						 question
	Precondition:
		quiz_dir is a valid path.
		quiz_name is a string.
	'''
	# create a dictionary of dictionaries where the first level keys are
	# question indexes, the second level keys are student logins, and the
	# values are question marks
	D = {}
	L = []
	for quiz_log in glob.glob(quiz_dir+'/*.xml'):
		# extract student login from index to quiz log
		login = quiz_log.split('/')[-1][:-4]

		# append student login to L
		L.append(login)

		# extract question marks for one student
		marks_dict = log_analysis.extract_one_log(quiz_log)

		# append question marks to D
		for index in marks_dict.keys():
			if not D.has_key(index):
				D[index] = {}
			D[index][login] = marks_dict[index][1]

	# open raw file for writing
	file_handle = open(quiz_name+'_raw.txt','w')

	# write column headers
	file_handle.write('Student')
	for index in sorted( D.keys() ):
		file_handle.write('\tQ'+str(index))
	file_handle.write('\n')

	# write question marks for each student
	for login in sorted(L):
		file_handle.write(login)
		for index in sorted( D.keys() ):
			file_handle.write('\t')
			if D[index].has_key(login):
				file_handle.write( str(D[index][login]) )
		file_handle.write('\n')

	# close raw file
	file_handle.close()

if __name__ == '__main__':
	# check number of command arguments
	if len(sys.argv) != 2:
		print 'Usage: ./mark_raw.py <quiz_dir>'
		sys.exit(-1)

	# create path to quiz dir
	quiz_dir = sys.argv[1]

	# exit if quiz dir doesn't exist
	if not os.path.exists(quiz_dir):
		print "Quiz dir '" + quiz_dir + "' not exist"
		sys.exit(-1)

	# extract quiz name from quiz dir
	dirs = quiz_dir.split('/')
	dirs.reverse()
	for dir in dirs:
		if dir != '':
			quiz_name = dir
			break

	# write question marks for each student to file
	create_raw(quiz_dir,quiz_name)
