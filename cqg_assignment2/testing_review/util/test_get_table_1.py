import html_util

print '''<html>
<head>
<title>html_util.get_table() - no borders</title>
</head>
<body>
''' + \
html_util.get_table([['a','b'],['c','d']]) + \
'''
</body>
</html>
'''
