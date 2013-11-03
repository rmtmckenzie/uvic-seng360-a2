game_type = 'liar_liar'

source_language = 'C'

parameter_list = [
	['$t0','assert'],['$t1','assert'],['$x1','int'],['$x2','int']
]

tuple_list = [
	['min_liar_liar_',
		['a > 5','',None,None],
		['a > 5','b < 6',None,None],
		['','b < 6',None,7],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;assert.h>
dx
dx	int min(int a,int b) {
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
dx	min($x1,$x2);
'''

argv_template = ''

stdin_template = ''
