game_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$i1','int'],['$i2','int'],['$y0','int']
]

tuple_list = [
	['min_io_forward_',	[1,2,None],	[4,9,None]],
	['min_io_backward_',	[None,None,2],	[None,None,6]],
	['min_io_mixed_',	[None,2,None],	[3,None,1]],
	['min_io_open_',	[None,None,None]],
]

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
dx	int a, b;
dx	scanf("%d", &a);
dx	scanf("%d", &b);
dx	printf("%d\\n", min(a,b));
'''

argv_template = ''

stdin_template = '''\
$i1
$i2
'''

stdout_template = '''\
$y0
'''
