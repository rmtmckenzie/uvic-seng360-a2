import generate_util

question_type = 'bullseye'
source_language = 'C'

hotspot_declarations = [
	['$a','int'], ['$b','int'], ['$c','int'],
	['$t0','target'], ['$t1','target'], ['$t2','target'], ['$t3','target'],
]

group_list = [
	['min_three_be_',
	 [None,None,None, True,False,False,False],
	 [None,None,None, False,True,False,False],
	 [None,None,None, False,False,True,False],
	 [None,None,None, False,False,False,True],
	],
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
dx				$t0
dx				printf("%d\\n",a);
dx			} else {
dx				$t1
dx				printf("%d\\n",c);
dx			}
dx		} else {
dx			if (b < c) {
dx				$t2
dx				printf("%d\\n",b);
dx			} else {
dx				$t3
dx				printf("%d\\n",c);
dx			}
dx		}
'''

argv_template = ''

stdin_template = ''
