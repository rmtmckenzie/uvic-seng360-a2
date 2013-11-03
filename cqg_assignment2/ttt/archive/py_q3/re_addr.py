import question_template

question = question_template.Question_template()

question.game_type = 'input_output'

question.source_language = 'python'

question.parameter_list = [
        ['$x0','string'],['$y0','string']
]

question.tuple_list = [
	['re_addr_',
		['100 Main Street',None],
		['100 Main St.',None],
		['100 Main St',None],
		['First Street',None],
		['100 First Street',None],
		['10 Island View Road',None],
		['10B Island View Road',None]
	]
]

question.global_code_template = '''\
x	import sys
dx	import re
'''

question.main_code_template = '''\
dx	number = '[0-9]+[A-Z]? '
dx	name = '[A-Z][a-z]*( [A-Z][a-z]*)* '
dx	suffix = '(Street|St\.|Avenue|Ave\.|Road|Rd\.)'
dx
dx	R = '^' + number + name + suffix + '$'
dx
dx	if re.search(R, '$x0'):
dx		print 'match'
dx	else:
dx		print 'no match'
'''

question.argv_template = ''

question.stdin_template = ''

question.stdout_template = '''\
$y0
'''
