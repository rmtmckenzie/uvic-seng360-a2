import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [ 
	['$x1','int'],['$x2','int'],['$x3','int'],
	['$y0','int'],
]

tuple_list = [
	['array_lib_add_at_',
		[0,1,0,None],
		[0,1,1,None],
		[0,2,0,None],
		[0,2,1,None],
		[0,2,2,None],
		[0,4,0,None],
		[0,4,1,None],
		[0,4,2,None],
		[2,0,0,None],
		[2,1,0,None],
		[2,1,1,None],
		[2,2,0,None],
		[2,2,1,None],
		[2,2,2,None],
		[4,0,0,None],
	]
]

global_code_template = '''\
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void al_add_at(int a[],int n,int i,int x)
dx	{
dx		int j;
dx		for (j = n; j > i; --j)
dx			a[j] = a[j-1];
dx		a[i] = x;
dx		return;
dx	}
dx
dx	void al_remove_at(int a[],int n,int i)
dx	{
dx		for (; i < n-1; ++i)
dx			a[i] = a[i+1];
dx		return;
dx	}
dx
dx	int al_find(int a[],int n,int x)
dx	{
dx		int i;
dx		for (i = 0; i < n; ++i)
dx			if(a[i] == x)
dx				return i;
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int b[] = {1,3,5,7,9};
dx	
dx		al_add_at(b+$x1,$x2,$x3,99);
dx		printf("%d\\n",al_find(b,5,99));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
