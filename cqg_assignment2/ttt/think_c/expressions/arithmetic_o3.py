import generate_util

''' ----------------------- SAFETY PROOF
zero divide
	/,% in op2 only
	d != 0
integer overflow
	input_list items at most 2 digits: a * b * c * d < 10^8
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$L0','ascii_string'],	# 0: parentheses
	['$a','int'],		# 1: input
	['$op0','ascii_string'],# 2: safe operator
	['$b','int'],		# 3: input
	['$R0','ascii_string'],	# 4: parentheses

	['$op1','ascii_string'],# 5: safe operator

	['$L1','ascii_string'],	# 6: parentheses
	['$c','int'],		# 7: input
	['$op2','ascii_string'],# 8: operator
	['$d','int'],		# 9: input
	['$R1','ascii_string'],	# 10: parentheses

	['$y','int']		# 11: output
]

operator_indexes = [2,5,8]
operators = ['+','-','*','/','%']
safe_operators = ['+','-','*']

substitute_indexes = [1,3,7,9]
substitute_values = [ [5,3,2,1], [7,5,3,2], [11,7,5,3], [13,11,7,5], ]

raw_group_list = [
	# (a op1 b) op1 c op2 d
	['arithmetic_o2_lp_',
	 ['(','$a',safe_operators,'$b',')', safe_operators,
	 '','$c',operators,'$d','', None]],

	# a op1 b op1 (c op2 d)
	['arithmetic_o2_rp_',
	 ['','$a',safe_operators,'$b','', safe_operators,
	 '(','$c',operators,'$d',')', None]],

	# (a op1 b) op1 (c op2 d)
	['arithmetic_o2_2p_',
	 ['(','$a',safe_operators,'$b',')', safe_operators,
	 '(','$c',operators,'$d',')', None]],
]

G = generate_util.Group_list(raw_group_list,12)
G.cross_product('c%i_',operator_indexes)
G.substitute(None,substitute_indexes,substitute_values)
group_list = G.group_list

print '***** expected number of questions:', \
	len(raw_group_list) * len(safe_operators)**2 * len(operators) * \
	len(substitute_values)
#	= 3 * 3**2 * 5 * 4 = 540

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		printf("%d\\n", $L0$a $op0 $b$R0 $op1 $L1$c $op2 $d$R1);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
