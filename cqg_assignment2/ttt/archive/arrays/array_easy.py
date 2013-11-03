import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [ 
	['$x1','int'],['$x2','int'],['$x3','int'],
	['$y0','int'],
]

tuple_list = [
	['array_easy_',
		[0,None],
		[1,None],
		[2,None],
		[3,None],
		[4,None],
	]
]

global_code_template = '''\
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		int b[] = {1,2,3,4,5};
dx	
dx		printf("%d\\n",b[$x1]);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
