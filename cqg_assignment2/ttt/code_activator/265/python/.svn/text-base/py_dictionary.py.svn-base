question_type = 'input_output'

source_language = 'python'

parameter_list = [
        ['$L0','int'], ['$L1','int'], ['$L2','int'],
	['$y0','int'], ['$y1','int'], ['$y2','int'],
]

tuple_list = [
	['py_dictionary_forward',
        ['a','b','c', None,None,None],
        ['x','b','c', None,None,None],
        ['a','y','c', None,None,None],
        ['a','b','z', None,None,None],
	],
	#['py_dictionary_backward_',
        #[None,None,None, 1,2,3],
        #[None,None,None, 'x',2,3],
        #[None,None,None, 1,'x',3],
        #[None,None,None, 1,2,'x'],
#	],
]

global_code_template = '''\
'''

main_code_template = '''\
dx	d = { 'a':1, 'b':2, 'c':3 }
dx	
dx	L = [ '$L0', '$L1', '$L2' ]
dx	
dx	for x in L:
dx		if x in d:
dx			print d[x]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
