import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],
]

tuple_list = [
	['MVE_Fig31a_',
		[1,2,None,None,None],
		[None,None,2,1,1],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx	  int x,y,z;		   // Configure
dx	  scanf("%d %d", &x, &y);  //Initialize
dx	  z = x;		   // Compute
dx	  x = y;		   // Compute
dx	  y = z;		   // Compute
dx	  printf("x: %d; y: %d; z: %d\\n", x, y, z);
dx				   // Output
'''

argv_template = ''

stdin_template = '''\
$x1 $x2
'''
stdout_template = '''\
x: $y0; y: $y1; z: $y2
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
