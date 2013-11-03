question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$i1','int'],['$i2','int'],['$y0','int']
]

group_list = [
	['min_io_forward_'] +	
		[[a,b,None] for a in range(5) for b in range(5)],
	['min_io_backward_',	[None,None,1],	[None,None,6]],
	['min_io_mixed_',	[None,2,None],	[3,None,1]],
	['min_io_open_',	[None,None,None]],
]
#print group_list

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a,b;
dx		a = $i1;
dx		b = $i2;
dx		if (a < b)
dx			printf("%d\\n", a);
dx		else
dx			printf("%d\\n", b);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
