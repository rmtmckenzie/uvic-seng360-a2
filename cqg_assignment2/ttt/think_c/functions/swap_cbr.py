question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$x1','int'],['$x2','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],['$y3','int'],['$y4','int'],
	['$y5','int'],['$y6','int'],['$y7','int']
]

group_list = [
	['swap_cbr_io_',
		[1,2,1,2,None,None,None,None,None,None],
		[9,1,9,1,None,1,1,None,None,None],
		[2,None,None,None,3,None,None,None,None,None],
		[None,3,None,None,None,3,None,2,None,None],
		[None,None,None,None,2,2,None,4,None,None],
		[None,None,None,None,None,None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void swap(int *x,int *y) {
dx		int tmp;
dx
dx		tmp = *x;
dx		*x = *y;
dx		printf("x:%d\\ty:%d\\n",*x,*y);
dx		*y = tmp;
dx		printf("x:%d\\ty:%d\\n",*x,*y);
dx	}
'''

main_code_template = '''\
dx		int a,b;
dx	
dx		a = $x1;
dx		b = $x2;
dx	
dx		printf("a:%d\\tb:%d\\n",a,b);
dx		swap(&a,&b);
dx		printf("a:%d\\tb:%d\\n",a,b);
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
a:$y0	b:$y1
x:$y2	y:$y3
x:$y4	y:$y5
a:$y6	b:$y7
'''
