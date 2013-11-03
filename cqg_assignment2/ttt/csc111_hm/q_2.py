question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$y0','string']
]

group_list = [
	['q_2_', [None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
dx	
'''

main_code_template = '''\
dx		int k; 
dx		for (k=1; k<=5; k++) { 
dx			printf("%d ", k); 
dx		} /*for*/ 
dx		return EXIT_SUCCESS; 
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
