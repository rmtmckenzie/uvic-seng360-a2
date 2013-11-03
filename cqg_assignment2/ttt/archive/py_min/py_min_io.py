import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
	['$i1','int'],['$x0','int'],['$y0','int']
]

tuple_list = [
	['py_min_io_forward_',	[1,2,None],	[4,9,None]],
	['py_min_io_backward_',	[None,None,2],	[None,None,6]],
	['py_min_io_mixed_',	[None,2,None],	[3,None,1]],
	['py_min_io_open_',	[None,None,None]],
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
dx	print min($i1,int(sys.argv[1]))
'''

argv_template = '$x0'

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
