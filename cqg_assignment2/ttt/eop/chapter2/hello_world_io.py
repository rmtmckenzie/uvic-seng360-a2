question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$s','string'],['$out','string']
]

group_list = [
	['hello_world_io_forward_',
		['hello world',None],
		['bonjour monde',None],
		['ni hao shi jie',None],
		['hey duniya',None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		printf("$s\\n");
'''
#x		printf("%s\\n",$s);

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
