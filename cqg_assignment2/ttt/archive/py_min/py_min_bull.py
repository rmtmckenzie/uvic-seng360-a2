import question_template

game_type = 'bullseye'
source_language = 'python'

parameter_list = [
	['$t0','target'],['$t1','target'],['$x1','int'],['$x2','int']
]

tuple_list = [
	['py_min_bull_',
                [True,False,1,None],
                [True,False,None,None],
                [False,True,None,7]
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
