game_type = 'input_output'

parameter_list = [
	['$y0','int'], ['$y1','int']
]

tuple_list = [
	[ 'KnR_1-2a_', [None,None]],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* printf Fahrenheit-Celsius table
dx	    for fahr = 0, 20, 40 */
'''

main_code_template = '''\
dx	int fahr, celsius;
dx	int lower, upper, step;
dx	
dx	lower = 0;      /* lower limit of temperature scale */
dx	upper = 40;     /* upper limit */
dx	step = 20;      /* step size */
dx	
dx	fahr = lower;
dx	while (fahr <= upper) {
dx		celsius = 5 * (fahr-32) / 9;
dx		printf("%d\\t%d\\n", fahr, celsius);
dx		fahr = fahr + step;
dx	}
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
0	-17
$y0	$y1
40	4
'''

