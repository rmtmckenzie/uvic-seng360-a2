import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$i1','int'],['$i2','int'],['$y0','int']
]

#get tuple_list
execfile('min_io_test/tuples.py')


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
dx		printf("%d\\n", min($i1,$i2));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
