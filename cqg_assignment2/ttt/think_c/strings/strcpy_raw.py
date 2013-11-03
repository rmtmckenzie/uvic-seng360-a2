question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x1','string'],['$x2','int'],['$y0','string'],
]

group_list = [
	['strcpy_raw_io_',
		['abcde',0,None],
		['abcde',1,None],
		['abcde',2,None],
		['abcde',5,None],
		['abcde',9,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
'''

main_code_template = '''\
dx		char *a = "$x1";
dx		char s[10];
dx	
dx		strcpy(s,a);
dx		s[$x2] = '\\0';
dx		printf("%s\\n",s);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
