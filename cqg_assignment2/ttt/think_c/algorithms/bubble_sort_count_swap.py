question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a0','int'],['$a1','int'],['$a2','int'],
	['$y','int']
]

group_list = [
	['bubble_sort_count_swap_',
		[3,1,2, None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int k = 0;
dx	void bubble_sort(int a[], int n)
dx	{
dx		int i,j,x;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = n-1; j > i; j--) {
dx				if (a[j] < a[j-1]) {
dx					x = a[j]; a[j] = a[j-1]; a[j-1] = x;
dx					k++;
dx				}
dx			}
dx		} 
dx	}
'''

main_code_template = '''\
dx		int a[] = {$a0,$a1,$a2};
dx		bubble_sort(a,3);        
dx		printf("%i\\n",k);
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
