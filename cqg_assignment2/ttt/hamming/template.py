tuples = \
[
	['fill_checkbits_',
		['0',0,[1,2]],
		['0',0,[1]],
		['0',0,[2]],
		['10',0,[1,2,4]],
		['10',0,[1]],
		['10',0,[2]],
		['10',0,[4]],
		['0101010',0,[1,2,4,8]],
		['0101010',0,[1]],
		['0101010',0,[2]],
		['0101010',0,[4]],
		['0101010',0,[8]],
	],
	['fill_checkbits_marked_',
		['0110111',1,[2]],
		['0110111',1,[4]],
		['0110111',1,[8]],
	],

	['fill_databits_',
		['0',0,[3]],
		['0',0,range(1,4)],
		['10',0,[3]],
		['10',0,[5]],
		['10',0,[3,5]],
		['10',0,range(1,6)],
		['0101010',0,[3]],
		['0101010',0,[5]],
		['0101010',0,[6]],
		['0101010',0,[7]],
		['0101010',0,[9]],
		['0101010',0,[10]],
		['0101010',0,[11]],
		['0101010',0,[3,5]],
		['0101010',0,[7,9]],
		['0101010',0,[6,11]],
		['0101010',0,[3,5,6,7,9,10,11]],
		['0101010',0,range(1,12)],
	],
	['fill_databits_marked_',
		['0110111',1,[6,11]],
		['0110111',1,[3,5,6,7,9,10,11]],
		['0110111',1,range(1,12)],
	],

	['finderror_',
		['0',0,1],
		['0',0,2],
		['0',0,3],
		['10',0,1],
		['10',0,3],
		['10',0,5],
		['0101010',0,1],
		['0101010',0,6],
		['0101010',0,11],
	],
	['finderror_marked_',
		['0110111',1,1],
		['0110111',1,6],
		['0110111',1,11],
	],
]
