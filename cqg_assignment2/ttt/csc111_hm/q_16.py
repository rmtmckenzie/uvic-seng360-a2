question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$y0','string'],
]

group_list = [
	['q_16_', [None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
dx	
dx	void f5(void) { printf("desire "); } 
dx	void f7(void) { printf("to "); } 
dx	void f1(void) { printf("learn something useful\\n"); } 
dx	void f3(void) { printf("always "); } 
dx	
'''

main_code_template = '''\
dx		f3(); f5(); f7(); f1(); 
dx		return EXIT_SUCCESS; 
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
