question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$y0','string'],
	['$y1','string'],
	['$y2','string'],
	['$y3','string'],
	['$y4','string'],
]

group_list = [
	['q_5_', [None,None,None,None,None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
dx	
'''

main_code_template = '''\
dx		printf("Welcome to CSC 111\\n"); 
dx		printf("Knowledge is Power\\n"); 
dx		printf("Develop a passion for learning.\\n"); 
dx		printf("If you do, "); 
dx		printf("you will never cease to grow.\\n"); 
dx		return EXIT_SUCCESS; 
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
$y3
$y4
'''
