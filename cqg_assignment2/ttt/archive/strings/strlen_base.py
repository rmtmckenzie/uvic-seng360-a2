import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','string'],['$x2','int'],['$y0','string'],
]

tuple_list = [
	['strlen_base_',
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
dx		char *s = "$x1";
dx	
dx		printf("%d\\n",strlen(s + $x2));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
