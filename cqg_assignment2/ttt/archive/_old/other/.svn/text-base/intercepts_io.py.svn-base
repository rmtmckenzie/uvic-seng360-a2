import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$a','float'],['$b','float'],['$c','float'],['$x','float'],['$y','float']
]

tuple_list = [
	['intercept_io_f_',	
		[2.0,5.0,12.0,None,None],	
		[10.0,5.0,24.0,None,None],	
	],
	['intercept_io_b_',	
		[None,None,None,6,2.4],
		[None,None,None,2.4,4.8],
	]
]

global_code_template = '''\
d	// This program prompts the user for the equation of a line
d	// whose slop is non-zero, and calculates and prints the x
d	// and y intercepts
d	#include &lt;iostream>
x	#include <iostream>
dx	using namespace std;
'''

main_code_template = '''\
dx	double a, b, c, xintercept, yintercept;
dx	
dx	// Prompt for input
dx	cout << "Place equation in form ax + by = c\\n";
dx	cout << "Enter a, b and c:";
dx	cin >> a >> b >> c;
dx	
dx	// Calculate the x- and y-intercepts
dx	xintercept = c / a;
dx	yintercept = c / b;
dx	
dx	//Print results
dx	cout << "x-intercept = " << xintercept << endl;
dx	cout << "y-intercept = " << yintercept << endl;
dx	
'''

argv_template = ''

stdin_template = '''\
$a
$b
$c
'''

stdout_template = '''\
Place equation in form ax + by = c
Enter a, b and c:x-intercept = $x
y-intercept = $y
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
