question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$x','int'], ['$y','int'],
	['$out0','string'], ['$out1','string'],
	['$out2','string'], ['$out3','string'],
	['$out4','string'], ['$out5','string'],
]

group_list = [
	['jason_quiz0_io_'] +
		[ [x,y,None,None,None,None,None,None]
			for x in range(5) for y in range(5) ]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	void foo (int x, int *y)
dx	{
dx		x = x + 1;
dx		*y = *y + 1;
dx	}
dx	
dx	void bar (int *x, int y)
dx	{
dx		x = x + 1;
dx		y = y + 1;
dx	}
'''

main_code_template = '''\
dx		int x,y;
dx	
dx		x = $x;
dx		y = $y;
dx	
dx		printf ("x:%d\\ty:%d\\n", x, y);
dx		foo(x,&y);
dx		printf ("x:%d\\ty:%d\\n", x, y);
dx		bar(&x,y);
dx		printf ("x:%d\\ty:%d\\n", x, y);
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
x:$out0	y:$out1
x:$out2	y:$out3
x:$out4	y:$out5
'''
