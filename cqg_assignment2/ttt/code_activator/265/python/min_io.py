question_type = 'input_output'
source_language = 'python'

parameter_list = [
	['$i1','int'],['$i2','int'],['$y0','int']
]

tuple_list = [
	['py_min_io_forward_',	[1,2,None],	[4,9,None]],
	['py_min_io_backward_',	[None,None,2],	[None,None,6]],
	['py_min_io_mixed_',	[None,2,None],	[3,None,1]],
	['py_min_io_open_',	[None,None,None]],
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
