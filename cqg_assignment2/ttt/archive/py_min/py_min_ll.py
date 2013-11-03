import question_template

import question_template

game_type = 'liar_liar'
source_language = 'python'

parameter_list = [
	['$t0','assert'],['$t1','assert'],['$x1','int'],['$x2','int']
]

tuple_list = [
	['py_min_ll_',
		['a > 5','',None,None],
		['','b < 6',None,7],
        ]
]

global_code_template = '''\
x	import sys
x
dx	def min(a,b):
dx		if a < b:
dx			$t0
dx			return a
dx		else:
dx			$t1
dx			return b
dx		
'''

main_code_template = '''\
dx	min($x1,$x2)
'''

argv_template = ''

stdin_template = ''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
