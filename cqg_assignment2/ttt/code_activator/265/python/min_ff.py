question_type = 'find_the_failure'
source_language = 'python'

parameter_list = [
	['$x1','int'],['$x2','int']
]

tuple_list = [
	['py_min_ff_',	[1,None],[None,None],[None,7]]
]

global_code_template = '''\
xX	import sys
dxX
'''

main_code_template = '''\
dxX	a = $x1
dxX	b = $x2
d	# print the smaller of a and b
dxX	if a < b:
dxX		print a
dxX	else:
dX		print a
x		print b
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
