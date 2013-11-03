question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$amount','int'],
	['$y0','string'], ['$y1','string'], ['$y2','string'],
]

group_list = [
	['making_change_io_',
		[5,None,None,None],
		[15,None,None,None],
		[35,None,None,None],
		[125,None,None,None],
		[10,None,None,None],
	],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
dx	
'''

RFU = '''
dx	// Purpose: write to stdout the numbers of quarters, dimes, and nickels
dx	// whose total is equivalent to amount, minimizing the total number of coins.
dx	// Precondition: amount is a positive multiple of 5.
'''

main_code_template = '''\
dx	
dx		int n, nq = 0, nd = 0, nn = 0;
dx		n = $amount;
dx	
dx		while (n >= 25) {n = n-25; nq++;}
dx		while (n >= 10) {n = n-10; nd++;}
dx		while (n >= 5) {n = n-5; nn++;}
dx	
dx		printf("quarters: %d\\n", nq);
dx		printf("dimes: %d\\n", nd);
dx		printf("nickels: %d\\n", nn);
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
quarters: $y0
dimes: $y1
nickels: $y2
'''
