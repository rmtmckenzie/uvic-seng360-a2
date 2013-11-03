question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$x','int'],['$y','int'],

	['$out0','string'],['$out1','string'],['$out2','string'],
	['$out3','string'],['$out4','string'],['$out5','string'],
	['$out6','string'],['$out7','string'],['$out8','string'],
]

group_list = [
	['swap_io_',
		[1,2, None,None,None, None,None,None, None,None,None],
		[2,1, None,None,None, None,None,None, None,None,None],
		[None,None, None,None,None, None,None,None, None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		int x,y,z;
dx	
dx		x = $x;
dx		y = $y;
dx	
dx		z = x;
dx		printf("x:%d\\ty:%d\\tz:%d\\n",x,y,z);
dx		x = y;
dx		printf("x:%d\\ty:%d\\tz:%d\\n",x,y,z);
dx		y = z;
dx		printf("x:%d\\ty:%d\\tz:%d\\n",x,y,z);
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
x:$out0	y:$out1	z:$out2
x:$out3	y:$out4	z:$out5
x:$out6	y:$out7	z:$out8
'''
