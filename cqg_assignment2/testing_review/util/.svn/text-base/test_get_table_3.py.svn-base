import html_util

print '''<html>
<head>
<title>html_util.get_table() - with selective 3px border</title>
<style type='text/css'>''' + \
html_util.make_css_borders(3) + \
'''
</style>
</head>
<body>
''' + \
html_util.get_table([
 ['','9','8'],
 ['','','3'],
 [('1','top_border'),('0','top_border'),('1','top_border')]
],'cellspacing=0') + \
'''
</body>
</html>
'''
