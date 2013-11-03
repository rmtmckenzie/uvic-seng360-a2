question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$expr','ascii_string'],
	['$out0','string'], ['$out1','string'], ['$out2','string'],
]

group_list = [
	['inc_dec_easy_io_',
	 ['--i',None,None,None], ['i--',None,None,None],
	 ['++i',None,None,None], ['i++',None,None,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx
dx		int i = 0;
dx
dx		printf("%d\\n", i);
dx		printf("%d\\n", $expr);
dx		printf("%d\\n", i);
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out0
$out1
$out2
'''
