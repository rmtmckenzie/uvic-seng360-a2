import question_template

game_type = 'bullseye'
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
dx	int a[] = {1, 3, 5, 7, 9};
dx	
dx	binsearch($x1, a, 5);
dx	binsearch($x2, a, 5);
'''

argv_template = ''

stdin_template = ''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
