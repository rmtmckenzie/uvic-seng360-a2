import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$x','int'], ['$operator','ascii_string'], ['$y','int'],
	['$out','string'],
]

x = range(-2,3)
# consider separate group for &&,||
operator = ['<','<=','==','!=','<=','<', '&&','||']
y = [-2,-1,1,2]

group_list = [
	['conditional_expression_io_'] + \
	 #[[1,'<',2,None]]
	 generate_util.cross_product_sublist([x,operator,y,None], range(3))
]

#DB print 'expected number of tuples:',len(x)*len(operator)*len(y)

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx
dx		printf("%s\\n", $x $operator $y ? "a" : "b");
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
