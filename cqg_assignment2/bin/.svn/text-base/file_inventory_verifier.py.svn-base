#!/usr/bin/python

import sys
import os

SUCCESS = 0
MISSING_FILES = 1
COMMAND_LINE_SYNTAX_FAILURE = 2

# file name with a trailing slash will match only a directory
filelist = [
	"bin/QUESTION_TYPE_template_verifier.py",
	"bin/QUESTION_TYPE_generate.py",

	"web2py/applications/cqg/question/QUESTION_TYPE.py",
	"web2py/applications/cqg/question/QUESTION_TYPE_util.py",

	"documents/QUESTION_TYPE/template_format.html",
	"documents/QUESTION_TYPE/question_rules.html",

	"testing_review/QUESTION_TYPE/question_template_verification_plan.html",

	"testing_review/QUESTION_TYPE/function_tests.py",

	"testing_review/QUESTION_TYPE/templates/",
	"testing_review/QUESTION_TYPE/question_library/",
	"testing_review/QUESTION_TYPE/quizzes/",
	"testing_review/QUESTION_TYPE/install_tests.py",
	"testing_review/QUESTION_TYPE/uninstall_tests.py",

	"testing_review/QUESTION_TYPE/manual_gui_test_plan.txt",
	"testing_review/QUESTION_TYPE/selenium_test_cases/",
	"testing_review/QUESTION_TYPE/selenium_test_suite.html",

	"testing_review/QUESTION_TYPE/log/",
]

if len(sys.argv) not in [2,3]:
	print "Usage: file_inventory_verifier.py question_type [cqg_directory]"
	sys.exit(COMMAND_LINE_SYNTAX_FAILURE)

if len(sys.argv) == 2: # print file list
	print "\n".join(filelist).replace("QUESTION_TYPE",sys.argv[1])
	sys.exit(SUCCESS)

if len(sys.argv) == 3: # verify files present
	status = SUCCESS
	for f in filelist:
		f = f.replace("QUESTION_TYPE",sys.argv[1])
		if not os.path.exists(os.path.join(sys.argv[2],f)):
			status = MISSING_FILES
			print "missing: "+f
	sys.exit(status)

