question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$n','int'],
	['$s','string'], ['$m','string'], ['$h','string'],
	['$d','string'], ['$w','string'],
]

group_list = [
	['time_period_io_',
		[59, None,None,None,None,None],
		[61, None,None,None,None,None],
		[1000, None,None,None,None,None],
		[100000, None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx		// Purpose: write to stdout w, d, h, m, s such that
dx		// (1) n seconds is equivalent to w weeks, d days, h hours,
dx		// m minutes, and s seconds and
dx		// (2) d < 7, h < 24, m < 60, and s < 60.
dx		// Precondition: n is nonnegative.
dx	
dx		int n = $n;
dx
dx		printf("%d second(s)\\n",n%60);
dx
dx		n = n/60;
dx		printf("%d minute(s)\\n",n%60);
dx
dx		n = n/60;
dx		printf("%d hour(s)\\n",n%24);
dx
dx		n = n/24;
dx		printf("%d day(s)\\n",n%7);
dx
dx		n = n/7;
dx		printf("%d week(s)\\n",n);
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$s second(s)
$m minute(s)
$h hour(s)
$d day(s)
$w week(s)
'''
