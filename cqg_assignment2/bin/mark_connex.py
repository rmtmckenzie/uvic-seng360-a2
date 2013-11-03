#!/usr/bin/python

import os
import sys
sys.path.append('./codeAct')
import log_analysis

if __name__ == '__main__':
	# check number of command arguments
	if len(sys.argv) != 3:
		print 'Usage: ./mark_connex.py <names_file> <quiz_dir>'
		sys.exit(-1)

	# create path to names file
	names_file = sys.argv[1]

	# exit if names file doesn't exist
	if not os.path.isfile(names_file):
		print "Names file '" + names_file + "' not exist"
		sys.exit(-1)

	# create path to quiz dir
	quiz_dir = sys.argv[2]

	# exit if quiz dir doesn't exist
	if not os.path.exists(quiz_dir):
		print "Quiz dir '" + quiz_dir + "' not exist"
		sys.exit(-1)

	# get name to login dictionary
	name_login_dict = log_analysis.get_name_login_dict(names_file)

	# get login to total mark dictionary
	login_mark_dict = log_analysis.get_login_mark_dict(quiz_dir)

	# for each student, print to stdout login, name, and total mark
	for name in sorted(name_login_dict.keys()):
		# find login corresponding to name
		login = name_login_dict[name]

		# find total mark corresponding to login
		if login_mark_dict.has_key(login):
			mark = login_mark_dict[login]
		else:
			mark = 0

		# print to stdout login, name, and total mark
		print login + ',' + name + ',' + str(mark)
