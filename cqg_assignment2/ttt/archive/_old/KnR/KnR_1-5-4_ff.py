game_type = 'find_the_failure'

parameter_list = [ ['$i1','string']]

tuple_list = [
	['KnR_1-5-4_ff_',[None] ]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX	
dxX	#define IN   1  /* inside a word */
dxX	#define OUT  0  /* outside a word */
dxX
dxX	/* count lines, words, and characters in input */
'''

main_code_template = '''\
dxX	int c, nl, nw, nc, state;
dxX	
dxX	state = OUT;
dxX	nl = nw = nc = 0;
dxX	while ((c = getchar()) != EOF) {
dxX		++nc;
dxX		if (c == '\\n')
dxX			++nl;
dxX		if (c == ' ' || c == '\\n' || c == '\\t')
dX			state = IN;
x			state = OUT;
dxX		else if (state == OUT) {
dxX			state = IN;
dxX			++nw;
dxX		}
dxX	}
dxX	printf("%d %d %d\\n", nl, nw, nc);
'''

argv_template = ''

stdin_template = '''\
$i1'''
