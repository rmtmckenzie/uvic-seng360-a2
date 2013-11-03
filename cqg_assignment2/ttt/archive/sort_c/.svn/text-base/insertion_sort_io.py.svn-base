question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['insertion_sort_io_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void insertion_sort(int a[], int n)
dx	{
dx		int i,j,temp;
dx
dx		for (i = 1; i < n; i++) {
dx			j = i;
dx			while (j > 0 && a[j-1] > a[j]) {
dx				temp = a[j];
dx				a[j] = a[j-1];
dx				a[j-1] = temp;
dx				j--;
dx			}
dx		}
dx	}
'''

main_code_template = '''\
dx		int i;
dx		int a[4] = {1,3,2,4};
dx
dx		insertion_sort(a,4);        
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
