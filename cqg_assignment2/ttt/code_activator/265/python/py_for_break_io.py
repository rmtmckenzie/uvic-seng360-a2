question_type = 'input_output'

source_language = 'python'

parameter_list = [
        ['$x0','int'],['$x1','int'], ['$x2','int'], ['$y0','int'],['$y1','int']
]

tuple_list = [
	['py_for_break_io_',
	# forward
        [0,2,2, None,None],
        [0,3,3, None,None],
        [0,4,4, None,None],
        [2,5,5, None,None],

	# backward/mixed
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
