game_type = 'input_output'

parameter_list = [['$x1','string'], ['$y0','string']]

tuple_list = [
	['KnR_1-9_',[None,None]]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	#define MAXLINE 1000   /* maximum input line length */
dx	
dx	int my_getline(char line[], int maxline);
dx	void copy(char to[], char from[]);
dx	
dx	/* my_getline:  read a line into s, return length  */
dx	int my_getline(char s[],int lim)
dx	{
dx		int c, i;
dx	
dx		for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\\n'; ++i)
dx			s[i] = c;
dx		if (c == '\\n') {
dx			s[i] = c;
dx			++i;
dx		}
dx		s[i] = '\\0';
dx		return i;
dx	}
dx	
dx	/* copy:  copy 'from' into 'to'; assume to is big enough */
dx	void copy(char to[], char from[])
dx	{
dx		int i;
dx	
dx		i = 0;
dx		while ((to[i] = from[i]) != '\\0')
dx			++i;
dx	}
dx	
dx	/* print the longest input line */
'''

main_code_template = '''\
dx	int len;            /* current line length */
dx	int max;            /* maximum length seen so far */
dx	char line[MAXLINE];    /* current input line */
dx	char longest[MAXLINE]; /* longest line saved here */
dx	
dx	max = 0;
dx	while ((len = my_getline(line, MAXLINE)) > 0)
dx		if (len > max) {
dx			max = len;
dx			copy(longest, line);
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
