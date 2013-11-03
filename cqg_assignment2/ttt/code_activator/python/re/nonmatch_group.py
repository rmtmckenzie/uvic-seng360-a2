question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$x0','ascii_string'],['$x1','ascii_string'],['$y0','string']
]

group_list = [
	['nonmatch_group_',
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

global_code_template = '''\
x	import sys
dx	import re
'''

main_code_template = '''\
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

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
