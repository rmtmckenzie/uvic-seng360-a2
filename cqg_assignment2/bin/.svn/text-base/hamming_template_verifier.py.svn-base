#!/usr/bin/python

import sys
import verify_util
import hamming_util
import file_util

# list of verification identifier/condition pairs
condition_list = [
	['tuples_defined',
		"'tuples' is defined"],
	['tuples_list',
		"'tuples' is a list"],
	['group_format',
		'Each group is a list of length at least 2'],
	['group_unique',
		'group[0] is a unique string'],
	['tuple_format',
		'Each tuple is a list of triples: [message, parity, indexes]'],
	['message',
		"'message' is a non-empty string of '0' and '1'"],
	['parity',
		"'parity' is 0 or 1"],
	["fill",
		"code_word_indexes; 'code_word_indexes' is a list of unique " +
		"indexes (1-relative) into the code word generated from " +
		"message"],
	["find_error",
		"code_word_indexes; 'code_word_indexes' is an index" +
		"(1-relative) into the code word generated from message"],
	['indexes',
		"'indexes' is either an int or a list of ints"],
]

def verify_conditions(template,condition_list):
	'''
	purpose
		verify each condition in condition_list
		on first failed condition, return error message
		otherwise, return None
	preconditions
		template was returned by file_util.dynamic_import()
		condition_list is a list where each element is a
		 list of two strings
	'''
	# convert conditions to dictionary
	conditions_dictionary = {}
	for condition in condition_list:
		conditions_dictionary[condition[0]] = condition[1]

	# test the conditions
	if not ('tuples' in dir(template)):
		return conditions_dictionary['tuples_defined']
	if not (type(template.tuples) == list):
		return conditions_dictionary['tuples_list']
	group_list = []
	for group in template.tuples:
		if not (type(group) == list and len(group) >= 2):
			return conditions_dictionary['group_format'] + \
			 '\n\tgroup: ' + str(group)
		if not (type(group[0]) == str and group[0] not in group_list):
			return conditions_dictionary['group_unique'] + \
			 '\n\tgroup: ' + str(group)
		else:
			group_list.append(group[0])
		for tuple in group[1:]:
			if not (type(tuple) == list and len(tuple) == 3):
				return conditions_dictionary['tuple_format'] + \
				 '\n\ttuple: ' + str(tuple)
			if not (type(tuple[0]) == str and len(tuple[0]) > 0):
				return conditions_dictionary['message'] + \
				 '\n\ttuple: ' + str(tuple)
			for character in tuple[0]:
				if not (character in ['0','1']):
					return conditions_dictionary[ \
					 'message'] + '\n\ttuple: ' + str(tuple)
			if not (tuple[1] in [0,1]):
				return conditions_dictionary['parity'] + \
				 '\n\ttuple: ' + str(tuple)
			code_word_length = hamming_util.get_code_word_length(
			 len(tuple[0]))
			if type(tuple[2]) == list:
				if not (len(tuple[2]) == len(set(tuple[2]))):
					return conditions_dictionary[ \
					 'fill'] + '\n\ttuple: ' + str(tuple)
				for i in tuple[2]:
					if not (
					 i in range(1,code_word_length+1)):
						return conditions_dictionary[ \
						 'fill'] + '\n\ttuple: ' + \
						 str(tuple)
			elif type(tuple[2]) == int:
				if not (
				 tuple[2] in range(1,code_word_length+1)):
					return conditions_dictionary[ \
					 'find_error'] + '\n\ttuple: ' + \
					 str(tuple)
			else:
				return conditions_dictionary['indexes'] + \
				 '\n\ttuple: ' + str(tuple)

	# all passed
	return None

# handle invocation from command line
if __name__ == '__main__':
	n = verify_util.template_verifier_main(sys.argv,
	 'Question Type hamming: Template Verification Conditions',
	 condition_list,verify_conditions)

	if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
		print 'Usage: hamming_template_verifier.py [template_file]'
	
	sys.exit(n)
