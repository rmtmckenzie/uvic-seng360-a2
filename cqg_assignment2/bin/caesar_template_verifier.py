#!/usr/bin/python

#A2 TODO

import os
import sys
import verify_util
import file_util

#list of verificationidentifier/condition pairs
condition_list = [


]

def verify_conditions(template,condition_list):
	conditions_dictionary = dict(conditions_list)



	# handle invocation from command line
	if __name__ == '__main__':
		n = verify_util.template_verifier_main(
			sys.argv,
			condition_list,
			verifify_conditions)
		if n == verify_util.COMMAND_LINE_SYNTAX_FAILURE:
			print 'Usage: caesar_template_verifier.py [template_file]'

		sys.exit(n)
