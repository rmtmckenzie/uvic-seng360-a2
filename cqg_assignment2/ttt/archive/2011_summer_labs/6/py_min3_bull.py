# if,elif,else

game_type = 'bullseye'

source_language = 'python'

parameter_list = [
        ['$t0','target'], ['$t1','target'], ['$t2','target'],
	['$t3','target'], ['$t4','target'], ['$t5','target'],

	['$x0','int'], ['$x1','int'], ['$x2','int'],
]

tuple_list = [
	['py_min3_bull_',
	[True, False,False,False,False,False,None,None,None],
	[False,True ,False,False,False,False,None,None,None],
	[False,False,True ,False,False,False,None,None,None],
	[False,False,False,True ,False,False,None,None,None],
	[False,False,False,False,True ,False,None,None,None],
#	[False,False,False,False,False,True ,None,None,None],

	[True, False,False,False,False,False,None,1,    None],
	[False,True ,False,False,False,False,None,1,    None],
	[False,False,True ,False,False,False,None,1,    None],
	[False,False,False,True ,False,False,None,1,    None],
	[False,False,False,False,True ,False,None,1,    None],
#	[False,False,False,False,False,True ,None,1,    None],

	[True, False,False,False,False,False,None,None,2    ],
	[False,True ,False,False,False,False,None,None,2    ],
	[False,False,True ,False,False,False,None,None,2    ],
	[False,False,False,True ,False,False,None,None,2    ],
	[False,False,False,False,True ,False,None,None,2    ],
#	[False,False,False,False,False,True ,None,None,2    ],
	]
]

global_code_template = '''\
x	import sys

dx	def min3(a,b,c):
dx		if a < b:
dx			if a < c:
dx				$t0
dx				return a
dx			else:
dx				$t1
dx				return c
dx		elif a < c:
dx			if b < a:
dx				$t2
dx				return b
dx			else:
dx				$t3
dx				return a
dx		elif b < c:
dx			if b < a:
dx				$t4
dx				return b
dx			else:
dx				$t5
dx				return a
dx	
'''

main_code_template = '''\
dx	min3($x0,$x1,$x2)
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
