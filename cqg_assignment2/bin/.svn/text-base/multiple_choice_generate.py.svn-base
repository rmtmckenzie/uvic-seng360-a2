#!/usr/bin/python

import sys
import os
import file_util

template_string = '''\
product_family = 'multiple_choice'
question_type = 'multiple_choice'

question_text = $q
answers = $a
correct_answer = $c
'''

if len(sys.argv) != 3:
	print 'Usage: multiple_choice_generate.py template question_directory'
	sys.exit(1)

try:
	template = file_util.dynamic_import(sys.argv[1])
except ImportError:
	print 'Failure while importing',sys.argv[1]
	sys.exit(2)

for group in template.question_groups:
	prefix = group[0]
	question_id = 0
	for (question_text,answers,correct_answer) in group[1:]:
		path = os.path.join(sys.argv[2],prefix+str(question_id))

		if not os.path.exists(path):
			os.mkdir(path)

		config_string = template_string
		config_string = config_string.replace('$q',
		 "r'''"+question_text+"'''")
		config_string = config_string.replace('$a',str(answers))
		config_string = config_string.replace('$c',str(correct_answer))

		file_util.write_string(
		 os.path.join(path,'cqg_config.py'), config_string)

		question_id += 1
