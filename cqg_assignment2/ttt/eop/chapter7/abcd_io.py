import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$a','int'], ['$b','int'], ['$c','int'], ['$d','int'],
	['$out','string'],
]

a = range(-2,3)
b = range(-2,3)
c = [-2,-1,1,2]
d = range(-2,3)
# print 'expected number of tuples',len(a)*len(b)*len(c)*len(d)

group_list = [
	['abcd_io_'] + \
	 generate_util.cross_product_sublist([a,b,c,d,None], range(4))
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx
dx		printf("%d\\n", $a + (($b/$c) - $d));
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
