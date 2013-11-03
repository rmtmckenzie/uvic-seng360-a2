question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a','ascii_string'], ['$n','int'], ['$out','string'],
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

a_list = [
	[1.0], [1.0,2.0], [1.0,2.0,3.0],

	[2.0], [2.0,3.0], [1.3,2.2,3.5],

	[3.0], [2.3,3.6], [3.3,3.2,3.5],
]

group_list = [
	['array_sum_io_'] + 
		[ [ list_to_c_array(a), len(a), None] for a in a_list ],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	double sum(double a[], int n) {
dx		double s = 0.0;
dx
dx		for (int i = 0; i < n; i++) s = s + a[i];
dx		return s;
dx	}
'''

main_code_template = '''\
dx		double a[] = $a;
dx
dx		printf("%.2f\\n", sum(a, $n));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
