# replace a list slice with a new list
import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$x0','int'],['$x1','int'],['$x2','int'],['$y0','int']
]

tuple_list = [
	['py_lists_slices_replace_io_',
	# forward
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

	# backward/mixed
	[None,1,None,2],
	[None,1,None,4],
	[None,2,None,0],
	[None,3,None,0],
	[None,4,None,0],
	[1,None,None,0],
	[2,None,None,0],
	[3,None,None,0],
	]
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

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
