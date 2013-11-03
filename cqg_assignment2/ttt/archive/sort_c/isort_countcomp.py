question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string']
]

tuple_list = [
	['isort_countcomp_',
		[None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void insertion_sort(int a[], int n)
dx	{
dx		int i,j,temp,comparison_count;
dx		comparison_count = 0;
dx
dx		for (i = 1; i < n; i++) {
dx			j = i;
dx			while (j > 0 && a[j-1] > a[j]) {
dx				comparison_count++;
dx				temp = a[j];
dx				a[j] = a[j-1];
dx				a[j-1] = temp;
dx				j--;
dx			}
dx		}
dx		printf("%i\\n",comparison_count);
dx	}
'''

main_code_template = '''\
dx		int a[3] = {1,3,2};
dx
dx		insertion_sort(a,3);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

