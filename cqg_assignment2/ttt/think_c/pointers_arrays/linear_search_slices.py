question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x1','int'],['$x2','int'],['$x3','int'],['$y0','int'],
]

group_list = [
	['linear_search_slices_io_',
		[1,0,0,None],
		[1,0,2,None],
		[1,0,5,None],
		[1,2,0,None],
		[1,2,1,None],
		[1,2,3,None],
		[1,4,0,None],
		[1,4,1,None],
		[5,0,0,None],
		[5,0,2,None],
		[5,0,5,None],
		[5,2,0,None],
		[5,2,1,None],
		[5,2,3,None],
		[5,4,0,None],
		[5,4,1,None],
		[9,0,0,None],
		[9,0,2,None],
		[9,0,5,None],
		[9,2,0,None],
		[9,2,1,None],
		[9,2,3,None],
		[9,4,0,None],
		[9,4,1,None],
	]	
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int find(int x,int a[],int n)
dx	{
dx		int i;
dx
dx		for (i = 0; i < n; i++) {
dx			if (x == a[i])
dx				return i;
dx		}
dx
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int b[] = {1,3,5,7,9};
dx	
dx		printf("%d\\n",find($x1,b+$x2,$x3));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
