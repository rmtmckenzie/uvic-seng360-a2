import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','string'],['$x2','string'],['$y0','string'],
]

tuple_list = [
	['strcmp_',
		['','abc',None],	
		['a','abc',None],	
		['ab','abc',None],	
		['abc','abc',None],	
		['1','345',None],	
		['2','345',None],	
		['3','345',None],	
		['4','345',None],	
		['5','345',None],	
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
dx
dx	char f(int n)
dx	{
dx		if (n < 0)
dx			return '-';
dx		else if (n == 0)
dx			return '0';
dx		else
dx			return '+';
dx	}
'''

main_code_template = '''\
dx		// Note: 'a' < 'b' < ... < 'z' and '0' < '1' < ... < '9'
dx	
dx		char *a = "$x1";
dx		char *b = "$x2";
dx		char n;
dx	
dx		n = strcmp(a,b);
dx		printf("%c\\n",f(n));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
