question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a','int'],['$b','int'],['$out','string']
]

group_list = [
	['compare_io_',	[1,2,None], [2,1,None], [1,1,None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a,b;
dx
dx		a = $a;
dx		b = $b;
dx		if (a < b)
dx			printf("first smaller\\n");
dx		if (a > b)
dx			printf("first larger\\n");
dx		if (a == b)
dx			printf("equal\\n");
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
