game_type = 'liar_liar'

parameter_list = [['$t0','assert'], ['$i1','string']]

tuple_list = [
	['KnR_1-5-4_liar_liar_',['nc < 3',None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	#define IN   1  /* inside a word */
dx	#define OUT  0  /* outside a word */
dx	
dx	/* count lines, words, and characters in input */
'''

main_code_template = '''\
dx	int c, nl, nw, nc, state;
dx	
dx	state = OUT;
dx	nl = nw = nc = 0;
dx	while ((c = getchar()) != EOF) {
dx		++nc;
dx		if (c == '\\n')
dx			++nl;
dx		if (c == ' ' || c == '\\n' || c == '\\t')
dx			state = OUT;
dx		else if (state == OUT) {
dx			$t0
dx			state = IN;
dx			++nw;
dx		}
dx	}
dx	printf("%d %d %d\\n", nl, nw, nc);
'''

argv_template = ''

stdin_template = '''\
$i1bc'''


