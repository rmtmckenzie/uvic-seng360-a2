# what sublist is exracted with out of range indexes?

game_type = 'input_output'

source_language = 'python'

parameter_list = [
	['$x0','int'],['$x1','int'],['$x2','int'],['$x3','int'],['$x4','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],
]

tuple_list = [
	['list_slices_outOfRange0_io_',
	# forward
	[3,1,0,1,4,None,None,None],
	[4,1,1,1,0,None,None,None],
	[2,1,2,1,2,None,None,None],
	[3,1,0,2,1,None,None,None],
	[3,1,1,0,3,None,None,None],
	[2,0,2,0,2,None,None,None],
	[2,1,3,0,1,None,None,None],

	# mixed/backwrad
	[2,1,None,None,None,4,None,8],
	[2,0,None,None,None,2,None,6],
	[3,2,None,None,None,6,None,2],
	[4,3,None,None,None,8,None,4],
	[4,0,None,None,None,2,None,4],
	[None,None,None,None,None,0,2,4],
        [None,None,None,None,None,2,4,6],
        [None,None,None,None,None,8,8,8],
        [None,None,None,None,None,8,0,2],
	]
]

global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	L = [2,4,6,8,0]
dx	print L[-10:$x0][$x1]
dx	print L[$x2:10][$x3]
dx	print L[-10:10][$x4]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
