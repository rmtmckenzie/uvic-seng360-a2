import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [ 
	['$x0','string'],['$x1','string'],['$x2','string'],
	['$y0','string'],['$y1','string'],['$y2','string'] 
]

tuple_list = [
	['echo_io_forward_',['a','b','c',None,None,None]],
]


global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx	int i;
dx	
dx	for (i = 1; i < argc; i++)
dx		printf("%s\\n", argv[i]);
'''

argv_template = '$x0 $x1 $x2'

stdin_template = '''\
'''

stdout_template = '''\
$y0
$y1
$y2
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
