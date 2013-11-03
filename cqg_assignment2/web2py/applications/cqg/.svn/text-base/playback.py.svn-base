import sys
import time
import re
import random
import os
import log
import errorlog

question_lib_path = "../question_library/"

class quiz:
	'''
	Exposure
		public
	Purpose
		create necessary questions
	Precondition
		- record is a dict of questions/answers/results
	'''
	def __init__(self,record):
		# quiz variables:
		#	playback is valable for non-standalone marked quiz
		# 	assume standalone is false
		self.practice_mode = False
		self.standalone = False
		self.logged = True
		self.log_dir = ''
		self.question_list = []
		self.answer_list = []
		self.message_list = []
		self.mark_list = []
		
		L = record.keys()
		L.sort()
		for k in L:
			q = record[k]
			path = q[0]
			answer = q[1]
			result = q[2]
			message = 'Correct'
			if result == 0:
				message = 'Incorrect'
			types = os.path.join(path,'types.py')
			try:
				exec(open(types,'r').read())
				# construct question object
				exec('import question.'+product_family)
				exec('question_obj = question.'+product_family+'.'+question_type+'(path)')
			except:
				errorlog.write("fatal: quiz spec OK, but question "+str(q)+" is problematic")
			self.question_list.append(question_obj)
			self.answer_list.append(answer)
			self.message_list.append(message)
			self.mark_list.append(result)

	'''
	Exposure
		public
	Purpose
		sets logging name for a marked quiz
	Precondition
		name is a string
	'''
	def set_log_name(self,name):
		self.log_name = name
		
	'''
	Exposure
		private
	'''
	def get_question_number(self,rv):
		if 'currqn' in rv and 'previousq' in rv:
			next_q_num = int(rv['currqn'])-1
		elif 'currqn' in rv and 'nextq' in rv:
			next_q_num = int(rv['currqn'])+1
		elif 'currqn' in rv and 'but' in rv:
			next_q_num = int(rv['currqn'])
		else:
			next_q_num = 0

		if next_q_num >= len(self.question_list):
			return len(self.question_list) - 1
		if next_q_num < 0:
			return 0

		return next_q_num

	'''
	Exposure
		public
	Precondition
		- rv is a dictionary
		- if 'but' in rv.keys() , rv.keys() also contains every
		  key in self.question_list[q_num].get_input_element_ids()
		- self.question_list[q_num].get_html() always returns a string if question was
		  successfully instantiated
		- get_question_number() always returns an int from 0 to
		  len(question_list)
	'''
	def get_html(self,rv):

		q_num = self.get_question_number(rv) #q_num always in range

		# submit button
		html = html_base.replace('$SUBMIT',gen_submit_button_html(
			self.practice_mode)) #qs_vars, qs_practice

		html = html.replace('$QUESTION',
			self.question_list[q_num].get_html(self.answer_list[q_num]))
			#q_num in range, self.question_list, self.answer_list initialized
			#and same length > 0 (see constructor)

		# navi buttons
		if not self.standalone:
			html = html.replace('$PREVIOUS',
				gen_previous_button_html(q_num == 0))
			html = html.replace('$NEXT',
				gen_next_button_html(q_num + 1 == len(self.question_list)))
		else:
			html = html.replace('$PREVIOUS','')
			html = html.replace('$NEXT','')
		
		# info cell
		if not self.standalone:
			html = html.replace('$INFO',
				gen_info_html(q_num,len(self.question_list),self.mark_list[q_num]))
				#self.mark_list initialized and same length > 0 as question_list
		else:
			html = html.replace('$INFO','')
	
		# message cell
		#self.message_list initialized and same length > 0 as question_list
		if self.message_list[q_num] == 'Correct':
			html = html.replace('$FONTCOLOR','green')
		else:
			html = html.replace('$FONTCOLOR','darkred')
		html = html.replace('$MESSAGE',self.message_list[q_num])
		html = html.replace('$Q_NUM',str(q_num))

		#updating timer as late as possible is fairer
		self.timer = int(time.time())
		return html

	'''
	Exposure
		private
	Purpose
		update the message in self.message_list[q_num]
	Precondition
		- rv is a dictionary with a key for every item in
		  self.question_list[q_num].get_input_element_ids()
		- q_num is a int 0 <= question_num < len(question_list)
	'''
	def process_answer(self,q_num,rv):
		question = self.question_list[q_num]
		self.answer_list[q_num] = rv

		answer_correct = question.check_answer(rv)
		if self.practice_mode:
			if answer_correct:
				self.message_list[q_num] = 'Correct'
			else:
				self.message_list[q_num] = 'Incorrect'
		else:
			log.write(
				self.log_dir,
				self.log_name,
				q_num,
				#FIXME: update docs to say path is public, or better yet,
				#implement question.getIdentifier() as described in giant todo
				#file
				question.path, 
				int(answer_correct) * self.mark_list[q_num],
				answer,
				int(time.time()) - self.timer
			)
			self.message_list[q_num] = 'Answer recorded'


#end of class; below here are private static utility methods and data

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
	</style>
</head>
<body>
<form method="get">
<table cellspacing="0" bgcolor="lightgrey" id="main">
  <tr><td colspan="2" id="question_cell">$QUESTION</td></tr>
  <tr><td align="center" colspan="2" style="height:50px;width:260px">
    <table class="nb" style="width:100%;text-align:center;"><tr><td>$PREVIOUS</td><td>$SUBMIT</td><td>$NEXT</td></table>
  </td></tr>
  <tr>
    <th align="left" bgcolor="white" width="60%">
      <font color="$FONTCOLOR">Message: <span id="message">$MESSAGE</span></font>
    </th>
    $INFO
  </tr>
</table>
<input type="hidden" name="currqn" value="$Q_NUM">
</form>
</body>
</html>'''

'''
Exposure
	private
'''
def gen_submit_button_html(practice_mode):
	label = 'Check answer'
	if not practice_mode:
		label = 'Submit answer'
	return '<input type="submit" style="height:30;width:180;font-size:100%"\
	 name="but" value="'+label+'" disabled>'

'''
Exposure
	private
'''
def gen_next_button_html(disabled):
	disable = ''
	if disabled:
		disable = 'disabled'
	return '<input type="submit" style="height:30;width:90;font-size:100%"\
	 name="nextq" value="Next" '+disable+'>'

'''
Exposure
	private
'''
def gen_previous_button_html(disabled):
	disable = ''
	if disabled:
		disable = 'disabled'
	return '<input type="submit" style="height:30;width:90;font-size:100%"\
	 name="previousq" value="Previous" '+disable+'>'

'''
Exposure
	private
'''
def gen_info_html(q_num,total,mark):
	#q_num + 1 is for display only; everywhere else, q_num is an array index
	return '<td align="right">Question '+str(q_num+1)+' of '+str(total)+' ('+str(mark)+' Marks)</td>'

