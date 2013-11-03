question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$n','int'], ['$b','int'],
	['$out0','string'], ['$out1','string'], ['$out2','string'],
	['$out3','string'], ['$out4','string'],
]

group_list = [
	['base_conversion_io_',
		[15,2,None,None,None,None,None],
		[15,8,None,None,None,None,None],
		[15,10,None,None,None,None,None],
		[15,16,None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	// Purpose: write to stdout the b-base digits of the numeral representing n.
dx	// Preconditions: n > 0 and b > 2
dx
'''

main_code_template = '''\
dx		int n,b;
dx	
dx		n = $n;
dx		b = $b;
dx		while (n != 0) { printf("%d\\n", n%b); n = n/b; }
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out0
$out1
$out2
$out3
$out4
'''
