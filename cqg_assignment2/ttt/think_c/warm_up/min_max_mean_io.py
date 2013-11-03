import generate_util

question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$a_value','ascii_string'], ['$a_length','int'],
	['$out0','string'],['$out1','string'],['$out2','string'],
]

'''
purpose:
	convert L to a string containing a C array initializer
preconditions:
	L is a non-empty list of int
'''
def list_to_c_array(L):
	s = str(L[0])
	for n in L[1:]:
		s += ',' + str(n)
	return '{' + s + '}'

a_list = [ range(1), range(3), range(5), [2,4,2,4], [1]*5, [1,2]*2]
group_list = [
	['min_max_mean_io_'] + 
		[ [list_to_c_array(L),len(L),None,None,None] for L in a_list ],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a[] = $a_value;
dx		int A_LENGTH = $a_length;
dx		int min,max,sum;
dx
dx		min = a[0]; max = a[0]; sum = a[0];
dx
dx		for (int i = 1; i < A_LENGTH; i++) {
dx			if (a[i] < min) {
dx				min = a[i];
dx			} else if (a[i] > max) {
dx				max = a[i];
dx			}
dx			sum = sum + a[i];
dx		}
dx
dx		printf("min: %d\\n", min);
dx		printf("max: %d\\n", max);
dx		printf("mean: %.2f\\n", sum/(float)A_LENGTH);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
min: $out0
max: $out1
mean: $out2
'''
