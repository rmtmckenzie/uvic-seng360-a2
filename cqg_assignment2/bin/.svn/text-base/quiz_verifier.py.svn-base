#!/usr/bin/python

import sys
import os
import re
import file_util
import verify_util
from quiz import get_question_dirs

# list of verification identifier/condition pairs
condition_list = [
        ['question_list_defined',
                "'question_list' is defined"],
        ['practice_mode_defined',
                "'practice_mode' is defined"],
        ['standalone_defined',
                "'standalone' is defined"],
        ['logged_defined',
                "'logged' is defined"],
        ['log_dir_defined',
                "'log_dir' is defined"],
        ['question_list_type',
                "'question_list' is non empty list of lists/tuples"],
        ['tuple_length',
                "each list/tuple in question_list is length 3"],
        ['mark_value',
                "mark is a non negative int"],
        ['count_value',
                "count is a non negative int"],
        ['practice_mode_type',
                "practice_mode is a bool"],
        ['standalone_type',
		"standalone is a bool"],
        ['only_one_question',
		"standalone quiz must contain only one question"],
        ['logged_type',
		"logged is a bool"],
        ['log_dir_type',
		"log_dir is a string"],
        ['log_dir_value',
		"log_dir is non empty in a logged quiz"],
        ['list_check',
		"every question in a list exists and is valid"],
        ['re_validate',
		"every re expression is valid and non empty"],
        ['re_check',
		"all questions specified by a re expression is valid"],
        ['one_or_more',
		"a quiz must contain at least 1 question"],
        ['not_enough_question',
		"Warning: count must be no larger than the size of the " + \
		"question pool"],
]

def check_question(q,library,t):
	'''
	purpose
		return None if q exist in library and q/cqg_config.py exists
		return error message otherwise
	precondition
		q is a string
		library is a path to quesiton library
		t is a two tuple
	'''
	d = os.path.join(library,q)
	if not os.path.isdir(d):
		return ' (' + d + ' in ' + str(t) + ' does not exist)'
	elif not os.path.isfile(os.path.join(d,'cqg_config.py')):
		return ' (' + d + ' in ' + str(t) + ' is not valid)'
	return None

def verify_conditions(quiz,condition_list):
	# convert conditions to dictionary
        conditions_dictionary = {}
        for condition in condition_list:
                conditions_dictionary[condition[0]] = condition[1]

	warning_message = ''

	# variable declaration check
	L = ['question_list','practice_mode','standalone','logged','log_dir']
	for v in L:
		if not v in dir(quiz):
			return conditions_dictionary[v + 'defined']

	# question_list type check
	if type(quiz.question_list) != list:
		return conditions_dictionary['question_list_type']
	if len(quiz.question_list) == 0:
		return conditions_dictionary['question_list_type']

	for t in quiz.question_list:
		if type(t) != tuple and type(t) != list:
			return conditions_dictionary['question_list_type'] + \
			 '\n\t' + str(t) + ' is not'

	# tuple length check
	for t in quiz.question_list:
		if len(t) != 3:
			return conditions_dictionary['tuple_length'] + \
			 '\n\t' + str(t) + ' is not'

	# mark value check
	for t in quiz.question_list:
		if type(t[0]) != int or (type(t[0] == int) and t[0] < 0):
			return conditions_dictionary['mark_value'] + \
			'\n\t' + str(t) + ': ' + str(t[0]) + ' is not'

	# count value check
	for t in quiz.question_list:
		if type(t[1]) != int or (type(t[1] == int) and t[1] < 0):
			return conditions_dictionary['mark_value'] + \
			'\n\t' + str(t) + ': ' + str(t[1]) + ' is not'
	 
	# practice_mode is a bool 
	if type(quiz.practice_mode) != bool:
		return conditions_dictionary['practice_mode_type']

	# quiz.standalone is a bool
	if type(quiz.standalone) != bool:
		return conditions_dictionary['standalone_type']

	# standalone quiz contain only one question
	if quiz.standalone:
		if len(quiz.question_list) > 1 or quiz.question_list[0][1] != 1:
			return conditions_dictionary['only_one_question']

	# logged is a bool
	if type(quiz.logged) != bool:
		return conditions_dictionary['logged_type']

	# log_dir is a string
	if type(quiz.log_dir) != str:
		return conditions_dictionary['log_dir_type']

	# log_dir non empty in logged quiz
	if quiz.logged and quiz.log_dir == '':
		return conditions_dictionary['log_dir_value']

	# count is no larger than the question pool size
	for t in quiz.question_list:
		if type(t[2]) == list:
			if t[1] > len(t[2]):
				warning_message += \
				 conditions_dictionary['not_enough_question']+\
				 '\n\t'+str(t)+'\n'
		elif type(t[2]) == str:
			sub_dir = os.path.split(t[2])[0]
			L = filter(lambda d: re.search(t[2],d) != None,
			 get_question_dirs(sub_dir,question_library))
			if t[1] > len(L):
				warning_message += \
				 conditions_dictionary['not_enough_question']+\
				 '\n\t'+str(t)+'\n'
				
	# question listed in a list is valid
	for t in quiz.question_list:
		if type(t[2]) == list:
			for d in t[2]:
				s = check_question(d,question_library,t)
				if s != None:
					return \
					 conditions_dictionary['list_check']

	# re exrepssion validation
	for t in quiz.question_list:
		if type(t[2]) == str: # pattern group:
			# empty re string check
			if t[2] == '':
				return conditions_dictionary['re_validate'] + \
				 '\n\t' + str(t) + ' has an empty re expression'
			# invalid re string check
			try:
				re.compile(t[2])
			except:
				return conditions_dictionary['re_validate'] + \
				 '\n\t' + str(t) + \
				 ' has an invalid re expression'

	# re expression question check
	for t in quiz.question_list:
		if type(t[2]) == str: # pattern group:
			sub_dir = os.path.split(t[2])[0]
			L = get_question_dirs(sub_dir,question_library)
			for d in L:
				if re.search(t[2],d) == None:
					continue
				s = check_question(d,question_library,t)
				if s != None:
					return \
					 conditions_dictionary['re_check'] + \
					 '\n\t' + str(d) + ' from '+str(t) + \
					 ' is invalid'

	# quiz contains at least one question
	no_question = True
	for t in quiz.question_list:
		if not no_question:
			break
		if type(t[2]) == list:
			# list of questions is verified
			no_question = False
			break
		if type(t[2]) == str:
			sub_dir = os.path.split(t[2])[0]
			L = get_question_dirs(sub_dir,question_library)
			for d in L:
				if re.search(t[2],d) != None:
					no_question = False
					break
	if no_question:
		return conditions_dictionary['one_or_more']
	
	# all condition passed
	if warning_message == '':
		return None
	else:
		return warning_message

# handle invocation from command line
if __name__ == '__main__':
	# print condition
	if len(sys.argv) == 1:
		verify_util.print_conditions('Quiz Verification Conditions',
		 condition_list)

	# check command line arguments
	if len(sys.argv) != 3:
		print 'Usage: quiz_verifier.py quiz_file question_library'
		sys.exit(-1)

	# load quiz file
	try:
		quiz = file_util.dynamic_import(sys.argv[1])
	except ImportError:
		print "quiz_file must be a Python file"
		sys.exit(-1) 

	# question library existance check
	question_library = os.path.abspath(sys.argv[2])
	if not os.path.isdir(question_library):
		print "question library directory must exist"
		sys.exit(-1) 

	print verify_conditions(quiz,condition_list)
