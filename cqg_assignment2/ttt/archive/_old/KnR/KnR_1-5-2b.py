game_type = 'input_output'

parameter_list = [ ['$i1','string'],['$y0','int'] ]

tuple_list = [
	['KnR_1-5-2b_',[None,4]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* count characters in input; 2nd version */
'''

main_code_template = '''\
dx	double nc;
dx	
dx	for (nc = 0; getchar() != EOF; ++nc)
dx		;
dx	printf("%.0f\\n", nc);
'''

argv_template = ''

stdin_template = '''\
$i1
b
'''

stdout_template = '''\
$y0
'''

