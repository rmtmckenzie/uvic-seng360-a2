import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [ ['$i1','int'],['$y0','int'],['$x0','char*'] ]

tuple_list = [
	['min_io_forward_',	[1,None,None],	[4,None,None] ],
	['min_io_backward_',	[None,2,None],	[None,6,None] ],
	['min_io_mixed_',	[2,None,None],	[3,1,None] ],
	['min_io_open_',	[None,None,None]],
]


global_code = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int min(int a, int b) {
dx		if (a < b) {
dx			return a;
dx		} else {
dx			return b;
dx		}
dx	}
'''

main_code = '''\
dx	int a, b;
dx	scanf("%d", &a);
dx	b = atoi(argv[1])
dx	printf("argv[1] argv[2] %d\\n", min(a,b));
'''

argvs = '$x0'

stdin_template = '''\
$i1
'''

stdout_template = '''\
min number $y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
