question_type = 'input_output'

source_language = 'python'

hotspot_declarations = [
        ['$x0','ascii_string'],
	['$y0','string'],['$y1','string'],['$y2','string']
]

group_list = [
	['date_',
		['July 5 2011', None, None, None],
		['july 5 2011', None, None, None],
		['July 5, 2011', None, None, None],

		['5 July 2011', None, None, None],
		['5 july 2011', None, None, None],
		['5 July 11', None, None, None],

		['5/7/2011', None, None, None],
		['55/7/2011', None, None, None],
		['5/17/2011', None, None, None],
		['5/17/011', None, None, None],
		['5/17/2011', None, None, None],
		['5/17/11', None, None, None],
	]
]

global_code_template = '''\
x	import sys
dx	import re
'''

main_code_template = '''\
dx	def parse_date(s):
dx		m = re.search('([a-zA-Z]+) ([0-9]+), ([0-9]+)', s)
dx
dx		if m:
dx			if m.group(1) in monthNumber:
dx				return [
dx					int(m.group(2)),
dx					monthNumber[m.group(1)],
dx
dx					int(m.group(3))
dx				]
dx			else:
dx				return [0,0,0]
dx
dx		m = re.search('([0-9]+) ([a-zA-Z]+) ([0-9]+)', s)
dx		if m:
dx			if m.group(2) in monthNumber:
dx				return [
dx					int(m.group(1)),
dx					monthNumber[m.group(2)],
dx					int(m.group(3))
dx				]
dx			else:
dx				return [0,0,0]
dx
dx		m = re.search('([0-9]+)/([0-9]+)/([0-9]+)', s)
dx		if m:
dx			return [
dx				int(m.group(1)),
dx				int(m.group(2)),
dx				int(m.group(3))
dx			]
dx
dx		return [0,0,0]
dx
dx	monthNumber = {
dx		'January' : 1, 'February' : 2, 'March' : 3,
dx		'April' : 4, 'May' : 5, 'June' : 6,
dx		'July' : 7, 'August' : 8, 'September' : 9,
dx		'October' : 10, 'November' : 11, 'December' : 12
dx	}
dx
dx	x = parse_date('$x0')
dx	print x[0]
dx	print x[1]
dx	print x[2]
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
