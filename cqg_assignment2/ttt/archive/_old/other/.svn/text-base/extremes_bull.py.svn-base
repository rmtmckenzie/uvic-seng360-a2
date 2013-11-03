import question_template

game_type = 'bullseye'
source_language = 'C'

parameter_list = [
	['$i1','int'],['$i2','int'],['$i3','int'],\
	['$t0','target'],['$t1','target'],['$t2','target'],['$t3','target']
]

tuple_list = [
	['extremes_bull_',	
		[None,None,None,True,False,False,False],	
		[None,None,None,False,True,False,False],	
		[None,None,None,False,False,True,False],	
		[None,None,None,False,False,False,True]	
	]
]

global_code_template = '''\
d	#include &lt;iostream>
x	#include <iostream>
dx	using namespace std;
dx
d	// This program prompts the user for three integers
d	// and calculates and prints the largest and smallest
dx	void getExtremes(int x, int y, int z, int &lge, int &sml)
dx	{
dx		lge = x;
dx		sml = x;
dx		if (y > lge) { $t0
dx			lge = y;
dx		} else if (y < sml) { $t1
dx			sml = y;
dx		}
dx		if (z > lge) { $t2
dx			lge = z;
dx		} else if (z < sml) { $t3
dx			sml = z;
dx		}
dx	}	
'''

main_code_template = '''\
dx	int x1, x2, x3, large, small;
dx	cout << "Enter three integers:";
dx	cin >> x1 >> x2 >> x3;
dx	getExtremes(x1,x2,x3,large,small);
dx	cout << "The largest integer is " << large << endl
dx		<< "The smallest integer is " << small << endl;
'''

argv_template = ''

stdin_template = '''\
$i1 $i2 $i3
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
