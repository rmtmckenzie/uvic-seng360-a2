question_type = 'bullseye'

source_language = 'C'

parameter_list = [ 
 ['$t0','target'],['$t1','target'],['$t2','target'],['$t3','target'],
 ['$x1','int'],['$x2','int'] 
]

tuple_list = [
 ['bin_search_bull_',
	[True,True,True,True,None,None],
 ]
]

global_code_template = '''\
dx	int binsearch(int x, int v[], int n) 
dx	{
dx		int low = 0, high = n, mid;
dx	
dx		while (low <= high) {
dx			mid = (low + high) / 2;
dx			if (x < v[mid]) {
dx				$t0
dx				high = mid - 1;
dx			} else if (x > v[mid]) {
dx				$t1
dx				low = mid + 1;
dx			} else {
dx				$t2
dx				return mid;
dx			}
dx		}
dx		$t3
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
