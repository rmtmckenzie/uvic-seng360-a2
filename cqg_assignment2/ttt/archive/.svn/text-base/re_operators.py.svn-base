import question_template

question = question_template.Question_template()

question.game_type = 'input_output'

question.source_language = 'python'

question.parameter_list = [
        ['$pattern','string'],['$string','string'],['$y0','string']
]

question.tuple_list = [
	['re_operators_A_',
		['^0$','0',None],
		['^0$','a0',None],
		['^0$','0b',None],
		['^0$','a0b',None],
	],
	['re_operators_B_',
		['^0|1$','0',None],
		['^0|1$','1',None],
		['^0|1$','0b',None],
		['^0|1$','1b',None],
		['^0|1$','a0b',None],
		['^0|1$','a1b',None],
	],
]

question.global_code_template = '''\
x	import sys
dx	import re
'''

question.main_code_template = '''\
dx	if re.search($pattern,$string):
dx		print 'match'
dx	else:
dx		print 'no match'
'''

question.argv_template = ''

question.stdin_template = ''

question.stdout_template = '''\
$y0
'''
