game_type = 'input_output'

parameter_list = [['$x1','int'], ['$y0','int'], ['$y1','int']]

tuple_list = [
	['KnR_1-8_',[None,-3,None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* power: raise base to n-th power; n >= 0; version 2 */
dx	int power(int base, int n)
dx	{
dx		int p;
dx	
dx		for (p = 1; n > 0; --n)
dx			p = p * base;
dx		return p;
dx	}
dx	
dx	/* test power function */
'''

main_code_template = '''\
dx	int i;
dx	
dx	for (i = 0; i < 3 ; ++i)
dx		printf("%d %d %d\\n", i, power(2,i), power($x1,i));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
0 1 1
1 2 $y0
2 4 $y1
'''
