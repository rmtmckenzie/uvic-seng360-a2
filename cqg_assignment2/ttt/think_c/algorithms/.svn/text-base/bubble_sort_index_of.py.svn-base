question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$a','ascii_string'],['$n','int'],['$x','int'],
	['$y0','string'],['$y1','string'],['$y2','string'],['$y3','string'],
	['$y4','string'],
]

'''
generation plan
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
'''
group_list = [
	['bubble_sort_index_of_',
		['1,2,3',3, 3, None,None,None,None,None],
		['1,3,2',3, 3, None,None,None,None,None],
		['2,1,3',3, 3, None,None,None,None,None],
		['2,3,1',3, 3, None,None,None,None,None],
		['3,1,2',3, 3, None,None,None,None,None],
		['3,2,1',3, 3, None,None,None,None,None],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	// Purpose: return the index of x in a[0..n-1]
dx	// Preconditions:
dx	//   n > 0 and a[0..n-1] dereferenceable
dx	//   x occurs exactly once in a[0..n-1]
dx	int find(int a[],int n,int x) {
x		int i;
x		for (i = 0; i < n; i++)
x			if (a[i] == x)
x				return i;
x	}
dx	
dx	void bubble_sort(int a[],int n)
dx	{
dx		int i,j,x;
dx
dx		for (i = 0; i < n-1; i++) {
dx			for (j = 0; j < n-i-1; j++) {
dx				if (a[j] > a[j+1]) {
dx					x = a[j]; a[j] = a[j+1]; a[j+1] = x;
dx					printf("%d\\n",find(a,n,$x));
dx				}
dx			}
dx		} 
dx	}
'''

main_code_template = '''\
dx		int a[] = {$a};
dx
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
