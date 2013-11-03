question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$x1','string'],['$y0','int'],
]

group_list = [
	['strlen_',
		['',None],	
		['a',None],
		['ab',None],
		['abc',None],
		['abcd',None],
		['ab'*2,None],
		['ab'*3,None],
		['ab'*4,None],
		['ab'*5,None],
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
