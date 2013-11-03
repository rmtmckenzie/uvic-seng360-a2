question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$pattern','ascii_string'],['$string','ascii_string'],['$y0','string']
]

group_list = [
	# concatenation
	['operators_concatenation_',
		['^(0)$','0',None],
		['^(0)$','a0',None],
		['^(0)$','0b',None],
		['^(0)$','a0b',None],
		['^(01)$','10',None],
		['^(01)$','01',None],
	],
	# alternation
	['operators_alternation_',
		['^(0|1)$','0',None],
		['^(0|1)$','1',None],
		['^(0|1)$','0b',None],
		['^(0|1)$','1b',None],
		['^(0|1)$','a0b',None],
		['^(0|10|1)$','01',None],
		['^(0|10|1)$','10',None],
	],
	# Kleene closure
	['operators_kleene_',
		['^(0*)$','',None],
		['^(0*)$','0',None],
		['^(0*)$','00',None],
		['^(0*)$','000',None],
		['^(0*)$','010',None],
	],
	# all together, with parens
	['operators_all_A_',
		['^((a|b|c)d*ef*)$', 'ce',None],
		['^((a|b|c)d*ef*)$', 'bbce',None],
		['^((12|23)*)$', '12',None],
		['^((12|23)*)$', '13',None],
		['^((12|23)*)$', '123',None],
	],
	# substring matching
	['operators_substring_',
		['00*','0',None],
		['00*','00',None],
		['0*','a0b',None],
		['0*','ab',None],
		['0','a0b',None],
		['0','ab',None],
	],

	# closures
	['operators_closures_',
		['0+','0',None],
		['0+','a0',None],
		['0+','ab',None],
		['0?','0',None],
		['0?','a0',None],
		['0?','ab',None],
	],
	# list
	['operators_list_',
		['[01]+','10',None],
		['[01]+','01',None],
		['[01]+','x10',None],
		['[0-9]+','127',None],
		['[0-9]+','x127',None],
		['[0-9]+','x1y27',None],
	],
	# dot
	['operators_dot_',
		['a.z','az',None],
		['a.z','abz',None],
		['a.*z','abz',None],
		['a.*z','az',None],
		['a.*z','a012z',None],
	],
	# escapes
	['operators_escapes_',
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
	['operators_all_B_',
		['(ab)*c+d?','c',None],
		['(ab)*c+d?','abcd',None],
		['(ab)*c+d?','bacd',None],
		['ab*c+d?','c',None],
		['ab*c+d?','ac',None],
		['ab*c+d?','abcd',None],
		['ab*c+d?','bacd',None],
	],
]

global_code_template = '''\
x	import sys
dx	import re
'''

main_code_template = '''\
dx	if re.search('$pattern','$string'):
dx		print 'match'
dx	else:
dx		print 'no match'
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
