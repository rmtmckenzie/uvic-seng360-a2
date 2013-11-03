import re
import os
import sys
import glob
import libxml2

def to_xml(temp_dir,quiz_log):
	'''
	Purpose
		Return the path to a temp quiz log, an XML document created
		 by adding root element <rx> to quiz_log.
		The temp quiz log is stored under temp_dir.
	Precondition
		temp_dir is the path to a temp directory.
		quiz_log is the path to a quiz log.
	'''
	# read content of quiz log
	f = open(quiz_log,'r')
	content = f.read()
	f.close()

	# add to content the root element rx
	content = '<rx>\n' + content + '</rx>\n'

	# write content to temp quiz log
	temp_quiz_log = temp_dir + '/rx.xml'
	f = open(temp_quiz_log,'w')
	f.write(content)
	f.close()

	# return path to temp quiz log
	return temp_quiz_log

def get_name_login_dict(names_file):
	'''
	Purpose
		Return a dictonary where the keys are the student names and the
		 values are the logins.
	Precondition
		names_file is a path to the file that contains login and name
		 pairs.
		each login and name is appended with comma.
	'''
	# create logins dictionary
	logins = {}

	# populate logins dictionary with student names and logins from
	# names_file
	f = open(names_file,'r')
	for line in f:
		m = re.search('^([\w|\d]+),(\".+\")',line)
		if m:
			login = m.group(1)
			name = m.group(2)
			logins[name] = login
	f.close()

	# return logins dictionary
	return logins

def get_login_mark_dict(quiz_dir):
	'''
	Purpose
		Return a dictionary where the keys are the logins and the
		 values are total marks.
	Precondition
		quiz_dir is a path to the directory that contains quiz logs.
	'''
	# make temp_dir if not exists
	temp_dir = quiz_dir+'/temp'
	if not os.path.exists(temp_dir):
		os.mkdir(temp_dir)

	# create summary dictionary
	summary = {}

	# populate summary dictionary with student logins and total marks
	for quiz_log in glob.glob(quiz_dir+'/*.xml'):
		# extract login from path to quiz log
		login = quiz_log.split('/')[-1][:-4]

		# create marks dictionary
		marks = {}

		# convert quiz log to XML by adding root element rx and store
		# XML into temp quiz log
		temp_quiz_log = to_xml(temp_dir,quiz_log)

		# use libxml2 to parse log
		parse_tree = libxml2.parseFile(temp_quiz_log)

		# create a context for XPath query execution
		context = parse_tree.xpathNewContext()

		# populate marks dictionary with question ids and marks
		for question in context.xpathEval('/rx/question'):
			index = 0
			mark = 0
			for x in question.xpathEval('index/text()'):
				index = int( x.get_content() )
			for x in question.xpathEval('result/text()'):
				mark = int( x.get_content() )
			if index not in marks.keys():
				marks[index] = mark

		# free resources used by document
		context.xpathFreeContext()
		parse_tree.freeDoc()

		# remove temp quiz log
		os.remove(temp_quiz_log)

		# populate summary with student login and total mark
		summary[login] = sum(marks.values())

	# remove temp dir
	os.rmdir(temp_dir)

	# return summary dictionary
	return summary
