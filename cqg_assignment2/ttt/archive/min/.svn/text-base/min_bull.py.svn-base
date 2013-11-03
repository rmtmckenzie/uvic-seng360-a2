game_type = 'bullseye'
source_language = 'C'

parameter_list = [ 
 	['$t0','target'],['$t1','target'],['$x1','int'],['$x2','int'] 
]

tuple_list = [
	['min_bull_',
		[True,False,1,None],
		[True,False,None,None],
		[False,True,None,7]
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int min(int a, int b) {
dx		if (a < b) { 
dx			$t0
dx			return a;
dx		} else { 
dx			$t1
dx			return b;
dx		}
dx	}
'''

main_code_template = '''\
dx		min($x1, $x2);
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
