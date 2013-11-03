from html_util import *

print '''<html>
<head>
<title>html_util test output</title>
</head>
<body>
'''

print ('x ' + get_radio_button('radio_button_set_A','x',True)
 + 'y ' + get_radio_button('radio_button_set_A','y',False))

print '<br />'

print ('a ' + get_radio_button('radio_button_set_B','a',False)
 + 'b ' + get_radio_button('radio_button_set_B','b',True))

print '''
</body>
</html>
'''
