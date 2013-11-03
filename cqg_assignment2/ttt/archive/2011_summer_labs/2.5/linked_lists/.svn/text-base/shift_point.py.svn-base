game_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$delta','int'],
	['$y0','string'],['$y1','string'],['$y2','string'],
	['$y3','string'],['$y4','string'],
]

tuple_list = [
	['shift_point_',	
		# base tuple
		# [0, 1,1,1,1,1],
		[0, None,None,None,None,None], # forward
		[None, 1,1,1,1,1], # backward
		[None, 1,1,1,1,None], # mixed

		# base tuple
		# [0, 1,1,1,0,0],
		[1, None,None,None,None,None], # forward
		[None, 1,1,1,0,0], # backward
		[None, 1,1,None,0,0], # mixed

		# base tuple
		# [0, 1,0,0,0,0],
		[2, None,None,None,None,None], # forward
		[None, 1,0,0,0,0], # backward
		[None, 1,None,0,0,0], # mixed
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	struct point {
dx		int x;
dx		int y;
dx	};
dx	
dx	void shiftpoint(struct point *p, int delta)
dx	{
dx		p->x += delta;
dx		p->y += delta;
dx	}
dx	
dx	int contains(struct point p, struct point p0, struct point p1)
dx	{
dx		if (p.x >=  p0.x && p.x <= p1.x && p.y >=  p0.y && p.y <= p1.y)
dx			return 1;
dx		else
dx			return 0;
dx	}
'''

main_code_template = '''\
dx		struct point a0 = {0,0};
dx		struct point a1 = {5,5};
dx		struct point a2 = {1,2};
dx		int i;
dx	
dx		for (i = 0; i < 5; i++) {
dx			shiftpoint(&a2,$delta);
dx			printf("%d\\n", contains(a2,a0,a1));
dx		}
dx
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
