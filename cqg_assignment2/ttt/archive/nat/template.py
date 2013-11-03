traffic = [
	["10.0.0.2", "$x1", "11.0.0.2", "$x2", "private", "$x3"],
	["11.0.0.2", "$x4", "11.0.0.1", "$x5", "public", "$x6"],
	["10.0.0.2", "$x7", "11.0.0.2", "$x8", "private", "$x9"],
	["10.0.0.2", "$xa", "11.0.0.2", "$xb", "private", "$xc"],
	["11.0.0.2", "$xd", "11.0.0.1", "$xe", "public", "$xf"]
]

tuples = [
	{'traffic':['5000','80',None,'80','5001',None,'3000','80',None,'80','5000',None,'80','5002',None],
	'tracking':[]},
	{'traffic':['5000','80',None,'80','5001',None,'3000','80',None,'80','5000',None,'80','5002',None],
	'tracking':[ [1,2], [2,6] ]},
	{'traffic':[None,None,'Y',None,None,'N',None,None,'Y',None,None,'Y',None,None,'N'],
	'tracking':[]},
	{'traffic':[None,None,'Y','80',None,None,'3000',None,None,'80',None,'Y',None,'5002',None],
	'tracking':[]},
]

