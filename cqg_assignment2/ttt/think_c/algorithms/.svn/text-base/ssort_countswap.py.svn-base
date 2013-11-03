question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['ssort_countswap_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void selection_sort(int a[], int n)
dx	{
dx		int i,j,temp,swap_count;
dx		swap_count = 0;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = i + 1; j < n; j++) {
dx				if (a[i] > a[j]) {
dx					temp = a[i];
dx					a[i] = a[j];
dx					a[j] = temp;
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
dx		selection_sort(a,3);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
