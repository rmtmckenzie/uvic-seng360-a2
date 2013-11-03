# list is referenced by references not by copy

question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$x0','int'],['$x1','int'], ['$x2','int'],['$x3','int'], ['$y0','int']
]

group_list = [
	['list_reference_semantics_io_forward_',
	[0,0,1,1,None],
	[1,1,3,2,None],
	[2,1,4,3,None],
	[3,2,5,4,None],
	[4,3,5,5,None],
	],

	['list_reference_semantics_io_mixed_backward_',
	[3,None,None,4,13],
	[1,None,3,None,9],
	[None,None,None,None,11],
	[None,2,None,4,15],
	],
]

global_code_template = '''\
x	import sys

dx	def operate(L):
dx		s = 0
dx		for i in L:
dx			if type(i) == int:
dx				s += i
dx			else:
dx				s += operate(i)
dx		return s
dx	
'''

main_code_template = '''\
dx	X = [$x0,range($x1,$x2),$x3]
dx	print operate(X)
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
