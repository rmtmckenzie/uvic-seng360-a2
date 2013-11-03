question_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$stdin0','int'],['$stdin1','int'],['$stdout0','int']
]

tuple_list = [
	['min_io_forward_',	[1,2,None],	[4,9,None]],
	['min_io_backward_',	[None,None,1],	[None,None,6]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a,b;
dx		scanf("%d",&a);
dx		scanf("%d",&b);
dx		if (a < b)
dx			printf("Minimum: %d\\n", a);
dx		else
dx			printf("Minimum: %d\\n", b);
'''

argv_template = ''

stdin_template = '''
$stdin0
$stdin1
'''

stdout_template = '''\
Minimum: $stdout0
'''
