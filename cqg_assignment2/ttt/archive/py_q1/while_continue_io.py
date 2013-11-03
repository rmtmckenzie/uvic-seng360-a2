# while loop with continue
import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$x0','int'],['$x1','int'],['$x2','int'],['$x3','int'],
	['$y0','int'],['$y1','int'],
]

tuple_list = [
	['py_while_continue_io_',
	# forward
        [0,1,0,3, None,None],
        [0,2,1,2, None,None],
        [0,3,0,5, None,None],
        [0,4,1,3, None,None],
        [2,5,2,4, None,None],

	# backward/mixed: Ming please add 3 more
	[None,	None,	None,	4,	16,	3],
	[3,	None,	None,	2,	None,	7],
	[None,	2,	4,	3,	None,	None],
	]
]

global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	s = $x0
dx	i = $x1
dx	while i > $x2:
dx		i -= 1
dx		if (i%$x3 == 0):
dx			continue
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
