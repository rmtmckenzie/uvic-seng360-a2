game_type = 'input_output'

parameter_list = [['$x1','string'], ['$y0','string']]

tuple_list = [
	['KnR_1-10_',[None,None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	#define MAXLINE 1000   /* maximum input line length */
dx	
dx	int max;                /* maximum length seen so far */
dx	char line[MAXLINE];     /* current input line */
dx	char longest[MAXLINE];  /* longest line saved here */
dx	
dx	int my_getline(void);
dx	void copy(void);
dx	
dx	/* my_getline: specialized version */
dx	int my_getline(void)
dx	{
dx		int c, i;
dx		extern char line[];
dx	
dx		for (i = 0; i < MAXLINE - 1
dx			&& (c=getchar()) != EOF && c != '\\n'; ++i)
dx			line[i] = c;
dx		if (c == '\\n') {
dx			line[i] = c;
dx			++i;
dx		}
dx		line[i] = '\\0';
dx		return i;
dx	}
dx	
dx	/* copy: specialized version */
dx	void copy(void)
dx	{
dx		int i;
dx		extern char line[], longest[];
dx	
dx		i = 0;
dx		while ((longest[i] = line[i]) != '\\0')
dx			++i;
dx	}
dx	
dx	/* print longest input line; specialized version */
'''

main_code_template = '''\
dx	int len;
dx	extern int max;
dx	extern char longest[];
dx	
dx	max = 0;
dx	while ((len = my_getline()) > 0)
dx		if (len > max) {
dx			max = len;
dx			copy();
dx		}
dx	if (max > 0)  /* there was a line */
dx		printf("%s", longest);
'''

argv_template = ''

stdin_template = '''
a
$x1
abc
'''

stdout_template = '''\
$y0
'''
