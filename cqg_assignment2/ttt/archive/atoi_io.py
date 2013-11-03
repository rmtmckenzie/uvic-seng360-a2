import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$i1','string'],['$y0','int']
]

tuple_list = [
	['atoi_io_',
		['1a',None],
		['+1a',None],
		['-1a',None],
		['a1',None],
		['a1a',None],
		['a2a',None],
		['11a',None],
		['a21a',None],
		['a-1a',None],
		['11a1a',None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;ctype.h>
x	#include <ctype.h>
dx
dx	// atoi:  convert s to integer
dx	int atoi(char s[])
dx	{
dx		int i,n,sign;
dx
dx		for (i = 0; isspace(s[i]); i++)  // skip white space
dx			;
dx		sign = (s[i] == '-') ? -1 : 1;
dx		if (s[i] == '+' || s[i] == '-')  // skip sign
dx			i++;
dx		for (n = 0; isdigit(s[i]); i++)
dx			n = 10*n+(s[i]-'0');
dx		return sign*n;
dx	}
'''

main_code_template = '''\
dx		printf("%d\\n", atoi("$i1"));
'''

argv_template = ''

stdin_template = '''\
'''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
