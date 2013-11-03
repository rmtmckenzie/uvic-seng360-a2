# for loop with break
import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$x0','int'],['$x1','int'], ['$x2','int'], ['$y0','int'],['$y1','int']
]

tuple_list = [
	['py_for_break_io_',
	# forward
        [1,2,1, None,None],
        [1,2,2, None,None],
        [1,3,3, None,None],
        [1,4,4, None,None],
        [2,5,5, None,None],

	# backward/mixed: Ming please add 3 more
	[3,None,None,9,None],
	[4,None,None,7,None],
	[5,None,None,11,None],
	]
]

global_code_template = '''\
x	import sys
'''

main_code_template = '''\
dx	s = $x0
dx	for i in range(1,$x1):
dx		if i % $x2 == 0:
dx			break
dx		s += i
dx	print s,i
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0 $y1
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
