import question_template

game_type = 'find_the_failure'
source_language = 'python'

parameter_list = [
	['$x1','int'],['$x2','int']
]

tuple_list = [
	['py_min_ff_',	[1,None],[None,None],[None,7]]
]

global_code_template = '''\
xX	import sys
xX
d	\'\'\'
d	purpose
d	       return the smaller of a and b
d	precondition
d	        none
d	examples
d	        min(1,2) returns 1
d	        min(1,1) returns 1
d	        min(1,0) returns 0
d	\'\'\'
dxX	def min(a,b):
dxX		if a < b:
dxX			return a
dxX		else:
x			return b
dX			return a
dxX		
'''

main_code_template = '''\
dxX	print min($x1,$x2)
'''

argv_template = ''

stdin_template = ''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
