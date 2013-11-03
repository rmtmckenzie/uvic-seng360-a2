import sys
import generate_util

'''
----- safety proof
all questions safe
'''

question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$b','float'],['$e','int'],['$y','string'],
]

group_list = [
	['power_function_io_'] +
		[[b,e,None] for b in [1.0,1.1,1.414] for e in range(4)],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	float power(float b,int e)
dx	{
dx		float r;
dx
dx		r = 1.0;
dx		for (int i = 0; i < e; i++)
dx			r = r * b;
dx		return r;
dx	}
'''

main_code_template = '''\
dx		float r;
dx
dx		r = power($b,$e);
dx		printf("%.2f\\n",r);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y
'''
