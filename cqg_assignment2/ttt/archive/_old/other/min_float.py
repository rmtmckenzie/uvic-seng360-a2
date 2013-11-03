import question_template

game_type = 'input_output'
source_language = 'C'

parameters = {
	'code': { },
	'stdin': {'$i1':'float', '$i2':'float'},
	'stdout': {'$y0':'float'},
}

tuple_list = [
	[ 	[],		['$i1','$i2'],		['$y0'] ],
	# [prefix,
	#       [[code_values],  [stdin_values],      [stdout_values]],
	#       ...
	# ]
	['min_float_', 
		[ [],		[1.3,2.6],			[None] ], 
		[ [],		[4.2,9.5],			[None] ],
	],
]

tuples = tuple_converter.convert_tuples(tuple_list)

global_code = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	float min(float a, float b) {
dx		if (a < b) {
dx			return a;
dx		} else {
dx			return b;
dx		}
dx	}
'''

main_code = '''\
dx	float a,b;
dx	scanf("%f",&a);
dx	scanf("%f",&b);
dx	printf("%.2f\\n", min(a,b));
'''

stdin_template = '''\
$i1
$i2
'''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
