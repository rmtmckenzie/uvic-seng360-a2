import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x0','int'],['$x1','int'],['$x2','int'],['$y0','int'],['$y1','int']
]

tuple_list = [
	['for_break_continue_forward_',	
		[0,5,5,None,None],	
		[0,7,4,None,None],	
		[0,3,4,None,None],	
		[1,5,4,None,None],	
		[1,7,4,None,None],	
		[2,6,6,None,None],	
		[3,5,4,None,None],	
		[4,3,5,None,None],	
		[5,5,4,None,None]	
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx	int s = $x0;
dx	int i;
dx	for (i = 1; i < $x1; i++) {
dx		if (i % 2 == 0)
dx			s++;
dx		if (i % 3 == 0)
dx			continue;
dx		if (i % $x2 == 0)
dx			break;
dx		s = s + i;
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
