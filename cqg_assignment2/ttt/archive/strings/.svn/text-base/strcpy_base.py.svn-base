import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','string'],['$x2','string'],['$x3','int'],['$x4','int'],
	['$y0','string'],['$y1','string'],
]

tuple_list = [
	['strcpy_base_',
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

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
