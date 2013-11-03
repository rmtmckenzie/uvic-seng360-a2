import copy
import generate_util

'''
----- safety proof
all questions safe
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$r','int'],
	['$y0','float'],['$y1','float'],['$y2','float'],
]

raw_group_list = [
	 [ 'newton_method_1_h%i_', [1, '1.000','1.000','1.000'] ],
	 [ 'newton_method_2_h%i_', [2, '1.500','1.417','1.414'] ],
	 [ 'newton_method_3_h%i_', [3, '2.000','1.750','1.732'] ],
	 [ 'newton_method_4_h%i_', [4, '2.500','2.050','2.001'] ],
	 [ 'newton_method_5_h%i_', [5, '3.000','2.333','2.238'] ],
	 [ 'newton_method_6_h%i_', [6, '3.500','2.607','2.454'] ],
	 [ 'newton_method_7_h%i_', [7, '4.000','2.875','2.655'] ],
	 [ 'newton_method_8_h%i_', [8, '4.500','3.139','2.844'] ],
	 [ 'newton_method_9_h%i_', [9, '5.000','3.400','3.024'] ],
	 [ 'newton_method_10_h%i_', [10,'5.500','3.659','3.196'] ],
]
hotspot_counts = [1,2,3]
hotspot_indexes = [1,2,3]

# generate 3 groups, 1 for each hotspot count
raw_group_list0 = copy.deepcopy(raw_group_list)
for g in raw_group_list0:
	g[0] = g[0] % 1
G1 = generate_util.Group_list(raw_group_list0,4)
G1.generalize(None,hotspot_indexes,1)

raw_group_list0 = copy.deepcopy(raw_group_list)
for g in raw_group_list0:
	g[0] = g[0] % 2
G2 = generate_util.Group_list(raw_group_list0,4)
G2.generalize(None,hotspot_indexes,2)

raw_group_list0 = copy.deepcopy(raw_group_list)
for g in raw_group_list0:
	g[0] = g[0] % 3
G3 = generate_util.Group_list(raw_group_list0,4)
G3.generalize(None,hotspot_indexes,3)

# concatenate for solution
group_list = G1.group_list + G2.group_list + G3.group_list

print '***** expected number of questions:', len(raw_group_list) * \
(generate_util.n_c_k(3,1) + generate_util.n_c_k(3,2) + generate_util.n_c_k(3,3))
#	= 10 * (3 + 3 + 1) = 70

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		int r,i;
dx		double x;
dx
dx		r = $r;
dx		x = 1.0;
dx		for (i = 0; i < 3; i++) {
dx			x = (x + r/x) / 2;
dx			printf("%4.3f\\n",x);
dx		}
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
