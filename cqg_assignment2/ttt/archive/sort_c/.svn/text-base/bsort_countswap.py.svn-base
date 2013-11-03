question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['bsort_countswap_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void bubble_sort(int a[], int n)
dx	{
dx		int i,j,temp,swap_count;
dx		swap_count = 0;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = n-1; j > i; j--) {
dx				if (a[j] < a[j-1]) {
dx					temp = a[j];
dx					a[j] = a[j-1];
dx					a[j-1] = temp;
dx					swap_count++;
dx				}
dx			}
dx		} 
dx		printf("%i\\n",swap_count);
dx	}
'''

main_code_template = '''\
dx		int a[3] = {1,2,3};
dx
dx		bubble_sort(a,3);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
