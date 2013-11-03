question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$y','int'],
	['$out','string']
]

group_list = [
	['leap_year_function_io_',
		# [2014,0],
		[2014,None], [None,365], [None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
d	<a href="static/leap_year_function.html">int is_leap_year(int y)</a>
x	int is_leap_year(int y) {
dx		if ((y%400) == 0) return 1;
dx		else // not a leap-century year
dx		if ((y%100) == 0) return 0;
dx		else // Julian calendar applies
dx		if ((y%4) == 0) return 1;
dx		else return 0;
dx	}
'''

main_code_template = '''\
dx		int y;
dx	
dx		printf("%d\\n",is_leap_year($y));
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
