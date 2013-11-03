question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['selection_sort_io_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void selection_sort(int a[], int n)
dx	{
dx		int i,j,temp;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = i + 1; j < n; j++) {
dx				if (a[i] > a[j]) {
dx					temp = a[i];
dx					a[i] = a[j];
dx					a[j] = temp;
dx				}
dx			}
dx		}
dx	}
'''

main_code_template = '''\
dx		int i;
dx		int a[4] = {1,3,2,4};
dx
dx		selection_sort(a,4);        
dx		for (i = 0; i < 4; i++) {
dx			printf("%d",a[i]);
dx		}
dx		printf("\\n");
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
