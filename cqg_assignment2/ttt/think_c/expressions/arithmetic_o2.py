import generate_util

'''----------------------- SAFETY PROOF
zero divide: /,%
	1. a, b, c > 0
		negative: undefined for %
		0: problems for / %
	2. b >= c
		so b/c != 0
	3. b not divisible by c
		so b%c != 0
integer overflow
	input_list items at most 2 digits: a * b * c < 10^6
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$L0','ascii_string'],	# 0: parentheses
	['$a','int'],		# 1: input
	['$op0','ascii_string'],# 2: operator
	['$L1','ascii_string'],	# 3: parentheses
	['$b','int'],		# 4: input
	['$R0','ascii_string'],	# 5: parentheses
	['$op1','ascii_string'],# 6: operator
	['$c','int'],		# 7: input
	['$R1','ascii_string'],	# 8: parentheses
	['$y','int']		# 9: output
]

operator_indexes = [2,6]
operators = ['+','-','*','/','%']

substitute_indexes = [1,4,7]
substitute_values = [ [5,3,2], [7,5,3], [11,7,5], [13,11,7], ]

# Note: the list could be replaced by a single item with Group_list.substitute
raw_group_list = [
	# a op0 b op1 c
	['arithmetic_o2_np_', # no parentheses
		['','$a',operators,'','$b','',operators,'$c','',None] ],

	# (a op0 b) op1 c
	['arithmetic_o2_lp_', # left parentheses
		['(','$a',operators,'','$b',')',operators,'$c','',None] ],

	# a op0 (b op1 c)
	['arithmetic_o2_rp_', # right parentheses
	['','$a',operators,'(','$b','',operators,'$c',')',None] ],
]

print '***** expected number of questions:', \
len(raw_group_list) * len(operators)**2 * len(substitute_values)
#3                    5**2                4        == 300

G = generate_util.Group_list(raw_group_list,10)

G.cross_product('c%i_',operator_indexes)

G.substitute(None,substitute_indexes,substitute_values)

group_list = G.group_list

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		printf("%d\\n", $L0$a $op0 $L1$b$R0 $op1 $c$R1);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
