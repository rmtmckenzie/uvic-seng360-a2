question_type = 'find_the_failure'
source_language = 'C'

parameter_list = [
	['$x1','int'],
	['$x2','int'],
	['$x3','int'],
]

tuple_list = [
	['bsort_ff_',
		[None,None,None]
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX
dxX	void bubble_sort(int a[], int n)
dxX	{
dxX		int i,j,temp;
dxX
dX		for (i = 0; i < n-2; i++) {
x		for (i = 0; i < n-1; i++) {
dxX			for (j = n-1; j > i; j--) {
dxX				if (a[j] < a[j-1]) {
dxX					temp = a[j];
dxX					a[j] = a[j-1];
dxX					a[j-1] = temp;
dxX				}
dxX			}
dxX		} 
dxX	}
'''

main_code_template = '''\
dxX		int a[3] = {$x1,$x2,$x3};
xX		int i;
dxX
dxX		bubble_sort(a,3);        
xX		for (i = 0; i < 3; i++) {
xX			printf("%d",a[i]);
xX		}
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
