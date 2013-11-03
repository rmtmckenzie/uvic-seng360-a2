question_type = 'input_output'
source_language = 'C'

hotspot_declarations = [
	['$expr','ascii_string'],

	['$out00','string'],
	['$out01','string'],
	 ['$out02','string'], ['$out03','string'], ['$out04','string'],
]

inc_dec = ['--','--','++','++']

group_list = [
	['inc_dec_harder_io_a_'] +
		[ ['a[$i]'.replace('$i',s), None,None,None,None,None] \
			for s in ['i--','--i','++i','i++']],

	['inc_dec_harder_io_b_'] +
		[ ['a[$i]'.replace('$i',s), None,None,None,None,None] \
			for s in ['a[i]--','--a[i]','++a[i]','a[i]++']],

	['inc_dec_harder_io_c_'] + # pre-increment
		[ ['$i0a[$i1i]'.replace('$i0',i0).replace('$i1',i1),
			None,None,None,None,None] \
			for i0 in ['--','++'] for i1 in ['--','++']
		],

	['inc_dec_harder_io_d_'] + # post-increment
		[ ['a[i$i0]$i1'.replace('$i0',i0).replace('$i1',i1),
			None,None,None,None,None] \
			for i0 in ['--','++'] for i1 in ['--','++']
		],
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
'''

main_code_template = '''\
dx
dx		int a[] = {2,1,4,3,2,1,0};
dx		int i = 3;
dx	
dx		printf("%d\\n", $expr);
dx		printf("%d %d %d %d\\n", i, a[0],a[1],a[2]);
dx	
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out00
$out01 $out02 $out03 $out04
'''
