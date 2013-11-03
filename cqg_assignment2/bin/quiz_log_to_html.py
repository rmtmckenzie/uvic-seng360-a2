#!/usr/bin/python

import os
import sys
import libxml2
import file_util

html_base = '''
<html>
<head>
	<style type="text/css">
		pre {
			padding-left: 3px;
		}
		table,td,th {
			border:1px solid black;
		}
		#main {
			width:776px;
		}
		#question_cell {
			height:563px;
			overflow:hidden;
			padding:0px;
			text-align:center;
			border:0px;
		}
		.nb, .nb td, .nb th {
			border:0px;
		}
$CSS
	</style>
</head>
<body>
<table cellspacing="0" bgcolor="lightgrey" id="main">
  <tr><td id="question_cell">$QUESTION</td></tr>
</table>
</body>
</html>
'''

def instantiate_question(question_library_path,question_path):
	'''
	purpose
		returns a question object instantiated from
		question_library_path/question_path
	precondition
		path is a string
	exceptions
		throws an exception of question could not be instantiated
	'''
	config_file = os.path.join(question_library_path,question_path,
	 'cqg_config.py')
	config = file_util.dynamic_import(config_file)

	# construct question object
	exec('import question.'+config.product_family)
	exec('question_obj = question.%s.%s(question_library_path,question_path)' % \
	 (config.product_family, config.question_type))
	return question_obj

# check number of command arguments
if len(sys.argv) != 4:
	print 'Usage: quiz_log_to_html.py log_file.xml question_library output_directory'
	sys.exit(-1)

log_filename = sys.argv[1]
question_library = sys.argv[2]
output_directory = sys.argv[3]

# read quiz log
f = open(log_filename,'r')
log_content = f.read()
f.close()

# create html output directory
html_dir = os.path.split(log_filename)[1] # get log file name without path
html_dir = os.path.splitext(html_dir)[0] # remove the extension
html_dir = os.path.join(output_directory,html_dir)
if os.path.exists(html_dir):
	print "error: html output directory '%s' already exists" % html_dir
	sys.exit(1)
os.mkdir(html_dir)

# kludge: add XML root element
log_content = '<root>\n' + log_content + '</root>\n'

# use libxml2 to parse log & create a context for XPath query
parse_tree = libxml2.parseMemory(log_content,len(log_content))
context = parse_tree.xpathNewContext()

questions = {}
for question in context.xpathEval('/root/question'):
	index = int(question.xpathEval('index/text()')[0].get_content())
	mark = int(question.xpathEval('result/text()')[0].get_content())

	try:
		answer = question.xpathEval('answer/text()')[0].get_content()
		answer = eval(answer) # convert string to dictionary
	except:
		answer = {}

	question_path = question.xpathEval('path/text()')[0].get_content()

	try:
		question_obj = instantiate_question(
		 question_library,question_path)
		questions[index] = [question_obj,mark,answer]
	except:
		print "error: could not instantiate",path

# free resources used by xml parser
context.xpathFreeContext()
parse_tree.freeDoc()

# generate individual question HTML files
for i in sorted(questions.keys()):
	question_obj,mark,answer = questions[i]

	# treat "not attempted" as all-blank submission for display purposes
	if len(answer) == 0:
		answer = {}
		for k in question_obj.get_input_element_ids():
			answer[k] = None

	# get HTML and CSS representation from question object
	question_html = question_obj.get_html(answer)
	if 'get_css' in dir(question_obj):
		css = question_obj.get_css(answer)
	else:
		css = ''

	html = html_base
	html = html.replace('$QUESTION',question_html)
	if mark:
		html = html.replace('$FONTCOLOR','green')
		html = html.replace('$MESSAGE','Correct')
	else:
		html = html.replace('$FONTCOLOR','darkred')
		html = html.replace('$MESSAGE','Incorrect')
	html = html.replace('$MARKS',str(mark))
	html = html.replace('$Q_NUM',str(i+1))

	html = html.replace('$CSS',css)

	file_util.write_string(os.path.join(html_dir,'question_%i.html'%i),
	 html)

# generate index HTML file
index_html = '''
<html>
<head>
</head>
<body>
$INDEX
</body>
</html>
'''
index = ''
for i in sorted(questions.keys()):
	index += "<a href='question_%i.html'>Question %i</a> " % (i,i+1)
	if questions[i][1]: # if mark is != 0
		index += "Correct"
	else:
		index += "Incorrect"
	index += "<br />"

index_html = index_html.replace('$INDEX',index)
file_util.write_string(os.path.join(html_dir,'index.html'),index_html)
