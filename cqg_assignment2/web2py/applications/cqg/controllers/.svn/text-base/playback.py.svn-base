import os
import ast # for converting string to dict
import libxml2 # for parsing quiz log
import cPickle

import playback as Playback

def index():
	if 'log_dir' in request.vars.keys():
		# at the beginning, get log_dir and login form request.vars
		log_base = '../quiz_log'
		log_dir = request.vars.log_dir
		login = request.vars.login
		quiz_log = os.path.join(log_base,log_dir,login+'.xml')
		if not os.path.isfile(quiz_log):
			return 'No record for '+login+' in quiz '+log_dir

		# parse the log file to get question path, answer and result
		record = {}
		content = open(quiz_log,'r').read()
		content = '<rx>\n'+content+'</rx>\n'
		parse_tree = libxml2.parseDoc(content)
		context = parse_tree.xpathNewContext()
		for question in context.xpathEval('/rx/question'):
			index = 0
			question_path = ''
			answer = {}
			result = 0
			for x in question.xpathEval('index/text()'):
				index = int(x.get_content())
			for x in question.xpathEval('path/text()'):
				question_path = x.get_content()
			for x in question.xpathEval('answer/text()'):
				answer = ast.literal_eval(x.get_content())
			for x in question.xpathEval('result/text()'):
				result = int(x.get_content())
			record[index] = [question_path,answer,result]
		print record
		quizobj = Playback.quiz(record)
		session['quiz'] = cPickle.dumps(quizobj)
	quizobj = cPickle.loads(session['quiz'])
	html = quizobj.get_html(request.vars)
	session['quiz'] = cPickle.dumps(quizobj)
	return html
