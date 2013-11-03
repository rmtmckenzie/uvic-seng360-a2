#!/usr/bin/python

import sys
import os
import hamming_util
import verify_util
import file_util

# list of verification identifier/condition pairs
condition_list = [
	['variables_defined',
		"'product_family', 'question_type', 'message', 'parity', " +
		"'code_word_indexes' are defined"],
	['product_family',
		"'product_family' is 'hamming'"],
	['question_type',
		"'question_type' is 'fill' or 'find_error'"],
	['parity',
		"'parity' is 0 or 1"],
	['message',
		"'message' is a non-empty string of '0' and '1'"],
	["fill",
		"'code_word_indexes' is a list of unique indexes " +
		"(1-relative) into the code word generated from message"],
	["find_error",
		"'code_word_indexes' is an index " +
		"(1-relative) into the code word generated from message"],
]

def verify_conditions(question_directory,config,condition_list):
	'''
	purpose
		verify each condition in condition_list
		on first failed condition, return error message
		otherwise, return None
	preconditions
		question_directory is a directory containing a config file
		config is a Python module reference
		condition_list is a list where each element is a
		 list of two strings
	'''
	conditions_dictionary = {}
	for condition in condition_list:
		conditions_dictionary[condition[0]] = condition[1]

	for v in ['product_family','question_type','message','parity',
	 'code_word_indexes']:
		if not (v in dir(config)):
			return(conditions_dictionary['variables_defined'])

	if not (config.product_family == 'hamming'):
		return(conditions_dictionary['product_family'])

	if not (config.question_type in ['fill','find_error']):
		return(conditions_dictionary['question_type'])

	if not (type(config.parity) is int and config.parity in [0,1]):
		return(conditions_dictionary['parity'])

	if not (type(config.message) == str and len(config.message) > 0):
		return conditions_dictionary['message']
	for character in config.message:
		if not (character in ['0','1']):
			return conditions_dictionary['message']

	code_word_length = hamming_util.get_code_word_length(
	 len(config.message))
	if config.question_type == 'fill':
		if not (type(config.code_word_indexes) is list and
		 len(config.code_word_indexes) ==
		 len(set(config.code_word_indexes))):
			return conditions_dictionary['fill']
		for i in config.code_word_indexes:
			if not (i in range(1,code_word_length+1)):
				return conditions_dictionary['fill']
	if config.question_type == 'find_error':
		if not (type(config.code_word_indexes) is int):
			return conditions_dictionary['find_error']
		if not (config.code_word_indexes in
		 range(1,code_word_length+1)):
			return conditions_dictionary['find_error']

	return None # no errors found

# handle invocation from command line
if __name__ == '__main__':
	n = verify_util.question_verifier_main(sys.argv,
	 'Question Type hamming: Question Verification Conditions',
	 condition_list,verify_conditions)

	if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
		print 'Usage: hamming_question_verifier.py [question_directory]'

	sys.exit(n)
