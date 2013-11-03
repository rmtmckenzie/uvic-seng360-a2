question_tuples = [ 
	[   
		'fdb_mixed',
		{   
			# Traffic table
			'traffic_table': 
			[   
				# Src, Dest, Port
				[None,'b',1],
				['c',None,2],
				[None,'c',None],
			],  

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[['a'],None,None,[]],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a',None,1,None]
		},
		{   
			# Traffic table
			'traffic_table': 
			[   
				# Src, Dest, Port
				[None,'b',1],
				['c','d',2],
				[None,'c',None],
			],  

			# FDB table
			# [Port1, Port2, Port3, Port4]
			'fdb':[None,None,[],['d']],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a','b',1,[2,3,4]]
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
			'fdb':[[],[],None,['e']],

			# Forward result
			# Src, Dest, Port, result_ports
			'f_result':['a','e',3,None]
		},
	]
]
