import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$div','int'],
	['$d0','string'],['$d1','string'],['$d2','string'],
		['$d3','string'],['$d4','string'],
	['$m0','string'],['$m1','string'],['$m2','string'],
		['$m3','string'],['$m4','string'],
]

group_list = [
	['div_mod_io_', 
		[1, None,None,None,None,None, None,None,None,None,None],
		[2, None,None,None,None,None, None,None,None,None,None],
		[3, None,None,None,None,None, None,None,None,None,None],
		[4, None,None,None,None,None, None,None,None,None,None],
		[5, None,None,None,None,None, None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		for (int n = 0; n < 5; n++) printf("%d ", n/$div);
dx		printf("\\n");
dx
dx		for (int n = 0; n < 5; n++) printf("%d ", n%$div);
dx		printf("\\n");
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$d0 $d1 $d2 $d3 $d4 
$m0 $m1 $m2 $m3 $m4 
'''
