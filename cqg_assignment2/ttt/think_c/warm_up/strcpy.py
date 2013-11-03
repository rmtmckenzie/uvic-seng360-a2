question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x1','string'],['$x2','string'],['$y0','string'],['$y1','string'],
]

group_list = [
	['strcpy_',
		['','xyz',None,None],
		['a','xyz',None,None],
		['ab','xyz',None,None],
		['abc','xyz',None,None],
		['abc','',None,None],
		['abc','x',None,None],
		['abc','xy',None,None],
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
dx		strcpy(s,a);
dx		printf("%s\\n",s);
dx	
dx		strcpy(s,b);
dx		printf("%s\\n",s);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
'''
