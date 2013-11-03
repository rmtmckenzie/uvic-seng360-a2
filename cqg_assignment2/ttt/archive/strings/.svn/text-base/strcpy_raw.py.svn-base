import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','string'],['$x2','int'],['$y0','string'],
]

tuple_list = [
	['strcpy_raw_',
		['abcde',0,'$y0'],
		['abcde',1,'$y0'],
		['abcde',2,'$y0'],
		['abcde',5,'$y0'],
		['abcde',9,'$y0'],
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

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
