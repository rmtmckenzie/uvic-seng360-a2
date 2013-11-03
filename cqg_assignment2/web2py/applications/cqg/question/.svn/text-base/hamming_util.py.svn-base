import math

'''
TERMINOLOGY

bit string:
	non-empty Python string containing only '0's and '1's
message:
	bit string containing a message to be encoded
code word:
	bit string containing data bits from a message and check bits
check bit:
	code word bit in positions 1,2,4, ...
data bit:
	code word bit copied from a message to a position other than 1,2,4, ...
'''

def is_power_of_2(n):
	'''
	Purpose
		return true if n is a power of 2
	Preconditions
		type(n) == int and n > 0
	Examples
		if x in {1,2,4}
			is_power_of_2(x) returns True
		if x in {3,5,6}
			is_power_of_2(x) returns False
	'''
	return math.log(n,2) == math.floor(math.log(n,2))

def get_code_word_length(message_length):
	'''
	Purpose
		return the length of the code word which encodes
		a message bit string of length message_length
	Preconditions
		type(message_length) == int and n > 0
	Examples
		get_code_word_length(1) returns 3
		get_code_word_length(2) returns 5
		get_code_word_length(3) returns 6
		get_code_word_length(8) returns 12
	'''
	m_i,w_i = 0,1
	while m_i < message_length:
		if not is_power_of_2(w_i): # data bit
			m_i += 1
		w_i += 1
	return w_i-1

def get_check_bit_indexes(n):
	'''
	Purpose
		return a list containing the one-relative indexes
		of the check bits in a code word of length n
	Preconditions
		type(n) == int and n > 2
	Examples
		get_check_bit_indexes(3) returns [1,2]
		get_check_bit_indexes(5) returns [1,2,4]
		get_check_bit_indexes(6) returns [1,2,4]
		get_check_bit_indexes(12) returns [1,2,4,8]
	'''
	return filter(is_power_of_2,range(1,n+1))

def get_data_bit_indexes(n):
	'''
	Purpose
		return a list containing the one-relative indexes
		of the data bits in a code word of length n
	Preconditions
		type(n) == int and n > 2
	Examples
		get_data_bit_indexes(3) returns [3]
		get_data_bit_indexes(5) returns [3,5]
		get_data_bit_indexes(6) returns [3,5,6]
		get_data_bit_indexes(12) returns [3,5,6,7,9,10,11,12]
	'''
	return filter(lambda x: not is_power_of_2(x),range(1,n+1))

def generate_code_word(message,parity):
	'''
	Purpose:
		return a code word computed from message using parity p
	Preconditions:
		message is a non-empty bit string
		parity in [0,1]
	Examples
		generate_code_word('0',0) returns '000'
		generate_code_word('0',1) returns '110'
		generate_code_word('010',0) returns '100110'
	'''

	# compute code_word as list of int; convert to bit string at end

	# create the list skeleton; dummy element simulates 1-relative indexing
	code_word = [None] * (get_code_word_length(len(message))+1)

	# copy in message bits
	data_bit_indexes = get_data_bit_indexes(len(code_word)-1)
	m_i = 0
	for d_i in data_bit_indexes:
		code_word[d_i] = int(message[m_i])
		m_i += 1

	# compute check bits
	for c_i in get_check_bit_indexes(len(code_word)-1):
		# xor code_word[c_i] with each data bit it checks
		xor = parity
		# for data bits to the right of c_i
		for d_i in [i for i in data_bit_indexes if i > c_i]:
			if c_i & d_i != 0: # c_i checks d_i
				xor ^= code_word[d_i]
		code_word[c_i] = xor

	# convert to 0-relative bit string and return
	w = ''
	for b in code_word[1:]:
		w += str(b)
	return w

def check_code_word(code_word,parity):
	'''
	Purpose
		return the sum of the indexes of the bad check bits in 
		code_word, or 0 if all the check bits in code_word are correct
	Precondition
		code_word is a bitstring, len(code_word) >= 2
		parity in [0,1]
	Examples
		check_code_word('000',0) returns 0
		check_code_word('100',0) returns 1
		check_code_word('010',0) returns 2
		check_code_word('001',0) returns 3
	'''

	# add dummy element to simulate 1-relative indexing
	code_word = '2' + code_word

	index_sum = 0 # initialize accumulator for bad check bit indexes
	data_bit_indexes = get_data_bit_indexes(len(code_word)-1)
	for c_i in get_check_bit_indexes(len(code_word)-1):
		# xor code_word[c_i] with each data bit it checks
		xor = int(code_word[c_i])
		for d_i in [i for i in data_bit_indexes if i > c_i]:
			if c_i & d_i != 0: # c_i checks d_i
				xor ^= int(code_word[d_i])
		# accumulate index if failed check bit
		if xor != parity:
			index_sum += c_i

	return index_sum
