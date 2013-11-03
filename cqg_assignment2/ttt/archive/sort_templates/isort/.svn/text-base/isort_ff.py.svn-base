import question_template

game_type = 'find_the_failure'
source_language = 'C'

parameter_list = [
	['$x1','int'],
	['$x2','int'],
	['$x3','int'],
]

tuple_list = [
	['isort_ff_',
		[None,None,None]
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX
dxX	void insertion_sort(int a[], int n)
dxX	{
dxX		int i,j,temp;
dxX
dX		for (i = 2; i < n; i++) {
x		for (i = 1; i < n; i++) {
dxX			j = i;
dxX			while (j > 0 && a[j-1] > a[j]) {
dxX				temp = a[j];
dxX				a[j] = a[j-1];
dxX				a[j-1] = temp;
dxX				j--;
dxX			}
dxX		}
dxX	}
'''

main_code_template = '''\
dxX		int a[3] = {$x1,$x2,$x3};
xX		int i;
dxX
dxX		insertion_sort(a,3);        
xX		for (i = 0; i < 3; i++) {
xX			printf("%d",a[i]);
xX		}
'''

argv_template = ''

stdin_template = ''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
