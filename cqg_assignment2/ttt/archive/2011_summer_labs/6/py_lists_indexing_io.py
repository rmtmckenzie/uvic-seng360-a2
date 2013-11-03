# what are the illegal/legal indexes of a list

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$x0','int'],['$y0','int'],
]

tuple_list = [
	['py_list_indexing_io_',
	# legal
	[0,None],
	[1,None],
	[2,None],
	[3,None],
	[4,None],
	[-1,None],
	[-2,None],
	[-3,None],
	[-4,None],
	[-5,None],

	# illegal
	
	[-6,None],
	[-7,None],
	[-8,None],
	[-9,None],
	[5,None],
	[6,None],
	[7,None],
	[8,None],
	]
]

# illegle: group 1: $x0 < -5; group 2: $x0 > 4
# legal: -5 <= $x0 <= 4
global_code_template = '''\
x	import sys

'''

main_code_template = '''\
dx	L = [2,4,6,8,0]
dx	try:
dx		print L[$x0]
dx	except IndexError:
dx		print 99
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
