question_type = 'find_the_failure'

source_language = 'C'

parameter_list = [
	['$correct','string'],
	['$incorrect','string'],
	['$search_value','int'],
]

forward_correct = "for (i = 0; i < n; i++)"
forward_left = "for (i = 1; i < n; i++)"
forward_right = "for (i = 0; i < n - 1; i++)"

backward_correct = "for (i = n - 1; i >= 0; i--)"
backward_left = "for (i = n - 2; i >= 0; i--)"
backward_right = "for (i = n - 1; i > 0; i--)"

tuple_list = [
	['for_ff_',
		[forward_correct,forward_left,None],
		[forward_correct,forward_right,None],
		[backward_correct,backward_left,None],
		[backward_correct,backward_right,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX
d	/*Purpose
d	*	if x is present in a[0..n-1]
d	*		return i such that a[i] == x
d	*	else
d	*		return -1
d	* Preconditions
d	*	n >= 0
d	*	a[0..n-1] is legally addressable
d	*/
dxX	int find(int x, int a[], int n)
dxX	{
dxX		int i;
dxX	
x		$correct
dX		$incorrect
dxX			if (x == a[i])
dxX				return i;
dxX	
dxX		return -1;
dxX	}
dxX
'''

main_code_template = '''\
dxX		int array[] = {1,2,3,4,5};
dxX		
dxX		printf("%d\\n", find($search_value,array,5));
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
