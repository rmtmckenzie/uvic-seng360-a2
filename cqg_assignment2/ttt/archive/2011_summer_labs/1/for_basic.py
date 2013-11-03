game_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$lower','int'],['$upper','int'],
	['$o0','string'],['$o1','string'],['$o2','string'],
	 ['$o3','string'],['$o4','string'],
	['$o5','string'],['$o6','string'],['$o7','string'],
	 ['$o8','string'],['$o9','string'],
]

tuple_list = [
	['for_basic_',
		# vary lower
		[0,5,None,None,None,None,None,None,None,None,None,None],
		[1,5,None,None,None,None,None,None,None,None,None,None],
		[2,5,None,None,None,None,None,None,None,None,None,None],
		[4,5,None,None,None,None,None,None,None,None,None,None],
		[5,5,None,None,None,None,None,None,None,None,None,None],
		# vary upper
		[0,0,None,None,None,None,None,None,None,None,None,None],
		[0,1,None,None,None,None,None,None,None,None,None,None],
		[0,2,None,None,None,None,None,None,None,None,None,None],
		[0,4,None,None,None,None,None,None,None,None,None,None],
		[0,5,None,None,None,None,None,None,None,None,None,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		int i;
dx
dx		for (i = $lower; i < $upper; i++) {
dx			printf("%d\\n",i);
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
