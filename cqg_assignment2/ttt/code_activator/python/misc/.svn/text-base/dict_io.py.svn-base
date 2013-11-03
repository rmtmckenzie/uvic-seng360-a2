question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$L0','string'], ['$L1','string'], ['$L2','string'],
	['$y0','string'], ['$y1','string'], ['$y2','string'],
]

group_list = [
	['dict_io_forward_',
        ['a','b','c', None,None,None],
        ['x','b','c', None,None,None],
        ['a','y','c', None,None,None],
        ['a','b','z', None,None,None],
	],
	#['dict_io_backward_',
        #[None,None,None, 1,2,3],
        #[None,None,None, 'x',2,3],
        #[None,None,None, 1,'x',3],
        #[None,None,None, 1,2,'x'],
#	],
]

global_code_template = '''\
'''

main_code_template = '''\
dx	D = { 'a':1, 'b':2, 'c':3 }
dx	
dx	L = [ '$L0', '$L1', '$L2' ]
dx	
dx	for x in L:
dx		if x in D:
dx			print D[x]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
