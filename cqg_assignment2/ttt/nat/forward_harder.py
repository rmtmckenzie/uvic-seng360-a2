traffic = [
	["10.0.0.2", "$x1", "11.0.0.2", "$x2", "private", "$x3"],
	["11.0.0.2", "$x4", "11.0.0.1", "$x5", "public", "$x6"],
	["10.0.0.2", "$x7", "11.0.0.2", "$x8", "private", "$x9"],
	["10.0.0.2", "$xa", "11.0.0.3", "$xb", "private", "$xc"],
	["11.0.0.2", "$xd", "11.0.0.1", "$xe", "public", "$xf"]
]

tuples = [
	{'traffic':['32769','80',None,'80','5001',None,'32768','80',None,'35000','80',None,'80','5002',None],
	'tracking':[ [0,i] for i in range(8) ]},
	{'traffic':['35667','80',None,'80','5001',None,'32768','80',None,'39000','80',None,'81','5001',None],
	'tracking':[ [2,i] for i in range(8) ]},
	{'traffic':['35667','80',None,'80','5000',None,'35667','80',None,'39000','80',None,'80','5002',None],
	'tracking':[ [1,i] for i in range(8) ]},
	{'traffic':['35667','80',None,'80','5002',None,'35667','80',None,'39000','80',None,'39000','5001',None],
	'tracking':[ [1,i] for i in range(8) ]},
	{'traffic':['32769','80',None,'80','5001',None,'42355','80',None,'36000','80',None,'80','5003',None],
	'tracking':[ [0,i] for i in range(8) ]},

	{'traffic':['35000','6667',None,'80','5000',None,'35001','81',None,'35002','22',None,'80','5002',None],
	'tracking':[ [0,i] for i in range(8) ]},
	{'traffic':['65535','80',None,'80','5001',None,'32768','80',None,'39000','80',None,'81','5001',None],
	'tracking':[ [2,i] for i in range(8) ]},
	{'traffic':['35667','80',None,'80','5000',None,'35667','80',None,'39000','80',None,'80','5002',None],
	'tracking':[ [1,i] for i in range(8) ]+[ [0,i] for i in range(8) ]},
	{'traffic':['39080','80',None,'80','5002',None,'39000','80',None,'39002','80',None,'39000','5001',None],
	'tracking':[ [1,i] for i in range(8) ]+[ [0,i] for i in range(8) ]},
	{'traffic':['32769','80',None,'80','5001',None,'42355','80',None,'36000','80',None,'80','5003',None],
	'tracking':[ [0,i] for i in range(8) ]+[ [2,i] for i in range(8) ]},
]

