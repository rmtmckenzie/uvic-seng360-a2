question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$n','int'],['$y0','int'], ['$y1','int'], ['$y2','int'],['$y3','int']
]

group_list = [
	['shift_io_easy_',
	# forward
        [0, None,None,None,None],
        [1, None,None,None,None],
        [2, None,None,None,None],
        [3, None,None,None,None],
	],

	['shift_io_hard_',
	[20, None,None,None,None],
	[21, None,None,None,None],
	[22, None,None,None,None],
	[23, None,None,None,None],
	[24, None,None,None,None],
	[25, None,None,None,None],
	[26, None,None,None,None],
	]
]

global_code_template = '''\
'''

main_code_template = '''\
dx	w,x,y,z = 0,1,2,3
dx	
dx	for i in range($n):
dx		w,x,y,z = x,y,z,w
dx	
dx	print w,x,y,z
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0 $y1 $y2 $y3
'''
