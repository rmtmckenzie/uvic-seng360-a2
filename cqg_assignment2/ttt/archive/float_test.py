import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$i1','int'],['$i2','int'],['$y0','float']
]

tuple_list = [
	['float_',	[1,2,None],	[4,9,None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int min(int a, int b) {
dx		if (a < b) {
dx			return a;
dx		} else {
dx			return b;
dx		}
dx	}
'''

main_code_template = '''\
dx		printf("%f\\n", 1.076);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
