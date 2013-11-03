question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$i','int'],
	['$y0','int'], ['$y1','int'], ['$y2','int'],
	['$y3','int'], ['$y4','int'], ['$y5','int'],
]

group_list = [
	['array_indexing_io_',
		[1, None,None,None, None,None,None,],
		[3, None,None,None, None,None,None,],
		[5, None,None,None, None,None,None,],
		[7, None,None,None, None,None,None,],
		[9, None,None,None, None,None,None,],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int a[] = {2,3,4,1,6,5,0,8,9,7};
dx
dx		printf("%d\\n", a[$i]);
dx		printf("%d\\n", a[a[$i]]);
dx		printf("%d\\n", a[a[a[$i]]]);
dx
dx		int b[] = {6,3,0,1,2,5,4,9,7,8};
dx
dx		for (int i = 0; i < 3; i++)
dx			printf("%d\\n",b[a[i]]);
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
'''
