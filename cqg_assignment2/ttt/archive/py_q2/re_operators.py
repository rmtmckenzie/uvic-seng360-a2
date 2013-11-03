import question_template

question = question_template.Question_template()

question.game_type = 'input_output'

question.source_language = 'python'

question.parameter_list = [
        ['$pattern','string'],['$string','string'],['$y0','string']
]

question.tuple_list = [
	# concatenation
	['re_operators_concatenation_',
		['^0$','0',None],
		['^0$','a0',None],
		['^0$','0b',None],
		['^0$','a0b',None],
		['^01$','10',None],
		['^01$','01',None],
	],
	# alternation
	['re_operators_alternation_',
		['^0|1$','0',None],
		['^0|1$','1',None],
		['^0|1$','0b',None],
		['^0|1$','1b',None],
		['^0|1$','a0b',None],
		['^0|10|1$','01',None],
		['^0|10|1$','10',None],
	],
	# Kleene closure
	['re_operators_kleene_',
		['^0*$','',None],
		['^0*$','0',None],
		['^0*$','00',None],
		['^0*$','000',None],
		['^0*$','010',None],
	],
	# all together, with parens
	['re_operators_all_A_',
		['^(a|b|c)d*ef*$', 'ce',None],
		['^(a|b|c)d*ef*$', 'bbce',None],
		['^(12|23)*$', '12',None],
		['^(12|23)*$', '13',None],
		['^(12|23)*$', '123',None],
	],
	# substring matching
	['re_operators_substring_',
		['00*','0',None],
		['00*','00',None],
		['0*','a0b',None],
		['0*','ab',None],
		['0','a0b',None],
		['0','ab',None],
	],

	# closures
	['re_operators_closures_',
		['0+','0',None],
		['0+','a0',None],
		['0+','ab',None],
		['0?','0',None],
		['0?','a0',None],
		['0?','ab',None],
	],
	# list
	['re_operators_list_',
		['[01]+','10',None],
		['[01]+','01',None],
		['[01]+','x10',None],
		['[0-9]+','127',None],
		['[0-9]+','x127',None],
		['[0-9]+','x1y27',None],
	],
	# dot
	['re_operators_dot_',
		['a.z','az',None],
		['a.z','abz',None],
		['a.*z','abz',None],
		['a.*z','az',None],
		['a.*z','a012z',None],
	],
	# escapes
	['re_operators_escapes_',
		['a\db','a0b',None],
		['a\db','a5b',None],
		['a\db','a9b',None],
		['a\d*b','a0b',None],
		['a\s*b','ab',None],
		['a\s*b','a b',None],
		['a\s*b','a      b',None],
		['\w*','',None],
		['\w*','ab',None],
		['\w*','a0b',None],
		['\w*','^a0b$',None],
	],
	# all together, with parens
	['re_operators_all_B_',
		['(ab)*c+d?','c',None],
		['(ab)*c+d?','abcd',None],
		['(ab)*c+d?','bacd',None],
		['ab*c+d?','c',None],
		['ab*c+d?','ac',None],
		['ab*c+d?','abcd',None],
		['ab*c+d?','bacd',None],
	],
]

question.global_code_template = '''\
x	import sys
dx	import re
'''

question.main_code_template = '''\
dx	if re.search('$pattern','$string'):
dx		print 'match'
dx	else:
dx		print 'no match'
'''

question.argv_template = ''

question.stdin_template = ''

question.stdout_template = '''\
$y0
'''
