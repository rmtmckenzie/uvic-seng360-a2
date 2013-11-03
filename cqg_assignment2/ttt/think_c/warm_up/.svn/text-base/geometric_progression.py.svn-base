import sys
import generate_util

'''
----- safety proof
all questions safe
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a0','int'],['$r','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],['$y3','int'],['$y4','int'],
]

group_templates = [
	 [ 'geometric_progression_a_h%i_', [1,2, 1,2,4,8,16] ],
	 [ 'geometric_progression_b_h%i_', [1,5, 1,5,25,125,625] ],
	 [ 'geometric_progression_c_h%i_', [7,3, 7,21,63,189,567] ],
]

print '***** expected number of questions:', \
 len(group_templates) * (generate_util.n_c_k(7,1) + generate_util.n_c_k(7,2))

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
dx		int a,r,i;
dx
dx		a = $a0;
dx		r = $r;
dx		i = 0;
dx		while (i < 5) {
dx			printf("%d\\n",a);
dx			a = a * r;
dx			i++;
dx		}
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
$y3
$y4
'''
