question_type = 'input_output'

source_language = 'C'

hotspot_declarations = [
	['$out0','string'], ['$out1','string'],
	['$out2','string'], ['$out3','string'],
	['$out4','string'], ['$out5','string'],
	['$out6','string'], ['$out7','string'],
	['$out8','string'], ['$out9','string'],
]

group_list = [
	['mpg_io_',
		[None,None, None,None, None,None, None,None, None,None],
	],
]


global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx	
'''

main_code_template = '''\
dx
dx		double K_P_M = 1.609; // kilometres per mile
dx		double L_P_G = 3.785; // litres per gallon
dx
dx		for (int m_p_g = 15; m_p_g <= 35; m_p_g = m_p_g + 5) {
dx			double k_p_g = m_p_g*K_P_M; // convert miles to kilometres
dx			double k_p_l = k_p_g/L_P_G; // convert gallons to litres
dx			double l_p_k = 1/k_p_l; // invert
dx			double l_p_100_k = l_p_k*100; // change to per 100
dx		}
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$out0	$out1
$out2	$out3
$out4	$out5
$out6	$out7
$out8	$out9
'''
