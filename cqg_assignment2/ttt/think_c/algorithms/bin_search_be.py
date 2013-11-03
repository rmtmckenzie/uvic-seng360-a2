question_type = 'bullseye'

source_language = 'C'

hotspot_declarations = [ 
	['$t0','target'],['$t1','target'],['$t2','target'],['$t3','target'],
	['$x1','int'],['$x2','int'] 
]

group_list = [
['bin_search_be',
	[True,True,False,False,None,None],
	[True,False,True,False,None,None],
	[False,True,True,False,None,None],
	[False,False,True,False,None,None],
	[False,True,False,False,None,None],
	[True,False,False,True,None,None],
	[False,True,False,True,None,None],
	[False,False,True,True,None,None],
	[False,True,False,False,-1,None],
	[True,False,False,False,999,None],
 ]
]

global_code_template = '''\
dx	int binsearch(int x, int v[], int n) 
dx	{
dx		int low, high, mid;
dx		
dx		low = 0;
dx		high = n - 1;
dx		while (low <= high) {
dx			mid = (low+high) / 2;
dx			if (x < v[mid]) { $t0
dx				high = mid - 1;
dx			}
dx			else if (x > v[mid]) { $t1
dx				low = mid + 1;
dx			}
dx			else {	$t2
dx				return mid;
dx			}
dx		} $t3
dx		return -1;
dx	}
'''

main_code_template = '''\
dx		int a[] = {1, 3, 5, 7, 9};
dx	
dx		binsearch($x1, a, 5);
dx		binsearch($x2, a, 5);
'''

argv_template = ''

stdin_template = ''

stdout_template = ''
