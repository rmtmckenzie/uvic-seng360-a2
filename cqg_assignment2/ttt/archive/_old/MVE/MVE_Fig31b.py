import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int'],
	['$y0','int'],['$y1','int'],['$y2','int'],['$y3','int'],['$y4','int'],
	['$y5','int'],['$y6','int'],['$y7','int'],['$y8','int'],
]

tuple_list = [
	['MVE_Fig31b_',
		[1,2,None,None,None,None,None,None,None,None,None],
		[None,None,1,2,1,2,2,1,2,1,1],
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
dx	  printf("x: %d;\\ty: %d;\\tz: %d\\n", x, y, z);
dx	  x = y;		   // Compute
dx	  printf("x: %d;\\ty: %d;\\tz: %d\\n", x, y, z);
dx	  y = z;		   // Compute
dx	  printf("x: %d;\\ty: %d;\\tz: %d\\n", x, y, z);
dx				   // Output
'''

argv_template = ''

stdin_template = '''\
$x1 $x2
'''
stdout_template = '''\
x: $y0;\ty: $y1;\tz: $y2
x: $y3;\ty: $y4;\tz: $y5
x: $y6;\ty: $y7;\tz: $y8
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
