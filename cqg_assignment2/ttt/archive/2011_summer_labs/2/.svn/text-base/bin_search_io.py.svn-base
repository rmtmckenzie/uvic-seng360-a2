game_type = 'input_output'

source_language = 'C'

parameter_list = [ 
	['$x1','int'],['$x2','int'],['$x3','int'],['$y0','int'],
]

tuple_list = [
	['bin_search_io_',
		[5,0,5,None],
		[3,0,5,None],
		[9,1,4,None],
		[7,1,4,None],
		[9,2,1,None],
		[2,0,5,None],
		[None,None,5,2],
		[None,None,None,1],
		[None,None,None,2],
		[None,None,None,3],
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	int binsearch(int x, int v[], int n) 
dx	{
dx		int low, high, mid, count;
dx		
dx		count = 0;
dx		low = 0;
dx		high = n - 1;
dx		while (low <= high) {
dx			count++;
dx			mid = (low+high) / 2;
dx			if (x < v[mid]) { 
dx				high = mid - 1;
dx			}
dx			else if (x > v[mid]) {
dx				low = mid + 1;
dx			}
dx			else {
dx				printf("%d\\n",count);
dx				return mid;
dx			}
dx		}
dx		printf("%d\\n",count);
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int a[] = {1, 3, 5, 7, 9};
dx	
dx		binsearch($x1, a+$x2, $x3);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
