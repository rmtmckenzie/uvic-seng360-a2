traffic = [
	["10.0.0.3", "$x", "202.168.0.1", "$x", "private", "$x"],
	["$x", "$x", "$x", "$x", "public", "$x"],
	["10.0.0.2", "35536", "202.168.0.2", "22", "private", "$x"],
	["10.0.0.3", "$x", "202.168.0.1", "$x", "private", "$x"],
	["$x", "$x", "$x", "5001", "public", "$x"],
]

tuples = [
	{'traffic':[
		'32768','22',None,
		None,None,None,None,None,
		None,
		'65535','22',None,
		None,None,None,None],
	'tracking':[]},
	{'traffic':[
		'65535','80',None,
		None,None,None,None,None,
		None,
		'65535','80',None,
		None,None,'11.0.0.1',None],
	'tracking':[]},
	{'traffic':[
		'65535','80',None,
		'202.168.0.1','80','11.0.0.1',None,'N',
		None,
		'65535','80',None,
		None,None,'11.0.0.1','Y'],
	'tracking':[]},
	{'traffic':[
		'65535','80',None,
		'202.168.0.1','80','11.0.0.1',None,'Y',
		None,
		'65535','80',None,
		None,None,'11.0.0.1','N'],
	'tracking':[]},
	{'traffic':[
		'65535','22',None,
		None,None,'11.0.0.1',None,'Y',
		None,
		'65535','22',None,
		None,'22','11.0.0.1','Y'],
	'tracking':[]},


	{'traffic':[
		'65000','22',None,
		None,None,None,None,None,
		None,
		'32769','22',None,
		None,None,None,None],
	'tracking':[]},
	{'traffic':[
		'32769','6667',None,
		None,None,None,None,None,
		None,
		'32769','6667',None,
		None,None,'11.0.0.1',None],
	'tracking':[]},
	{'traffic':[
		'32769','6667',None,
		'11.0.0.3','37769','11.0.0.1','5000',None,
		None,
		'32769','6667',None,
		None,None,'11.0.0.1','Y'],
	'tracking':[]},
	{'traffic':[
		'32769','6667',None,
		'202.168.0.1','6667','11.0.0.1',None,'Y',
		None,
		'32769','6667',None,
		None,None,'11.0.0.1','N'],
	'tracking':[]},
	{'traffic':[
		'32769','22',None,
		None,None,'11.0.0.1',None,'Y',
		None,
		'32769','22',None,
		None,'22','11.0.0.1','Y'],
	'tracking':[]},
]

