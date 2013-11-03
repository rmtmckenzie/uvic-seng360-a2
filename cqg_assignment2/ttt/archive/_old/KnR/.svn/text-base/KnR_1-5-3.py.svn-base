game_type = 'input_output'

parameter_list = [ ['$y0','int'] ]

tuple_list = [
	['KnR_1-5-3_',[None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* count lines in input */
'''

main_code_template = '''\
dx	int c, nl;
dx	
dx	nl = 0;
dx	while ((c = getchar()) != EOF)
dx		if (c == '\\n')
dx			++nl;
dx	printf("%d\\n", nl);
'''

argv_template = ''

stdin_template = '''\
a
b
'''


stdout_template = '''\
$y0
'''

