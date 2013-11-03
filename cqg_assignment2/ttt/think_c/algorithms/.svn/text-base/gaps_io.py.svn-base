question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a','ascii_string'],['$n','int'],
	['$y0','string'],['$y1','string'],['$y2','string'],['$y3','string'],
	['$y4','string'],
]

group_list = [
	['gaps_io_',
		['0',1, None,None,None,None,None],
		['1',1, None,None,None,None,None],
		['2',1, None,None,None,None,None],

		['0,1',2, None,None,None,None,None],
		['1,2',2, None,None,None,None,None],
		['2,4',2, None,None,None,None,None],

		['0,1,2',3, None,None,None,None,None],
		['1,3,5',3, None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int x = 0;
dx
dx	void gaps(int x[],int n)
dx	{
dx		int i=0, j=0;
dx		while (i < n) {
dx			if (j < x[i]) {
dx				printf("%d\\n",j);
dx			} else {
dx				i++;
dx			}
dx			j++;
dx		}
dx	}
'''

main_code_template = '''\
dx		int a[] = {$a};
dx
dx		gaps(a,$n);        
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
$y3
$y4
'''
