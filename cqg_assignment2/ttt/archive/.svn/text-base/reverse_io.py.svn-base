import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [ 
	['$x1','int'],['$y0','string'],
]

tuple_list = [
	['reverse_io_forward_',
		[0,None],
		[1,None],
		[2,None],
		[3,None],
		[4,None],
	],
	['reverse_io_backward_',
		[None,'edcba'],
		[None,'aedcb'],
		[None,'abedc'],
		[None,'abced'],
		[None,'abcde'],
	]

]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
dx
dx	void r(char s[])
dx	{
dx		int c,i,j;
dx
dx		for (i = 0,j = strlen(s)-1; i < j; i++,j--) {
dx			c = s[i];
dx			s[i] = s[j];
dx			s[j] = c;
dx		}
dx	}
'''

main_code_template = '''\
dx		char s[10] = "abcde";
dx	
dx		r(s+$x1);
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
