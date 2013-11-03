# multiple references the same list

game_type = 'input_output'

source_language = 'python'

parameter_list = [
        ['$y0','int'],['$y1','int'],['$y2','int'],
]

tuple_list = [
	['list_multi_to_one_reference_io_',
	[None,	1,	0],
	[0,     None,	0],
	[0,     1,	None],
	[None,	1,	None],
	[None,	None,	0],
	[0,	None,	None],
	[None,	None,	None],
	]
]

global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	Y = range(2)
dx	X = [2,Y,3]
dx	print X[1][0]
dx	print X[1][1]
dx	X[1] = 9
dx	print Y[0]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
