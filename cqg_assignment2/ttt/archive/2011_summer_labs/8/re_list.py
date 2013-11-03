game_type = 'input_output'

source_language = 'python'

parameter_list = [
        ['$list','string'],['$y0','string'],['$y1','string'],['$y2','string']
]

tuple_list = [
	['re_list_',
		[
			"[ ['^0$','0'], ['^01$','01'], ['^01$','01'] ]",
			None,
			None,
			None
		],
		[
			"[ ['(0|1|2)x','x'], ['0|1|2x','1x'], ['[012]x','x'] ]",
			None,
			None,
			None
		],
		[
			"[ ['aa|bb','bab'], ['aa|bb','aba'], ['aa|bb','xabay'] ]",
			None,
			None,
			None
		],
	],
]

global_code_template = '''\
x	import sys
dx	import re
'''

main_code_template = '''\
dx	for x in $list:
dx		if re.search(x[0],x[1]):
dx			print 'match'
dx		else:
dx			print 'no match'
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
