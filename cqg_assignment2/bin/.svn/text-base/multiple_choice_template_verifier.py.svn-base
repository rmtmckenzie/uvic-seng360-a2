#!/usr/bin/python

import os
import sys
import verify_util
import file_util

# list of verification identifier/condition pairs
condition_list = [
	['question_groups_defined',
		"'question_groups' is defined"],
	['question_groups_list',
		"'question_groups' is a list"],
	['group_format',
		'Each group is a list of length at least 2'],
	['group_unique',
		'group[0] is a unique string'],
	['question_format',
		'Each question is a list of length 3'],
	['question_text',
		"'question_text' is a string"],
	['answers',
		"'answers' is a list of strings"],
	['correct_answer',
		"'correct_answer' is an index into answers or a list of "
		"indeces into answers"],
]
 
def verify_conditions(template,condition_list):
	conditions_dictionary = dict(condition_list)

	if not ('question_groups' in dir(template)):
		return conditions_dictionary['question_groups_defined']
	if not (type(template.question_groups) == list):
		return conditions_dictionary['question_groups_type']

	prefix_list = []
	for group in template.question_groups:
		if not (type(group) == list and len(group) >= 2):
			return conditions_dictionary['group_format'] + \
			 '\n\tgroup: ' + str(group)

		if not (type(group[0]) == str and group[0] not in prefix_list):
			return conditions_dictionary['group_unique'] + \
			 '\n\tgroup: ' + str(group)
		else:
			prefix_list.append(group[0])

		for question in group[1:]:
			if not (type(question) == list and len(question) == 3):
				return \
				 conditions_dictionary['question_format'] + \
				 '\n\tquestion: ' + str(question)

			if not (type(question[0]) == str):
				return conditions_dictionary['question_text']+\
				 '\n\tquestion: ' + str(question)

			if not (type(question[1]) is list):
				return conditions_dictionary['answers'] + \
				 '\n\tquestion: ' + str(question)
			for i in question[1]:
				if not (type(i) is str):
					return \
					 conditions_dictionary['answers'] + \
					 '\n\tquestion: ' + str(question)

			if type(question[2]) is int:
				if question[2] not in range(len(question[1])):
					return \
					 conditions_dictionary[
					 'correct_answer'] + \
					 '\n\tquestion: ' + str(question)

			elif type(question[2]) is list:
				for i in question[2]:
					if i not in range(len(question[1])):
						return \
						 conditions_dictionary[ 
						 'correct_answer'] + \
						 '\n\tquestion: '+str(question)
			else:
				return \
				 conditions_dictionary['correct_answer'] + \
				 '\n\tquestion: ' + str(question)

# handle invocation from command line
if __name__ == '__main__':
	n = verify_util.template_verifier_main(sys.argv,
	 'Question Type multiple_choice: Template Verification Conditions',
	 condition_list,verify_conditions)

	if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
		print 'Usage: multiple_choice_template_verifier.py [template_file]'

	sys.exit(n)
