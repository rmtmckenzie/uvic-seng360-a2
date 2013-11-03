import question_template

game_type = 'find_the_failure'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int']
]

tuple_list = [
	['MVE_Fig310_',
		[2, None],
		[None, None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
xX	#include <stdio.h>
dxX	
'''

main_code_template = '''\
dxX	  printf("Input two positive integers:\\n");
dxX	  int p,q; scanf("%d %d", &p, &q);
dxX	  int x = p, y = q;
dxX	  // gcd(x,y) == gcd(p,q)
dX	  while (x < y) {
x	  while (x != y) {
dxX	    if (x < y)
dxX	      y = y-x;
dxX	    else if (y < x)
dxX	      x = x-y;
dxX	    // gcd(x,y) == gcd(p,q)
dxX	  }
dxX	  // x == y and gcd(x,y) == gcd(p,q)
dxX	  printf("The gcd is: %d\\n", x);
'''

argv_template = ''

stdin_template = '''\
$x1 $x2
'''

stdout_template = '''\
Input two positive integers:
The gcd is: $y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
