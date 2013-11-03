import generate_util

question_type = 'bullseye'
source_language = 'C'

hotspot_declarations = [
	['$w1','int'], ['$w2','int'], ['$w3','int'],
	['$w4','int'], ['$w5','int'], ['$w6','int'],
	['$w7','int'], ['$w8','int'], ['$w9','int'],

	['$t0','target'], ['$t1','target'], ['$t2','target'],
	['$t3','target'], ['$t4','target'], ['$t5','target'],
	['$t6','target'], ['$t7','target'], ['$t8','target'],
]

group_list = [
	# Note: for be, the inputs need NOT be all the same but one
	['counterfeit_coin_be_', 
		[None,1,1, None,1,2, 1,1,2,
		False,False,True, False,False,False, False,False,False],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx		int w1,w2,w3,w4,w5,w6,w7,w8,w9;
dx
dx		w1 = $w1;
dx		w2 = $w2;
dx		w3 = $w3;
dx		w4 = $w4;
dx		w5 = $w5;
dx		w6 = $w6;
dx		w7 = $w7;
dx		w8 = $w8;
dx		w9 = $w9;
dx
dx		if ((w1+w2+w3) < (w4+w5+w6)) {
dx			// w1 or w2 or w3
dx			if (w1 < w2) { $t0 printf("one"); }
dx			else if (w1 > w2) { $t1 printf("two"); }
dx			else { $t2 printf("three"); }
dx		} else if ((w1+w2+w3) > (w4+w5+w6)) {
dx			// w4 or w5 or w6
dx			if (w4 < w5) { $t3 printf("four"); }
dx			else if (w4 > w5) { $t4 printf("five"); }
dx			else { $t5 printf("six"); }
dx		} else {
dx			// w7 or w8 or w9
dx			if (w7 < w8) { $t6 printf("seven"); }
dx			else if (w7 > w8) { $t7 printf("eight"); }
dx			else { $t8 printf("nine"); }
dx		}
dx		printf("\\n");
'''

argv_template = ''

stdin_template = ''
