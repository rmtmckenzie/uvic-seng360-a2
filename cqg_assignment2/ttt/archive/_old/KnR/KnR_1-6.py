game_type = 'input_output'

parameter_list = [['$x1','string']]

tuple_list = [
	['KnR_1-6_',[None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* count digits, white space, others */
'''

main_code_template = '''\
dx	int c, i, nwhite, nother;
dx	int ndigit[10];
dx	
dx	nwhite = nother = 0;
dx	for (i = 0; i < 10; ++i)
dx		ndigit[i] = 0;
dx	
dx	while ((c = getchar()) != EOF)
dx		if (c >= '0' && c <= '9')
dx			++ndigit[c-'0'];
dx		else if (c == ' ' || c == '\\n' || c == '\\t')
dx			++nwhite;
dx		else
dx			++nother;
dx	
dx	printf("digits =");
dx	for (i = 0; i < 10; ++i)
dx		printf(" %d", ndigit[i]);
dx	printf(", white space = %d, other = %d\\n",
dx		nwhite, nother);
'''

argv_template = ''

stdin_template = '''\
$x1 1 2 3 4'''

stdout_template = '''\
digits = 1 1 1 1 1 0 0 0 0 0, white space = 4, other = 0
'''
