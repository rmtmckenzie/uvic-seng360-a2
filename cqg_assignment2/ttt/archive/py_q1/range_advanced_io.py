# range(L,U) half open, half closed
import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$x0','int'],['$x1','int'],['$x2','int'],['$x3','int'],['$x4','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],['$y3','int'],
]

tuple_list = [
	['py_range_advanced_io_',
	# forward
        [1,0, 1,6,1, None,None, None,None],
        [2,1, 1,5,2, None,None, None,None],
        [5,2, 1,6,3, None,None, None,None],
        [5,3, 2,5,2, None,None, None,None],
        [5,4, 2,6,3, None,None, None,None],

	# mixed: Ming please add 2 more
        [5,None, 2,5,1, None,3, None,None],
        [6,None, 3,4,0, None,2, None,None],
        [6,None, 1,5,3, None,4, None,None],
	]
]

global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	L = range($x0)
dx	print L[0],L[$x1]
dx
dx	L = range($x2,$x3)
dx	print L[-1],L[$x4]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0 $y1
$y2 $y3
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
