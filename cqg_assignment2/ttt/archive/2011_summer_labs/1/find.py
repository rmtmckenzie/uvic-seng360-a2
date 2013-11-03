game_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$lower','int'],['$upper','string'],
	['$b0','int'],['$b1','int'],['$b2','int'],['$b3','int'],['$b4','int'],
	['$x','int'],['$n','int'],
	['$o0','string'],
]

tuple_list = [
	['find_',
		# fault: $lower; player selects target
		[1,'n', 1,3,5,7,9, None,5, -1],

		# fault: $upper; player selects target
		[0,'n-1', 1,3,5,7,9, None,5, -1],

		# fault: $lower; player selects array
		[1,'n', None,3,None,7,None, 9,5, -1],
	]	
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
d	/* purpose
d	*	if x is present in a[0..n-1]
d	*		return i such that a[i] == x
d	*	else
d	*		return -1
d	* preconditions
d	*	n >= 0 and a[0..n-1] legally addressable
d	*/
dx	int find(int x,int a[],int n)
dx	{
dx		int i;
dx
dx		for (i = $lower; i < $upper; i++)
dx			if (x == a[i])
dx				return i;
dx
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int b[] = {$b0,$b1,$b2,$b3,$b4};
dx	
dx		printf("%d\\n",find($x,b,$n));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$o0
'''
