import question_template

import question_template

game_type = 'liar_liar'
source_language = 'C'

parameter_list = [
	['$t0','assert'],['$t1','assert'],
	['$x1','int'],['$x2','int'],['$x3','int'],['$x4','int'],['$x5','int'],
	['$x6','int'],['$x7','int'],
]

tuple_list = [
	['MVE_Fig91b_',
		['c == 1','',1,None,None,1,1,1,1],
		['','c == 1',None,1,None,1,1,1,1],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	int digit( int a, int b, int c, int d, int e, int f, int g) {
dx	  if (a) {
dx	    if (b) { 
dx	      $t0
dx	      if (c) {
dx	        if (d) {
dx	          if (e) {
dx	            if (f)
dx	              if (g) {
dx	                return 8;
dx	              } else return 0;
dx	          } else { /* a b c d !e */
dx	              if (f) return -1;
dx	              else if (g) return 3;
dx	                   else {
dx	                     return -1;
dx	                   }
dx	          }
dx	        } else /* a b c !d */
dx	            if (e) return -1;
dx	            else
dx	              if (f) return 9;
dx	              else return 7;
dx	      } else /* a b !c */
dx	          return 2;
dx	    } else /* a !b */
dx	        if (c) return 5;
dx	        else return -1;
dx	  } else /* !a */
dx	      if (b) {
dx		$t1
dx	        if (c)
dx	          if (d) return -1;
dx	          else
dx	            if (e) return -1;
dx	            else
dx	              if (f) return 4;
dx	              else return 1;
dx	      } else /* !a !b */
dx	          return 6;
dx	}		
'''

main_code_template = '''\
dx	  int a,b,c,d,e,f,g;
dx	  scanf("%d %d %d %d %d %d %d", &a, &b, &c, &d, &e, &f, &g);
dx	  digit(a, b, c, d, e, f, g);
'''

argv_template = ''

stdin_template = '''\
$x1 $x2 $x3 $x4 $x5 $x6 $x7
'''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
