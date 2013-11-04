#!/usr/bin/python

#A2 DONE : maybe?

import sys
import os
import file_util

template_string = '''\
product_family = 'caesar'
question_type = 'caesar'

plaintext = {plaintext}
key = {key}
hotspots = {hotspots}
'''

if len(sys.argv) != 3:
	print 'Usage: caesar_generate.py template question_directory'
	sys.exit(1)

try:
	template = file_util.dynamic_import(sys.argv[1])
except ImportError:
	print 'Failure while importing',sys.argv[1]
	sys.exit(2)

for group in template.group_list:
	prefix = group[0]
	for question_id,(plaintext, key, hotspots) in enumerate(group[1:]):
		path = os.path.join(sys.argv[2], prefix + str(question_id))

		if not os.path.exists(path):
			os.mkdir(path)

		config_string = template_string.format(**locals())

		file_util.write_string(
			os.path.join(path, 'cqg_config.py'), config_string)

