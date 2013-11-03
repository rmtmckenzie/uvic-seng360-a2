question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
	['$i1','int'],['$i2','int'],['$y0','int']
]

group_list = [
	['min_io_forward_', [1,2,None], [4,9,None]],
	['min_io_backward_', [None,None,2], [None,None,6], [None,None,None]],
]

global_code_template = '''\
x	import sys
dx
'''

main_code_template = '''\
dx	a = $i1
dx	b = $i2
dx	if a < b:
dx		print a
dx	else:
dx		print b
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
