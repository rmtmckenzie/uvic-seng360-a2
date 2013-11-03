question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$day','int'],['$month','int'], ['$year','int'],
	['$out','string'],
]

group_list = [
	['ordinal_day_io_',
		[1,1,2000,None],
		[1,2,2000,None],
		[1,3,2000,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
d	<a href="static/leap_year_function.html">int is_leap_year(int y);</a>
x	int is_leap_year(int y) {
x		if ((y%400) == 0) return 1;
x		else // not a leap-century year
x		if ((y%100) == 0) return 0;
x		else // Julian calendar applies
x		if ((y%4) == 0) return 1;
x		else return 0;
x	}
dx
dx	// Purpose: return ordinal day of date given in the arguments
dx	// Preconditions: day_in_month > 0; month in 1..12.
dx	int ordinal_day(int day_in_month, int month, int year) {
dx		int a[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
dx		int day_number = day_in_month;
dx	
dx		for(int i = 1; i <= month ; i++)
dx			day_number = day_number + a[i-1];
dx		if (is_leap_year(year) && month > 2)
dx			day_number++;
dx	
dx		return day_number ;
dx	}
'''

main_code_template = '''\
dx
dx		printf("%d\\n",ordinal_day($day,$month,$year));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
