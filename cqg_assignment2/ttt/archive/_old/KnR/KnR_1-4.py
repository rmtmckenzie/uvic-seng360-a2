game_type = 'input_output'

parameter_list = [ ['$y0','float'], ['$y1','float'] ]

tuple_list = [
	[ 'KnR_1-4_',[None,None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	#define LOWER	0      /* lower limit of temperature scale */
dx	#define UPPER	40     /* upper limit */
dx	#define STEP	20     /* step size */
dx	
dx	/* print Fahrenheit-Celcius table */	
'''

main_code_template = '''\
dx	int fahr;
dx	
dx	for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
dx		printf("%3d %6.1f\\n", fahr, (5.0/9.0)*(fahr-32));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
  0  -17.8
 $y0   $y1
 40    4.4
'''

