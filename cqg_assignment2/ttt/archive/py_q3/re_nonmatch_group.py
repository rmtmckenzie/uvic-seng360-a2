import question_template

question = question_template.Question_template()

question.game_type = 'input_output'

question.source_language = 'python'

question.parameter_list = [
        ['$x0','string'],['$x1','string'],['$y0','string']
]

question.tuple_list = [
	['re_nonmatch_group_',
		['(0*)', '00b', None ],
		['(?:0*)', '00b', None ],

		['(0+)', '00b', None ],
		['(?:0+)', '00b', None ],

		['(\d*)', 'a00b', None ],
		['(?:\d*)', 'a00b', None ],

		['([a-e])\s*(\d+)', ' abc 123 ', None ],
		['(?:[a-e])\s*(\d+)', ' abc 123 ', None ],

		['((?:a|b)\d+)', 'a01', None ],
		['((?:a|b)\d+)', 'b01', None ],
		['((?:a|b)\d+)', 'c01', None ],
		['((?:a|b)\d+)', 'b 01', None ],
	]
]

question.global_code_template = '''\
x	import sys
dx	import re
'''

question.main_code_template = '''\
dx
dx	m = re.search('$x0','$x1')
dx
dx	if m:
dx		if m.lastindex:
dx			for i in range(1,m.lastindex+1):
dx				print m.group(i),
dx		else:
dx			print 'no match'
dx	else:
dx		print 'no match'
'''

question.argv_template = ''

question.stdin_template = ''

question.stdout_template = '''\
$y0
'''
