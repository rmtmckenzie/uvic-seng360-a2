question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a','ascii_string'],['$n','int'],['$i','int'],
	['$y0','string'],['$y1','string'],['$y2','string'],['$y3','string'],
	['$y4','string'],
]

'''
GENERATION PLAN
	apply cross product: {$a} X {$i}
		put $a's with same length in same group
	$a: '1', '1,2','2,1', '1,2,3','2,1,3'
		or any 3 unequal ints
		consider: duplicates
	$n: generate from $a; count commas plus one?
		comma_count = lambda s: len(filter(lambda c: c == ',',s))
		length of filter on ','?
	$i: range($n)
	$yN: None
		perhaps generalize in the future
example: ['3,2,1',3, 0, None,None,None,None,None],
a3 = ['1,2,3', '3,2,1']
hotspot_value_list = [
	[a3,3,range(3), None,None,None,None,None],
]

# o:number of operators, b:hotspot value number, c:cross product number
group_name = 'bubble_sort_value_at_o2_b%i_c%i_'

group_list = generate_util.generate_group_cross_product \
 (hotspot_value_list,group_name,input_list,input_indexes,operator_indexes)
'''
group_list = [
	['bubble_sort_value_at_',
		# suggest: cross-product on $a, $i
		['1,2,3',3, 0, None,None,None,None,None],
		['1,3,2',3, 0, None,None,None,None,None],
		['2,1,3',3, 0, None,None,None,None,None],
		['2,3,1',3, 0, None,None,None,None,None],
		['3,1,2',3, 0, None,None,None,None,None],
		['3,2,1',3, 0, None,None,None,None,None],

		['1,2,3',3, 2, None,None,None,None,None],
		['1,3,2',3, 2, None,None,None,None,None],
		['2,1,3',3, 2, None,None,None,None,None],
		['2,3,1',3, 2, None,None,None,None,None],
		['3,1,2',3, 2, None,None,None,None,None],
		['3,2,1',3, 2, None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	void bubble_sort(int a[], int n)
dx	{
dx		int i,j,x;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = 0; j < n-i-1; j++) {
dx				if (a[j] > a[j+1]) {
dx					x = a[j]; a[j] = a[j+1]; a[j+1] = x;
dx					printf("%d\\n",a[$i]);
dx				}
dx			}
dx		} 
dx	}
'''

main_code_template = '''\
dx		int a[] = {$a};
dx		bubble_sort(a,$n);        
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
$y3
$y4
'''
