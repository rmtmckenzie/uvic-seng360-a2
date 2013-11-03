game_type = 'input_output'

parameter_list = [ ['$i1','string'],['$y0','int'] ]

tuple_list = [
	['KnR_1-5-2a_',[None,4]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* count characters in input; 1st version */
'''

main_code_template = '''\
dx	long nc;
dx	
dx	nc = 0;
dx	while (getchar() != EOF)
dx		++nc;
dx	printf("%ld\\n", nc);
'''

argv_template = ''

stdin_template = '''\
$i1
b
'''


stdout_template = '''\
$y0
'''

