question_type = 'input_output'
source_language = 'python'

hotspot_declarations = [
	['$C','string'],['$K','int'],['$out','string']
]

group_list = [
	['caesar_decrypt_io_',	['IFMMP',1,None]],
]

global_code_template = '''\
dx	letters = [
dx		'A','B','C','D','E',
dx		'F','G','H','I','J',
dx		'K','L','M','N','O',
dx		'P','Q','R','S','T',
dx		'U','V','W','X','Y',
dx		'Z'
dx	]
dx
dx	def caesar_decrypt(C,N):
dx		P = ''
dx		for c in C:
dx			c_i = letters.index(c)
dx			if c_i >= N:
dx				p_i = c_i-N
dx			else:
dx				p_i = c_i + len(letters) - N
dx			P += letters[p_i]
dx		return P
'''

main_code_template = '''\
dx	print caesar_decrypt('$C',$K)
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out
'''
