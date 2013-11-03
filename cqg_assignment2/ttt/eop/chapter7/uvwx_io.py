import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$u','int'], ['$v','int'], ['$w','int'], ['$x','int'],
	['$out','string'],
]

u = [-2,-1,1,2]
v = [-2,-1,1,2]
w = [-2,-1,1,2]
x = range(-2,3)
print 'expected number of tuples',len(u)*len(v)*len(w)*len(x)


group_list = [
	# EoP example
	['uvwx_io_eop_'] + [[1,-2,3,-4,None]],

	['uvwx_io_b_'] + \
	 generate_util.cross_product_sublist([u,v,w,x,None], range(4))
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx
dx		int u,v,w,x;
dx		u = $u;
dx		v = $v;
dx		w = $w;
dx		x = $x;
dx		printf("%d\\n", u/w*-u + v/u + v-x- -x/v);
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
