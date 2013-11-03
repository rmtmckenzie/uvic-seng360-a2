question_type = 'bullseye'

source_language = 'python'

hotspot_declarations = [
	['$t0','target'],['$t1','target'],['$x1','int'],['$x2','int']
]

group_list = [
	['min_be_',
                [True,False,1,None],
                [True,False,None,None],
                [False,True,None,7]
        ]
]

global_code_template = '''\
x	import sys
dx
'''

main_code_template = '''\
dx	a = $x1
dx	b = $x2
dx	if a < b:
dx		$t0
dx		print a
dx	else:
dx		$t1
dx		print b
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
