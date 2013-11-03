'''
Definitions:
	bitstring: a nonempty string comprising only characters in ['0','1']
'''

def from_int(width,value):
	'''
	Purpose
		returns bitstring representation of value. leading 0s are
		prepended to make the result exactly width chars wide.
	Precondition
		width is a positive int
		value is a non-negative int
		binary representation of value fits into width bits
	'''
	bitstring = bin(value)[2:] # omit "0b" prefix
	padding = width - len(bitstring)
	return '0'*padding + bitstring

def to_int(bitstring):
	'''
	Purpose
		returns the unsigned integer value of bitstring.
	Precondition
		bitstring is a bitstring
	'''
	return eval('0b'+bitstring)

def cqg_xor(a,b):
	'''
	Purpose
		xor two bitstrings
	Precondition
		a and b are bitstrings
		a and b must be of the same length
	'''
	result = ''
	for i in range(len(a)):
		if(a[i] == b[i]):
			result += '0'
		else:
			result += '1'
	return result

def cqg_and(a,b):
	'''
	Purpose
		and two bitstrings
	Precondition
		a and b are bitstrings
		a and b must be of the same length
	'''
	result = ''
	for i in range(len(a)):
		if(a[i] == '1' and  b[i] == '1'):
			result += '1'
		else:
			result += '0'
	return result
