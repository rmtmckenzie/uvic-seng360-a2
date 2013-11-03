import os
import cPickle

import quiz as Quiz

SERVERNAME = 'cdoku'
SERVERNAME = 'graffiti'

def index():
	# the beginning of the quiz, create quiz and init answer_list
	if 'spec' in request.vars.keys():
		try:
			quizobj = Quiz.quiz(request.vars['spec'])
			session['quiz'] = cPickle.dumps(quizobj)
		except:
			return "No such quiz"
		# reset the login
		if 'login' in session.keys():
			del session['login']

	# if quiz does not exist, redirect to home page
	if not 'quiz' in session.keys():
		redirect(URL(r=request, c='default'))

	#work around web2py session can't store instances problem:
#see http://groups.google.com/group/web2py/browse_thread/thread/acec00df5cf27193
#and https://groups.google.com/forum/#!msg/web2py/dmN54cpMuXo/lufvxmaQMLUJ
#this bug combines with the other one (see question/codeact.py), in that
#updates to class static vars *do* get stored in session, somehow
	#FIXME: cache.ram might be more appropriate
	quizobj = cPickle.loads(session['quiz'])

	# check login in marked mode
	if 'login' in session.keys() and session['login'] != '':
		#FIXME: I think this should be a constructor parameter. But since
		#we don't know until after instantiation whether a quiz is practice mode,
		#it can't be. hmm. should a composer really have its own login function,
		#or should that be a separate concern?
		quizobj.initialize_log(session['login'])
	if not quizobj.practice_mode and 'login' not in session.keys():
		redirect(URL(r=request, f='seng_auth'))
	else:
		session['login'] = ''
	
	html = quizobj.get_html(request.vars)
	session['quiz'] = cPickle.dumps(quizobj)
	return html

def seng_auth():
	if not 'username' in request.vars.keys(): # not a submission
		return dict(msg='')
	else: # request is a submission
		if request.vars['username'] == "cqg_tester":
			session.login = request.vars['username']
			redirect(URL(r=request, f='index'))
		# get user list
		user_list = 'allowed_users.txt'
		# check if student is registered in SENG265
		users = open(os.path.join('../users/',user_list),
		 'r').read().split('\n')
		if not request.vars['username'] in users:
			return dict(
			 msg = 'Not registered in the current session.')
		# authenticate username and password
		if os.uname()[1] == SERVERNAME:
			seng_auth = __import__('seng_auth')
			if seng_auth.authenticate(request.vars['username'],
			 request.vars['password']) != 0:
				return dict(msg='Wrong username or password.')
		session.login = request.vars['username']
		redirect(URL(r=request, f='index'))
