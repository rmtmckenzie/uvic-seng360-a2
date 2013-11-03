import generate_util

# generation code for operator precedence questions

binary_operator_precedence = [ # precedence is row number from Table 7.1
	['*',1], ['/',1], ['%',1],
	['+',2], ['-',2],
	['<<',3], ['>>',3],
	['<',4], ['<=',4],['>',4], ['>=',4],
	['==',5], ['!=',5],
	['&',6],
	['^',7],
	['|',8],
	['&&',9],
	['||',10],
]

def precedence(operator0,operator1):
	question = '''\
	Consider the binary operators <tt>$operator0</tt> and
	<tt>$operator1</tt>.
	Does <tt>$operator0</tt> have higher, equal, or lower precedence
	than <tt>$operator1</tt>?
	'''
	question = question.replace('$operator0',operator0[0])
	question = question.replace('$operator1',operator1[0])
	if operator0[1] < operator1[1]:
		correct_index = 0
	elif operator0[1] == operator1[1]:
		correct_index = 1
	else:
		correct_index = 2
	return [question, ['higher','equal','lower'], correct_index]

L = generate_util.choose_k(binary_operator_precedence,2)
L_swapped = [ [p[1],p[0]] for p in L ]

print 'expected number of multiple_choice_7_1_ questions:', \
	len(L)+len(L_swapped)

question_groups = [

['multiple_choice_7_1_'] + # structure and value of an expression -----
	[ precedence(p[0],p[1]) for p in (L + L_swapped) ]

]
