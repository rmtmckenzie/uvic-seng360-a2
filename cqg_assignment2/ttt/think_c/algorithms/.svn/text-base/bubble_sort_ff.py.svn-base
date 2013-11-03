question_type = 'find_the_failure'

source_language = 'C'

# NOTE: could make entire xX lines hot for multiple bugs in 1 template
hotspot_declarations = [
	['$a0','int'],['$a1','int'],['$a2','int'],['$a3','int'],
]

group_list = [
	['bubble_sort_ff_',
		[None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX
dxX	// Purpose: sort a[0..n-1] in place
dxX	// Preconditions: n > 0 and a[0..n-1] dereferenceable
dxX	void bubble_sort(int a[],int n)
dxX	{
dxX		int i,j,x;
dxX
dxX		for (i = 0; i < n-1; i++) {
x			for (j = 0; j < n-i-1; j++) {
dX			for (j = 1; j < n-i-1; j++) {
dxX				if (a[j] > a[j+1]) {
dxX					x = a[j]; a[j] = a[j+1]; a[j+1] = x;
dxX				}
dxX			}
dxX		} 
dxX	}
'''

main_code_template = '''\
dxX		int i;
dxX		int a[] = {$a0,$a1,$a2,$a3};
dxX
dxX		bubble_sort(a,4);        
dxX		for (i = 0; i < 4; i++)
dxX			printf("%d\\n",a[i]);
dxX
'''

argv_template = ''

stdin_template = ''
