import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [ 
	['$x1','int'],['$x2','int'],['$y0','int'],
]

tuple_list = [
	['for_basic_',
		[0,1,None],
		[0,2,None],
		[0,3,None],
		[0,4,None],
		[0,5,None],
		[0,6,None],
		[1,6,None],
		[2,6,None],
		[3,6,None],
		[0,None,6],
		[0,None,10],
		[0,None,15],
		[None,None,15],
		[None,None,93],
		[None,None,None],	
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>	
x	#include <stdio.h>	
'''

main_code_template = '''\
dx		int s = $x1;
dx		int i;
dx		for (i = 1; i < $x2; i++) {
dx			s = s + i;
dx		}
dx		printf("%d\\n",s);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
