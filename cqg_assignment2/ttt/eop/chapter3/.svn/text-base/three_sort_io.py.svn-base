import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$a','int'], ['$b','int'], ['$c','int'],
	['$out0','string'], ['$out1','string'], ['$out2','string'],
	['$out3','string'], ['$out4','string'], ['$out5','string'],
	['$out6','string'], ['$out7','string'], ['$out8','string'],
]

group_list = [
	['three_sort_io_',
		[1,2,3, None,None,None, None,None,None, None,None,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

# for future use:
specification = '''\
d
d	// Purpose:
d	//	read 3 integer values from stdin and
d	//	write them to stdout, in increasing order
d	// Preconditions: the 3 integers are in [-1000..1000]
'''

main_code_template = '''\
dx		int a,b,c;
dx
dx		a = $a;
dx		b = $b;
dx		c = $c;
dx
dx		int x;
dx		if (a > b) { x = a; a = b; b = x; }
dx		printf("%d %d %d\\n",a,b,c);
dx
dx		if (b > c) { x = b; b = c; c = x; }
dx		printf("%d %d %d\\n",a,b,c);
dx
dx		if (a > b) { x = a; a = b; b = x; }
dx		printf("%d %d %d\\n",a,b,c);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out0 $out1 $out2
$out3 $out4 $out5
$out6 $out7 $out8
'''
