#!/usr/bin/python

import sys
import subprocess

if len(sys.argv) < 4:
	print 'Usage: batch_quiz_log_to_html.py question_library output_directory log_file1.xml log_file2.xml ...'
	sys.exit()

question_library = sys.argv[1]
output_directory = sys.argv[2]

for filename in sys.argv[3:]:
	result = subprocess.call(['quiz_log_to_html.py',
	 filename,question_library,output_directory])
	if result:
		print "aborted while processing "+filename
		sys.exit()
