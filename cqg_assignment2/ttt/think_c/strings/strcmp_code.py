question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [ 
	['$x1','string'],['$x2','string'],['$y0','int'],
]

group_list = [
	['strcmp_code_io_',	
		['','abc',None],	
		['a','abc',None],	
		['ab','abc',None],	
		['abc','abc',None],	
		['abc','a',None],	
		['abc','ab',None],	
		['abc','abd',None],	
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
dx	int strcmp_0(char *s0, char *s1) {
dx		int i;
dx
dx		for (i = 0; s0[i] == s1[i]; i++)
dx			if (s0[i] == '\\0')
dx				return 0;
dx		return s0[i] - s1[i];
dx	}
'''

main_code_template = '''\
dx		// Note ASCII values:
dx		//      'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101
dx	
dx		char *a = "$x1";
dx		char *b = "$x2";
dx	
dx		printf("%d\\n",strcmp_0(a,b));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
