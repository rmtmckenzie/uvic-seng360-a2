question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string'],
	['$y1','string'],
	['$y2','string'],
]

tuple_list = [
	['isort_track_',
		[None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int find(int haystack[], int n, int needle) {
dx		int i;
dx		for (i = 0; i < n; i++)
dx			if (haystack[i] == needle)
dx				return i;
dx	}
dx
dx	void insertion_sort(int a[], int n)
dx	{
dx		int i,j,temp;
dx
dx		for (i = 1; i < n; i++) {
dx			j = i;
dx			printf("%i\\n",find(a,n,2));
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
dx		int a[3] = {4,3,2};
dx
dx		insertion_sort(a,3);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
