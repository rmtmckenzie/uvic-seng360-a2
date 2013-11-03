question_type = 'input_output'

source_language = 'python'

parameter_list = [
        ['$x0','string'],['$x1','string'],['$y0','string']
]

tuple_list = [
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

global_code_template = '''\
x	import sys
dx	import re
'''

main_code_template = '''\
dx
dx	m = re.search('$x0', '$x1')
dx
dx	for i in range(1,m.lastindex+1):
dx		print m.group(i),
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
