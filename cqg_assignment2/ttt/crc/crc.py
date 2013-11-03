import generate_util
import crc_util

def raw_group(divisors,messages,qh,rh,wh):
	'''
	purpose
		return a group with:
			name: 'crc_d%i_m%i_' with divisor, message lengths
			divisors: a list of divisors of the same length
			messages: a list of messages of the same length
			forward only: no divisor or dividend hotspots
			quotient hotspots: list of all qh-tuples of hotspots
			remainder hotspots: list of all rh-tuples of hotspots
			work hotspots: list of all rh-tuples of hotspots
	preconditions
		divisors: non-empty list of bitstrings of length > 1
			all divisors are the same length
		messages: non-empty list of bitstrings of length >= d
			all messages are the same length
		qh, rh, wh: legal hotspot counts
	'''
	# extract divisor, message lengths
	d_len = len(divisors[0])
	m_len = len(messages[0])

	# compute quotient, remainder, work lengths
	q_len = crc_util.quotient_len(d_len,m_len)
	r_len = crc_util.remainder_len(d_len,m_len)
	num_rows = crc_util.number_of_rows(d_len,m_len)
	row_width = crc_util.row_width(d_len,m_len)

	# compute quotient, remainder, work index lists; index pairs for work
	q_indexes = range(0,q_len)
	r_indexes = range(0,r_len)
	w_indexes = generate_util.cross_product \
		([range(num_rows),range(row_width)])

	# create the group, ready for cross product
	return [ 'crc_d%i_m%i_' % (d_len,m_len), [
		divisors, messages, [ ], [ ],
		generate_util.choose_k(q_indexes,qh),
		generate_util.choose_k(r_indexes,rh),
		generate_util.choose_k(w_indexes,wh),
	]]

def raw_group_num_questions(divisors,messages,qh,rh,wh):
	'''
	purpose, preconditions, comments
		same as for group_count except that the number of questions
		generated by the return value of raw_group is returned
	'''
	d_len = len(divisors[0])
	m_len = len(messages[0])

	q_len = crc_util.quotient_len(d_len,m_len)
	r_len = crc_util.remainder_len(d_len,m_len)
	num_rows = crc_util.number_of_rows(d_len,m_len)
	row_width = crc_util.row_width(d_len,m_len)

	q_indexes = range(0,q_len)
	r_indexes = range(0,r_len)
	w_indexes = generate_util.cross_product \
		([range(num_rows),range(row_width)])

	return len(divisors) * len(messages) * \
		generate_util.n_c_k(q_len,qh) * \
		generate_util.n_c_k(r_len,rh) * \
		generate_util.n_c_k(num_rows*row_width,wh)

'''
STRATEGY
	INPUT
		0: divisors: supply list manually
		1: messages: supply list manually
		2: divisor hotspots: none; forward questions only
		3: dividend hotspots: none; forward questions only
	OUTPUT
		4: quotient hotspots: choose_k hotspots from list of all
		5: remainder hotspots: choose_k hotspots from list of all
		6: work hotspots: choose_k hotspots from list of all
	GENERATION
		apply cross product to
			divisor, message, quotient, remainder, work lists
'''

d_2 = ['10','11'] # divisors may not begin with '0'
m_2 = ['00','01','10','11']

d_3 = ['100','101','110','111']
m_3 = ['000','001','010','011', '100','101','110','111']

d_m_qh_rh_wh_list = [
	[ d_2, m_2, 1, 1, 2 ], # 240
	[ d_2, m_3, 1, 1, 2 ], # 2160
	[ d_3, m_3, 1, 1, 1 ], # 2860
	[ ['10100'], ['100000'], 1, 1, 1 ], # 1320
]

# generate groups
G0 = [ ]
for x in d_m_qh_rh_wh_list:
	G0.append(raw_group(x[0],x[1],x[2],x[3],x[4]))
G1 = generate_util.Group_list(G0,7)
G1.cross_product(None,[0,1,4,5,6])
group_list = G1.group_list
'''
for g in group_list:
	print g[0]
	for h in g[1:]:
		print '\t',h
'''

# compute counts
n = 0
print '***** expected number of questions:',
for x in d_m_qh_rh_wh_list:
	n += raw_group_num_questions(x[0],x[1],x[2],x[3],x[4])
print n
