import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int'],['$y0','int'],['$y1','int'],['$y2','int'],
	['$y3','int'],['$y4','int'],['$y5','int'],['$y6','int'],['$y7','int']
]

tuple_list = [
	['swap_cbv_',
		[3,2,3,2,None,None,2,None,None,None],
		[2,3,2,3,None,3,None,None,None,None],
		[3,None,None,5,None,None,None,None,None,None],
		[3,4,None,None,None,None,None,None,None,None],
		[None,None,None,None,2,None,None,4,None,None],
		[None,None,None,None,None,None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	// swap the values of x and y
dx	void swap(int x,int y) {
dx		int tmp;
dx
dx		tmp = x;
dx		x = y;
dx		printf("x:%d\\ty:%d\\n",x,y);
dx		y = tmp;
dx		printf("x:%d\\ty:%d\\n",x,y);
dx	}
'''

main_code_template = '''\
dx		int a,b;
dx	
dx		a = $x1;
dx		b = $x2;
dx	
dx		printf("a:%d\\tb:%d\\n",a,b);
dx		swap(a,b);
dx		printf("a:%d\\tb:%d\\n",a,b);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
a:$y0	b:$y1
x:$y2	y:$y3
x:$y4	y:$y5
a:$y6	b:$y7
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
