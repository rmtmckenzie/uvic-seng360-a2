game_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$x','int'],
	['$o0','string'],['$o1','string'],['$o2','string'],
	 ['$o3','string'],['$o4','string'],
	['$o5','string'],['$o6','string'],['$o7','string'],
	 ['$o8','string'],['$o9','string'],
]

tuple_list = [
	['three_x_forward_',
		[1,None,None,None,None,None,None,None,None,None,None],
		[2,None,None,None,None,None,None,None,None,None,None],
		[4,None,None,None,None,None,None,None,None,None,None],
		[5,None,None,None,None,None,None,None,None,None,None],
		[3,None,None,None,None,None,None,None,None,None,None],
		[6,None,None,None,None,None,None,None,None,None,None],
		[8,None,None,None,None,None,None,None,None,None,None],
		[10,None,None,None,None,None,None,None,None,None,None],
		[16,None,None,None,None,None,None,None,None,None,None],
	],
	['three_x_backward_',
		[None,None,None,None,None,None,None,None,None,None,None],
		[None,2,None,None,None,None,None,None,None,None,None],
		[None,16,None,None,None,None,None,None,None,None,None],
		[None,5,None,None,None,None,None,None,None,None,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
'''

main_code_template = '''\
dx		int x;
dx
dx		x = $x;
dx		while (x > 1) {
dx			printf("%d\\n",x);
dx			if (x%2 == 1)
dx				x = 3*x + 1;
dx			else
dx				x = x/2;
dx		}
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$o0
$o1
$o2
$o3
$o4
$o5
$o6
$o7
$o8
$o9
'''
