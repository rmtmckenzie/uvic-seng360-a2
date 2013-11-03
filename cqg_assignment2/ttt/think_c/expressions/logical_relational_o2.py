import generate_util

'''
----------------------- SAFETY PROOF
no issues
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$x0','int'],			# 0: input
	['$y0','int'],			# 1: input

	['$not','ascii_string'],	# 2: cross_product

	['$L','ascii_string'],		# 3: hotspot_value constant
	['$relop0','ascii_string'],	# 4: cross_product
	['$logop0','ascii_string'],	# 5: cross_product
	['$exp','ascii_string'],	# 6: cross_product
	['$R','ascii_string'],		# 7: hotspot_value constant

	['$logop1','ascii_string'],	# 8: cross_product
	['$relop1','ascii_string'],	# 9: cross_product

	['$y','string']			# 10: output
]

logical_operators = ['&&','||']
not_operator = ['!','']
relational_operators = ['<','<=','==','!=','>','>=']
expressions = ['x < 0', 'y > 0']

cross_product_indexes = [2,4,5,6,8,9]

substitute_values = [ [1,2], [3,4], ]
substitute_indexes = [0,1]

raw_group_list = [

	# x $relop0 y $logop0 $exp $logop1 y $relop1 x
	['logical_relational_o2_np_',
	 ['$x0', '$y0',
	 [''], '', relational_operators, logical_operators,
	 expressions, '', logical_operators,
	 relational_operators, None]],

	# ! ( x $relop0 y $logop0 $exp ) $logop1 y $relop1 x
	['logical_relational_o2_p_',
	 ['$x0', '$y0',
	 not_operator, '(', relational_operators, logical_operators,
	 expressions, ')', logical_operators,
	 relational_operators, None]],
]

G = generate_util.Group_list(raw_group_list,12)
G.cross_product('c%i_',cross_product_indexes)
G.substitute(None,substitute_indexes,substitute_values)
group_list = G.group_list

print '***** expected number of questions:', \
	len(substitute_values) * \
	len(relational_operators) * \
	len(logical_operators) * \
	len(expressions) * \
	len(logical_operators) * \
	len(relational_operators) * \
	3 # not operator: group[0]:1; group[1]:2
#       = 2 * 6 * 2 * 2 * 2 * 6 * 3 = 1728

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int x,y;
dx		
dx		x = $x0;
dx		y = $y0;
dx		
dx		if ($not$Lx $relop0 y $logop0 $exp$R $logop1 y $relop1 x)
dx			printf("A");
dx		else
dx			printf("B");
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
