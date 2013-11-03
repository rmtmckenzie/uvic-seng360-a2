# what sublist is extracted by default lower/upper indexes?

question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$x0','int'],['$x1','int'],['$x2','int'],['$x3','int'],['$x4','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],
]

group_list = [
	['list_slices_defaultUL_io_forward_',
	[0,1,3,1,4,None,None,None],
	[1,1,4,1,0,None,None,None],
	[2,1,2,1,2,None,None,None],
	[0,2,3,1,1,None,None,None],
	[1,0,3,1,3,None,None,None],
	[2,0,2,0,2,None,None,None],
	[3,0,2,1,1,None,None,None],
	],

	['list_slices_defaultUL_io_mixed_',
	[None,None,2,1,None,2,None,8],
	[None,None,2,0,None,4,None,6],
	[None,None,3,2,None,6,None,2],
	[None,None,4,3,None,0,None,4],
	[None,None,4,0,None,0,None,4],
	],

	['list_slices_defaultUL_io_backward_',
	[None,None,None,None,None,0,2,4],
	[None,None,None,None,None,2,4,6],
	[None,None,None,None,None,8,8,8],
	[None,None,None,None,None,8,0,2],
	[None,None,None,None,None,4,2,0],
	[None,None,None,None,None,6,8,2],
	[None,None,None,None,None,8,2,4],
	],
]

global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	L = [2,4,6,8,0]
dx	print L[$x0:][$x1]
dx	print L[:$x2][$x3]
dx	print L[:][$x4]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
