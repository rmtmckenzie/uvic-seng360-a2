import html_util

print '''<html>
<head><title>html_util test output</title></head>
<body>
'''

print 'default height ' + \
 html_util.get_select_multiple('text0',['0','1','2','3','4'],[]) + \
 '<p>' + \
 'explicit height ' + \
 html_util.get_select_multiple('text1',['0','1','2','3','4'],[],3) + \
 '<p>' + \
 'multiple selections ' + \
 html_util.get_select_multiple('text1',['0','1','2','3','4'],['1','3'])

print '''
</body>
</html>
'''
