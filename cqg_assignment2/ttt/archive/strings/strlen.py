import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','string'],['$y0','int'],
]

tuple_list = [
	['strlen_',
		['',None],	
		['a',None],
		['ab',None],
		['abc',None],
		['abcd',None],
	]
]


global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
'''

main_code_template = '''\
dx		printf("%d\\n",strlen("$x1"));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
