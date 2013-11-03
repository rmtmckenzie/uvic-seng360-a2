game_type = 'input_output'

parameter_list = [
	['$y0','float'], ['$y1','float']
]

tuple_list = [
	[ 'KnR_1-2b_', [None,None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* print Fahrenheit-Celsius table
dx	    for fahr = 0, 20, 40; floating-point version */
'''

main_code_template = '''\
dx	float fahr, celsius;
dx	float lower, upper, step;
dx	
dx	lower = 0;      /* lower limit of temperature scale */
dx	upper = 40;     /* upper limit */
dx	step = 20;      /* step size */
dx	
dx	fahr = lower;
dx	while (fahr <= upper) {
dx		celsius = (5.0/9.0) * (fahr-32.0);
dx		printf("%3.0f %6.1f\\n", fahr, celsius);
dx		fahr = fahr + step;
dx	}
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
  0  -17.8
 $y0   $y1
 40    4.4
'''
