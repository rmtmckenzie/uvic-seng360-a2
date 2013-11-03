game_type = 'input_output'

parameter_list = [ ['$i1','string'],['$y0','string'] ]

tuple_list = [
	['KnR_1-5-1b_',['abc',None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx	int c;
dx	
dx	while ((c = getchar()) != EOF)
dx		putchar(c);
'''

argv_template = ''

stdin_template = '''\
$i1
'''

stdout_template = '''\
$y0
'''
