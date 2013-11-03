game_type = 'input_output'

parameter_list = [ ['$i1','string'],['$y0','string'] ]

tuple_list = [
	['KnR_1-5-1a_',['abc',None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx	int c;
dx	
dx	c = getchar();
dx	while (c != EOF) {
dx		putchar(c);
dx		c = getchar();
dx	}
'''

argv_template = ''

stdin_template = '''\
$i1
'''

stdout_template = '''\
$y0
'''

