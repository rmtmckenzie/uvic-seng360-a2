question_tuples = [ 
	[   
		'fdb_backward',
		{   
			# Traffic table
			'traffic_table': 
			[   
				# Src, Dest, Port
				['a','b',1],
				['c','d',2],
				[None,'c',3],
			],  

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[['a'],['c'],['b'],[]],

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
				['d','c',None],
			],  

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[['a'],['c'],[],['d']],

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
				[None,'d',3],
			],  

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[[],[],['a','c'],['e']],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a','e',3,None]
		},
	]
]
