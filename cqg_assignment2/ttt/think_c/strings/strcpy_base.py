question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x1','string'],['$x2','string'],['$x3','int'],['$x4','int'],
	['$y0','string'],['$y1','string'],
]

group_list = [
	['strcpy_base_io_',
		['abcde','vwxyz',0,0,None,None],
		['abcde','vwxyz',0,1,None,None],
		['abcde','vwxyz',1,0,None,None],
		['abcde','vwxyz',1,1,None,None],
		['abcde','vwxyz',2,3,None,None],
		['abcde','vwxyz',3,2,None,None],
		['abcde','vwxyz',4,0,None,None],
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
dx		char *b = "$x2";
dx		char s[10];
dx	
dx		strcpy(s,a+$x3);
dx		printf("%s\\n",s);
dx	
dx		strcpy(s+$x4,b);
dx		printf("%s\\n",s);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
'''
