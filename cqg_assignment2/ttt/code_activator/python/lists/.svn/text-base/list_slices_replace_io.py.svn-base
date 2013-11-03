# replace a list slice with a new list

question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$x0','int'],['$x1','int'],['$x2','int'],['$y0','int']
]

group_list = [
	['list_slices_replace_io_forward_',
	[0,3,4,None],
	[0,3,3,None],
	[0,3,2,None],
	[1,3,5,None],
	[1,3,4,None],
	[1,3,3,None],
	[1,3,2,None],
	[0,1,4,None],
	[0,1,5,None],
	[0,1,6,None],
	],

	['list_slices_replace_io_mixed_backward_',
	[None,1,None,2],
	[None,1,None,4],
	[None,2,None,0],
	[None,3,None,0],
	[None,4,None,0],
	[1,None,None,0],
	[2,None,None,0],
	[3,None,None,0],
	],
]

global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	L = [2,4,6,8,0]
dx	L[$x0:$x1] = [2,4,6,8]
dx	print L[$x2]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
