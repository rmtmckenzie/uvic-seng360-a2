#!/usr/bin/python

#A2 DONE

import os
import sys
import verify_util
import file_util

#list of verificationidentifier/condition pairs
condition_list = [
	#1
	['group_list_defined',
		"'group_list' is defined"],
	#2
	['group_list_type',
		"'group_list' is a list"],
	#3
	['group_format',
		"Each group is a list of length at least 2"],
	#4
	['group_unique',
		'group[0] is a unique string'],
	#5
	['question_format',
		'Each question is a list of length 3'],
	#6
	['plain_text',
		"question[0] or 'plaintext' is a string comprising of only characters"
		"in [A-Z]"],
	#7
	['key',
		"question[1] or 'key' is an integer in range [0-25]"],
	#8
	['hotspots',
		"hotspots is a list"],
	#9
	['hotspot_individual',
		"Each hotspot is an integer in range of the length of the plain_text"]

]

def verify_conditions(template,condition_list):
	conditions_dictionary = dict(conditions_list)
	#1
	if not ('group_list_defined' in dir(template)):
		return conditions_dictionary['question_groups_defined']
	#2
	if not (type(template.group_list) == list):
		return conditions_dictionary['question_groups_type']

	group_name_list = []
	for group in template.group_list:
		#3
		if not (type(group) == list and len(group >= 2)):
			return conditions_dictionary['group_format'] + \
				'\n\tgroup: ' + str(group)

		#4
		if not(type(group[0]) == str and group[0] not in group_name_list):
			return conditions_dictionary['group_unique'] + \
				'\n\tgroup: ' + str(group)
		else:
			group_name_list.append(group[0])

		for question in group[1:]:
			#5
			if not (type(question) == list and len(question) == 3):
				return \
					conditions_dictionary['question_format'] + \
					'\n\tquestion: ' + str(question)
			#6
			if not (type(question[0]) == str and \
					min(question[0]) >= 'A' and \
					max(question[0]) <= 'Z'):
				return conditions_dictionary['plain_text'] + \
					'\n\tquestion: ' + str(question)
			#7
			if not (type(question[1]) == int and \
					question[1] < 26 and \
					question[1] >= 0):
				return conditions_dictionary['key'] + \
					'\n\tquestion: ' + str(question)
			#8
			if not (type(question[2]) is list):
				return conditions_dictionary['hotspots'] + \
					'\n\tquestion: ' + str(question)

			for i in question[2]:
				#9
				if not (type(i) is int and \
						i < len(question[0]) and \
						i >= 0):
					return conditions_dictionary['hotspot_individual'] + \
						'\n\tquestion: ' + str(question)


# handle invocation from command line
if __name__ == '__main__':
	n = verify_util.template_verifier_main(
		sys.argv,
		"Question Type caesar: Template Verification Conditions",
		condition_list,
		verify_conditions)
	if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
		print 'Usage: caesar_template_verifier.py [template_file]'

	sys.exit(n)
