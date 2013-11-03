game_type = 'input_output'

parameter_list = [
	['$y0','int'], ['$y1','float']
]

tuple_list = [
	[ 'KnR_1-3_', [None,None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	/* print Fahrenheit-Celsius table */
'''

main_code_template = '''\
dx	int fahr;
dx	
dx	for (fahr = 0; fahr <= 40; fahr = fahr + 20)
dx		printf("%3d %6.1f\\n", fahr, (5.0/9.0)*(fahr-32));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
  0  -17.8
 20   -6.7
 $y0    $y1
'''

