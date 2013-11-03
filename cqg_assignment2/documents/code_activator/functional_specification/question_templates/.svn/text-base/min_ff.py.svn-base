game_type = 'find_the_failure'

source_language = 'C'

parameter_list = [ 
	['$x1','int'], ['$x2','int'] 
]

tuple_list = [
	['min_ff_',[None,None],[1,None],[None,7]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX
d	/*
d	purpose
d		return the smaller of a and b
d	precondition
d		none
d	examples
d		min(1,2) returns 1
d		min(1,1) returns 1
d		min(1,0) returns 0
d	*/
dxX	int min(int a, int b) {
dxX		if (a < b) {
dxX			return a;
dxX		} else {
dX			return a;
x			return b;
dXx		}
dXx	}
'''

main_code_template = '''\
dxX	printf ("%d\\n", min($x1, $x2));
'''

argv_template = ''

stdin_template = ''
