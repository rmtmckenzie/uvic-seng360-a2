import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$a','int'], ['$b','int'], ['$c','int'], ['$y','int'],
]

group_list = [
	['min_three_io_h1_'] + generate_util.generalize([1,2,3,1],1),

	['min_three_io_h2_'] + generate_util.generalize([1,2,3,1],2),

	['min_three_io_cp_'] + generate_util.cross_product_sublist \
	 ( [ [1,2,5],[3,4,7],[5,6,9],None ], [0,1,2])
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a,b,c;
dx
dx		a = $a;
dx		b = $b;
dx		c = $c;
dx
dx		if (a < b) {
dx			if (a < c) {
dx				printf("%d\\n",a);
dx			} else {
dx				printf("%d\\n",c);
dx			}
dx		} else {
dx			if (b < c) {
dx				printf("%d\\n",b);
dx			} else {
dx				printf("%d\\n",c);
dx			}
dx		}
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
