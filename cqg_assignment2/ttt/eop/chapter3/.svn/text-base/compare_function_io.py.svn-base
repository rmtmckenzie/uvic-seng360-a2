question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a','int'],['$b','int'],['$out','string']
]

group_list = [
	['compare_function_io_', [1,2,None], [2,1,None], [1,1,None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	int int_compare(int a, int b) {
dx		if (a < b) return -1;
dx		if (a > b) return 1;
dx		return 0;
dx	}
'''

main_code_template = '''\
dx
dx		printf("%d\\n", int_compare($a, $b));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
