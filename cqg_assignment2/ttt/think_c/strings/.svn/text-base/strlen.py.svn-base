question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x1','string'],['$y0','int'],
]

group_list = [
	['strlen_io_',
		['',None],	
		['a',None],
		['ab',None],
		['abc',None],
		['abcd',None],
	]
]


global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
'''

main_code_template = '''\
dx		printf("%d\\n",strlen("$x1"));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
