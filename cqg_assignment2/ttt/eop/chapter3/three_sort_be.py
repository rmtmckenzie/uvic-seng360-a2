import generate_util

question_type = 'bullseye'
source_language = 'C'

hotspot_declarations = [
	['$a','int'], ['$b','int'], ['$c','int'],
	['$t0','target'], ['$t1','target'], ['$t2','target'],
]

group_list = [
	['three_sort_be_', 
		[None,None,None, True,False,False],
		[None,None,None, False,True,False],
		[None,None,None, False,False,True],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a,b,c,x;
dx
dx		a = $a;
dx		b = $b;
dx		c = $c;
dx
dx		if (a > b) { $t0 x = a; a = b; b = x; }
dx
dx		if (b > c) { $t1 x = b; b = c; c = x; }
dx
dx		if (a > b) { $t2 x = a; a = b; b = x; }
'''

argv_template = ''

stdin_template = ''
