import sys
import os
import file_util

# return values for main functions
SUCCESS = 0
IMPORT_FAILURE = 1
DIRECTORY_FAILURE = 2
CONDITION_FAILURE = 3
COMMAND_LINE_SYNTAX_FAILURE = 4

def print_conditions(title,condition_list):
	'''
	purpose
		write HTML version of condition_list to stdout
		using title in <title> and <h2>
	preconditions
		title is a string
		condition_list is a list
			each element of condition_list is a list of 2 strings
	'''
	print '<html><head>'
	print '<title>' + title + '</title>'
	print '</head>'
	print '<body>'
	print '<h2>' + title + '</h2>'
	print '<dl>'
	for condition in condition_list:
		print '<dt><b>' + condition[0] + '</b><dd>\n' + condition[1]
	print '</dl>'
	print '</body></html>'

def template_verifier_main(argv,title,condition_list,verify_conditions):
	'''
	CONSIDER: is this documentation worth maintaining?
		it is longer than the code! is it easier to read?
	Purpose
		if len(argv) == 1:
			invoke print_conditions(title,condition_list)
			return SUCCESS
		elif len(argv) == 2:
			invoke verify_conditions(argv[2],condition_list)
			if argv is not a readable file containing valid Python
				return IMPORT_FAILURE
			else if return value is a string
				write the string to stdout
				return CONDITION_FAILURE
			else
				return SUCCESS
		else:
			return COMMAND_LINE_SYNTAX_FAILURE
	Precondition
		argv is a list of strings
		title is a string
		condition_list is a list where each element is a
		 list of two strings
		verify_conditions is a function accepting a string
		 and a condition list
	'''
	if len(argv) == 1: # print conditions
		print_conditions(title,condition_list)
		return SUCCESS
	elif len(sys.argv) == 2: # verify conditions
		try:
			template = file_util.dynamic_import(argv[1])
		except:
			print 'Failure while importing',argv[1]
			return IMPORT_FAILURE
		# check conditions
		error_message = verify_conditions(template,condition_list)
		if error_message == None:
			return SUCCESS
		else:
			print 'Condition failed:\n\t',error_message
			return CONDITION_FAILURE
	else: # argv syntax error
		return COMMAND_LINE_SYNTAX_FAILURE

def question_verifier_main(argv,title,condition_list,verify_conditions):
	'''
	Purpose
		if len(argv) == 1:
			print condition_list formatted in HTML
		elif len(argv) == 2:
			verify condition_list by using verify_conditions
		else:
			print usage of argv[0]
	Precondition
		argv is a list of strings
		title is a string
		condition_list is a list of 2-string lists
		verify_conditions(Q,C,L) is a function where
		 Q is a directory containing a config file,
		 C is a reference to the cqg_config module in Q and
		 L is a list where each element is a list of 2 strings
	'''
	# process command line arguments
	if len(argv) == 1: # print conditions
		print_conditions(title,condition_list)
		return SUCCESS

	elif len(argv) == 2: # verify conditions
		if not file_util.check_directory(argv[1],True):
			print 'Not a readable directory: ' + argv[1]
			return DIRECTORY_FAILURE

		config_file = os.path.join(argv[1],'cqg_config.py')
		try:
			config = file_util.dynamic_import(config_file)
		except:
			print 'Failure while importing',config_file
			return IMPORT_FAILURE

		# check conditions
		error_message = verify_conditions(argv[1],config,condition_list)
		if error_message == None:
			return SUCCESS
		else:
			print 'Condition failed:\n\t',error_message
			return CONDITION_FAILURE
	else: # argv syntax error
		print 'Usage: echo_question_verifier.py [question_directory]'
		return COMMAND_LINE_SYNTAX_FAILURE

#-----------------------------------------------------------------

def generate_main(argv,create_cqg_config):
	'''
	Purpose
		if len(argv) == 3:
			create a cqg_config.py for each template tuple by using
			 create_cqg_config
		else:
			print usage of argv[0]
	Precondition
		argv is a list of strings
		create_cqg_config is a function that takes a template tuple as
		 input parameter
	'''
	pass
