question_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int'],['$x3','int'],['$y0','int'],
]

tuple_list = [
	['find_',
		[7,None,None,1],
	]	
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int find(int x, int a[], int n)
dx	{
dx		int i;
dx
dx		for (i = 0; i < n; i++)
dx			if (x == a[i])
dx				return i;
dx
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int b[] = {1, 3, 5, 7, 9};
dx	
dx		int n = find($x1,b+$x2,$x3);
dx		printf("find returns: %d\\n",n);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
find returns: 1
'''
