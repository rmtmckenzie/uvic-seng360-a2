question_type = 'bullseye'
source_language = 'C'

hotspot_declarations = [ 
 	['$t0','target'],['$t1','target'],['$x1','int'],['$x2','int'] 
]

group_list = [
	['min_be_',
		[True,False,1,None],
		[True,False,None,None],
		[False,True,None,7]
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a,b;
dx		a = $x1;
dx		b = $x2;
dx		if (a < b) {
dx			$t0
dx			printf("%d\\n", a);
dx		} else {
dx			$t1
dx			printf("%d\\n", b);
dx		}
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
