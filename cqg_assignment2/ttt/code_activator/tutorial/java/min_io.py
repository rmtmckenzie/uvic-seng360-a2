question_type = 'input_output'
source_language = 'java'
public_class_name = 'Min'

parameter_list = [
	['$i1','int'],['$i2','int'],['$y0','int']
]

tuple_list = [
	['java_min_io_forward_',	[1,2,None],	[4,9,None]],
	['java_min_io_backward_',	[None,None,1],	[None,None,6]],
	['java_min_io_mixed_',	[None,2,None],	[3,None,1]],
	['java_min_io_open_',	[None,None,None]],
]

global_code_template = ''

main_code_template = '''\
dx			int a,b;
dx			a = $i1;
dx			b = $i2;
dx			if (a < b)
dx				System.out.println(a);
dx			else
dx				System.out.println(b);
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''
