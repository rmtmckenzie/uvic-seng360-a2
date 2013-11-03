game_type = 'input_output'

source_language = 'C'

parameter_list = [ 
	['$x1','int'],['$x2','int'],['$x3','int'],
	['$y0','int'],['$y1','int'],['$y2','int']
]

# needs work:
tuple_list = [
	['add_at_',
		[0,1,0,None,None,None],
		[0,1,1,None,None,None],
		[0,2,0,None,None,None],
		[0,2,1,None,None,None],
		[0,2,2,None,None,None],
		[0,4,0,None,None,None],
		[0,4,1,None,None,None],
		[0,4,2,None,None,None],
		[2,0,0,None,None,None],
		[2,1,0,None,None,None],
		[2,1,1,None,None,None],
		[2,2,0,None,None,None],
		[2,2,1,None,None,None],
		[2,2,2,None,None,None],
		[4,0,0,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void add_at(int a[],int n,int i,int x)
dx	{
dx		int j;
dx		for (j = n; j > i; --j)
dx			a[j] = a[j-1];
dx		a[i] = x;
dx		return;
dx	}
'''

main_code_template = '''\
dx		int b[6];
dx		int i;
dx		for (i = 0; i < 6; i++)
dx			b[i] = 2*i+1;
dx	
dx		add_at(b+$x1,$x2,$x3,99);
dx
dx		printf("%d %d %d\\n",b[0],b[3],b[5]);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0 $y1 $y2
'''
