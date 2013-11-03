question_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$lower','int'],['$upper','int'],['$mod_a','int'],
	['$break_continue_a','string'],
	['$o0','string'],
	['$o1','string'],
	['$o2','string'],
	['$o3','string'],
	['$o4','string'],
]

tuple_list = [
	['while_break_forward_io_',
		# vary $lower
		[0,5,2,'break',None,None,None,None,None],
		[1,5,2,'break',None,None,None,None,None],
		[5,5,2,'break',None,None,None,None,None],
		# vary $upper
		[0,0,2,'break',None,None,None,None,None],
		[0,1,2,'break',None,None,None,None,None],
		[0,5,2,'break',None,None,None,None,None],
		# vary $mod
		[0,5,1,'break',None,None,None,None,None],
		[0,5,3,'break',None,None,None,None,None],
	],
	['while_continue_forward_io_',
		# cut-and-pasted from above:
		# vary $lower
		[0,5,2,'continue',None,None,None,None,None],
		[1,5,2,'continue',None,None,None,None,None],
		[5,5,2,'continue',None,None,None,None,None],
		# vary $upper
		[0,0,2,'continue',None,None,None,None,None],
		[0,1,2,'continue',None,None,None,None,None],
		[0,5,2,'continue',None,None,None,None,None],
		# vary $mod
		[0,5,1,'continue',None,None,None,None,None],
		[0,5,3,'continue',None,None,None,None,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
'''

main_code_template = '''\
dx		int i;
dx
dx		i = $lower;
dx		while (i < $upper) {
dx			if (i % $mod_a == 0 && i > 0) {
dx				i++;
dx				$break_continue_a;
dx			}
dx			printf("%d\\n",i);
dx			i++;
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
'''
