question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$y0','string'],
	['$y1','string'],
	['$y2','string'],
	['$y3','string'],
]

group_list = [
	['q_15_', [None,None,None,None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
dx	
dx	void printText (void) { 
dx		printf ("UVic's 50th Anniversary\\n"); 
dx	} /*printText*/ 
dx
dx	void printNLines (int n) { 
dx		int k; 
dx		for (k=1; k<=n; k++); 
dx	} /*printNLines*/ 
dx	
'''

main_code_template = '''\
dx		printNLines(4); 
dx		printNLines(21); 
dx		return EXIT_SUCCESS; 
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
$y3
'''
