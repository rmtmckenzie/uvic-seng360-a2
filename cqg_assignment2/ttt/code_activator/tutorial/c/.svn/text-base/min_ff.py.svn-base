question_type = 'find_the_failure'

source_language = 'C'

hotspot_declarations = [ 
	['$x1','int'], ['$x2','int'] 
]

group_list = [
	['min_ff_',[1,None],[None,None],[None,7]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX	
'''

main_code_template = '''\
dxX		int a,b;
dxX		a = $x1;
dxX		b = $x2;
d		// print the smaller of a and b
dxX		if (a < b)
dxX			printf("%d\\n", a);
dxX		else
dX			printf("%d\\n", a);
x			printf("%d\\n", b);
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
