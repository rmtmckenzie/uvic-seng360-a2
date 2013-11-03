question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$list','ascii_string'],
	['$y0','string'],['$y1','string'],['$y2','string']
]

group_list = [
	['list_forward_',
		[
			"[ ['^0$','01'], ['^01$','01'], ['^01$','01'] ]",
			None,None,None
		],
		[
			"[ ['(0|1|2)x','x'], ['0|1|2x','1x'], ['[012]x','x'] ]",
			None,None,None
		],
		[
			"[ ['aa|bb','bab'], ['aa|bb','aba'], ['aa|bb','xabay'] ]",
			None,None,None
		],
		[
			"[ ['\w3\w \dR\d','v3r5R9'],['\wT\w \d\w\d','5T3 1Z7'],['\w\d\w \d\w\d','v9a 6y1'] ]",
			None,None,None
		],
		[
			"[ ['\w?E\w\w[1-4]+','seng265'],['\w?E\w\w[1-4]+','SENG222'],['\w?E\w\w[1-4]+','Eng311'] ]",
			None,None,None
		],
		[
			"[ ['uivc*','uvicuvic'], ['uvic*','uviccc'],['uvic*','uvi'] ]",
			None,None,None
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
