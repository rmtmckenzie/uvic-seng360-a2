game_type = 'input_output'
source_language = 'python'

parameter_list = [
	['$i1','int'],['$x0','int'],['$y0','int']
]

tuple_list = [
	['py_min_io_stdin_',	[4,9,None]],
]

global_code_template = '''\
x	import sys
x
dx	def min(a,b):
dx		if a < b:
dx			return a
dx		else:
dx			return b
dx		
'''

main_code_template = '''\
dx	print min($i1,
dx		min(int(sys.argv[1]),int(sys.stdin.read())))
'''

argv_template = '$x0'

stdin_template = '3'

stdout_template = '''\
$y0
'''
