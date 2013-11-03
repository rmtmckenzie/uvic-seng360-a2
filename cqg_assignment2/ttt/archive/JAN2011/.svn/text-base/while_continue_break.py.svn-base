import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x0','int'],['$x1','int'],['$x2','int'],['$x3','int'],
	['$y0','int'],['$y1','int']
]

tuple_list = [
	['while_break_forward_',	
		[0,8,5,3,None,None],	
		[0,8,3,2,None,None],	
		[1,3,2,4,None,None],	
		[1,3,2,1,None,None],	
		[2,7,4,3,None,None],	
		[2,5,3,3,None,None],	
		[5,5,4,2,None,None],	
		[9,5,4,2,None,None],	
		[13,6,2,1,None,None],	
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx	int s = $x0;
dx	int i = 0;
dx	while (i < $x1) {
dx		if (s > 10)
dx			break;
dx		if (i % $x2 == 0) {
dx			s = s + i;
dx			i++;
dx		} else {
dx			i = i + $x3;
dx		}
dx	}
dx	printf("%d\\n",s);
dx	printf("%d\\n",i);
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
