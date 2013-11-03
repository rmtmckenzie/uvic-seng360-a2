# list is referenced by references not by copy
import question_template

game_type = 'input_output'
source_language = 'python'

parameter_list = [
        ['$x0','int'],['$x1','int'], ['$x2','int'],['$x3','int'], ['$y0','int']
]

tuple_list = [
	['py_lists_reference_semantics_io_',
	# forward
	[0,0,1,1,None],
	[1,1,3,2,None],
	[2,1,4,3,None],
	[3,2,5,4,None],
	[4,3,5,5,None],

	# Ming please add a few backward/mixed tuples
	[3,None,None,4,13],
	[1,None,3,None,9],
	[None,None,None,None,11],
	[None,2,None,4,15],
	]
]

global_code_template = '''\
x	import sys

dx	def list_sum(L):
dx		sum = 0
dx		for i in L:
dx			if type(i) == int:
dx				sum += i
dx			else:
dx				sum += list_sum(i)
dx		return sum
dx	
'''

main_code_template = '''\
dx	X = [$x0,range($x1,$x2),$x3]
dx	print list_sum(X)
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
