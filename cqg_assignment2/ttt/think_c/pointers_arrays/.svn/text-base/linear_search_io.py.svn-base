question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$x','int'], ['$a','ascii_string'], ['$n','int'],
	['$out','string'],
]

group_list = [
	['linear_search_io_'] +
		[ [x,'{1,2,3}',3,None] for x in range(5) ] +
		[ [x,'{6,4,2,0}',4,None] for x in range(8) ] +
		[ [x,'{6,4,2,4}',4,None] for x in range(8) ]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	int linear_search(int x, int a[], int n) {
dx		for (int i = 0; i < n; i++)
dx			if (x == a[i])
dx				return i;
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int a[] = $a;
dx
dx		printf("%d\\n", linear_search($x, a, $n));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
