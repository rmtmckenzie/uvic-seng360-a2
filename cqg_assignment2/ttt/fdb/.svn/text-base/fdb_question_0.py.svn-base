def make_tuples(traffic_tables,results):
	pass
	tuples = []
	for t in traffic_tables:
		for f in results:
			d = {
				'traffic_table':t,
				'fdb':[None,None,None,None],
				'f_result':f
			}
			tuples += [d]
	return tuples

traffic_tables = [ \
	[ ['a','b',1] ],
	[ ['b','d',1], ['e','d',2] ],
	[ ['c','d',1], ['c','d',1] ],

	[ ['d','e',3], ['c','d',1], ['b','c',2],
	  ['a','e',3], ['c','d',2], ['d','c',3] ],

	[ ['a','b',1], ['c','d',2], ['a','c',3] ], # move a
	[ ['b','d',1], ['e','d',2], ['c','d',1] ], # 2 devices on same port
	[ ['c','d',1], ['c','d',2], ['b','c',3] ],
	[ ['d','e',1], ['c','d',2], ['b','c',3] ],
]

results = [ \
	['a','b',1,None],
	['b','c',1,None],
	['c','e',1,None],
]

question_tuples = [
	['fdb_forward'] + 
	make_tuples(traffic_tables,results)
]

#print question_tuples

'''
question_tuples = [
	[
		'fdb_forward',
		{
			# Traffic table
			'traffic_table':
			[
				# Src,	Dest,	Port
				['a',	'b',	1],
				['c',	'd',	2],
				['b',	'c',	3],
			],

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[None,None,None,None],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a','b',1,None]
		},
		{
			# Traffic table
			'traffic_table':
			[
				# Src, Dest, Port
				['a','b',1],
				['c','d',2],
				['b','c',3],
			],

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[None,None,None,None],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a','d',1,None]
		},
		{
			# Traffic table
			'traffic_table':
			[
			# Src, Dest, Port
				['c','b',2],
				['a','d',3],
				['e','b',4],
				['c','d',1],
			],

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[None,None,None,None],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a','e',3,None]
		},
	]
]
'''
