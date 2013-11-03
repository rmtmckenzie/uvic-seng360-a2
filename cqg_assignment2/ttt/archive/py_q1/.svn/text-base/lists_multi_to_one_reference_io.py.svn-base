# multiple references the same list
import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$y0','int'],['$y1','int'],['$y2','int'],
]

tuple_list = [
	['py_list_multi_reference_io_',
	# Ming : can you add a few more?
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

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
