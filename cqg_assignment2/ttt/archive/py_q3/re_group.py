import question_template

question = question_template.Question_template()

question.game_type = 'input_output'

question.source_language = 'python'

question.parameter_list = [
        ['$x0','string'],['$x1','string'],['$y0','string']
]

question.tuple_list = [
	['re_group_',
		['(0*)', 'a00b', None ],
		['(0*)', '00b', None ],

		['(0+)', 'a00b', None ],
		['(0+)', '00b', None ],

		['(\d+)', 'a 123 b', None ],
		['(\d+)', 'a00b', None ],
		['(\d*)', 'a00b', None ],

		['([a-e]+)', ' abc 123 ', None ],
		['([a-e]*)', ' abc 123 ', None ],
		['([a-e]?)', ' abc 123 ', None ],

		['([0-9]+\.[0-9]+)', '123.45', None ],
		['([0-9]+)\.([0-9]+)', '123.45', None ],
		['([0-9]*)\.([0-9]*)', '123.45', None ],
		['([0-9]*).([0-9]*)', '123x45', None ],
		['([0-9]*).([0-9]*)', '123.45', None ],
	]
]

question.global_code_template = '''\
x	import sys
dx	import re
'''

question.main_code_template = '''\
dx
dx	m = re.search('$x0', '$x1')
dx
dx	for i in range(1,m.lastindex+1):
dx		print m.group(i),
'''

question.argv_template = ''

question.stdin_template = ''

question.stdout_template = '''\
$y0
'''
