question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$y0','string'],
	['$y1','string'],
	['$y2','string'],
]

tuple_list = [
	['bsort_track_',
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
dx	void bubble_sort(int a[], int n)
dx	{
dx		int i,j,temp;
dx
dx		for (i = 0; i < n-1; i++) {
dx			printf("%i\\n",find(a,n,2));
dx			for (j = n-1; j > i; j--) {
dx				if (a[j] < a[j-1]) {
dx					temp = a[j];
dx					a[j] = a[j-1];
dx					a[j-1] = temp;
dx				}
dx			}
dx		} 
dx	}
'''

main_code_template = '''\
dx		int a[3] = {3,2,4};
dx
dx		bubble_sort(a,3);        
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''

