question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$p','int'],['$q','int'],
	['$y0','string'],['$y1','string'],['$y2','string'],['$y3','string'],
	['$y4','string'],['$y5','string'],['$y6','string'],['$y7','string'],
]

group_list = [
	['euclid_io_',
		[2,5, None,None,None,None, None,None,None,None],
		[34,26, None,None,None,None, None,None,None,None],
		[26,34, None,None,None,None, None,None,None,None],
		[1,1, None,None,None,None, None,None,None,None],
		[2,2, None,None,None,None, None,None,None,None],
		[2,4, None,None,None,None, None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	int gcd(int x,int y)
dx	{
dx		while (x != y) {
dx			printf("%d %d\\n",x,y);
dx			if (x < y) y = y-x;
dx			else x = x-y;
dx		}
dx		return x;
dx	}
'''

main_code_template = '''\

dx		int g;
dx		
dx		g = gcd($p,$q);        
dx		printf("%d\\n",g);
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
$y5
$y6
$y7
'''
