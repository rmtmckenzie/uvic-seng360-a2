#!/usr/bin/python

import sys
import os
import file_util

template_string = '''\
product_family = 'hamming'
question_type = $q

message = $m
parity = $p
code_word_indexes = $c
'''

if len(sys.argv) != 3:
	print 'Usage: hamming_generate.py template question_directory'
	sys.exit(1)

try:
	template = file_util.dynamic_import(sys.argv[1])
except ImportError:
	print 'Failure while importing',sys.argv[1]
	sys.exit(2)

for group in template.tuples:
	prefix = group[0]
	question_id = 0
	for message,parity,code_word_indexes in group[1:]:
		path = os.path.join(sys.argv[2],prefix+str(question_id))

		# create the question directory if necessary
		if not os.path.exists(path):
			try:
				os.mkdir(path)
			except:
				print 'Failure creating directory:', path
				sys.exit(3)

		if type(code_word_indexes) == list:
			question_type = 'fill'
		elif type(code_word_indexes) == int:
			question_type = 'find_error'

		# write the next config
		config = os.path.join(path,'cqg_config.py')
		try:
			f = open(config,"w")
			config_string = template_string
			config_string = config_string.replace('$q',
			 "'"+question_type+"'")
			config_string = config_string.replace('$m',
			 "'"+message+"'")
			config_string = config_string.replace('$p',str(parity))
			config_string = config_string.replace('$c',
			 str(code_word_indexes))
			f.write(config_string)
			f.close()
		except:
			print 'Failure creating file:', path
			sys.exit(4)

		question_id += 1
