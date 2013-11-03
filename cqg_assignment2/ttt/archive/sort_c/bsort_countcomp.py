question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['bsort_countcomp_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void bubble_sort(int a[], int n)
dx	{
dx		int i,j,temp,comparison_count;
dx		comparison_count = 0;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = n-1; j > i; j--) {
dx				comparison_count++;
dx				if (a[j] < a[j-1]) {
dx					temp = a[j];
dx					a[j] = a[j-1];
dx					a[j-1] = temp;
dx				}
dx			}
dx		} 
dx		printf("%i\\n",comparison_count);
dx	}
'''

main_code_template = '''\
dx		int a[2] = {1,3};
dx
dx		bubble_sort(a,2);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
