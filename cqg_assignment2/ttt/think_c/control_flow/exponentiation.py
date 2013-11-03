import sys
import generate_util

'''
----- safety proof
all questions safe
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$b','int'],['$e','int'],['$y','int'],
]

group_templates = [
	[ 'exponentiation_a_h%i_', [2,3,8] ],
	[ 'exponentiation_b_h%i_', [3,3,27] ],
	[ 'exponentiation_c_h%i_', [1,3,1] ],
	[ 'exponentiation_d_h%i_', [2,0,1] ],
]

print '***** expected number of questions:', \
 len(group_templates) * (generate_util.nCk(3,1) + generate_util.nCk(3,2))

group_list = [ ]
for g in group_templates:
	for h in [1,2]:
		group_list.append([g[0]%h] + generate_util.generalize(g[1],h))

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		int r,b,e,i;
dx		b = $b;
dx		e = $e;
dx
dx		r = 1;
dx		for (i = 0; i < e; i++)
dx			r = r * b;
dx
dx		printf("%d\\n",r);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
