question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$b','float'], ['$e','int'],
	['$out','string'],
]

group_list = [
	['extreme_compounding_io_',
		[2.0, 1, None],
		[2.0, 2, None],
		[2.0, 3, None],
		[1.414, 2, None],
		[1.732, 2, None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	double power(double b, int e) {
dx		double p = 1.0;
dx		for (int i = 0; i < e; i++) p = p*b;
dx		return p;
dx	}
dx
'''

RFU = '''
dx	// Purpose: return b to the power e
dx	// Precondition: b > 1 and e > 0
'''

main_code_template = '''\
dx	
dx		printf("%.2f\\n",power($b,$e));
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
