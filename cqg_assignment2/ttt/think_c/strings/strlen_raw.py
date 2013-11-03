question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x1','string'],['$x2','int'],['$y0','string'],
]

group_list = [
	['strlen_raw_io_',
		['abcd',0,None],	
		['abcd',1,None],	
		['abcd',2,None],	
		['abcd',3,None],	
		['abcd',4,None],	
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
'''

main_code_template = '''\
dx		char s[10];
dx	
dx		strcpy(s,"$x1");
dx		s[$x2] = '\\0';
dx		printf("%d\\n",strlen(s));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
