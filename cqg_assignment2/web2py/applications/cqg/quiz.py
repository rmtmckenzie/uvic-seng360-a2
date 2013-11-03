import sys
import time
import re
import random
import os
import log
import errorlog
import traceback
import question.file_util as file_util
import question.html_util as html_util


class quiz:
	'''
	Exposure
		public
	Purpose
		create necessary questions
	Precondition
		- the quiz_specifications directory must exist and be executable+readable
		- the file named by quiz_spec exists, is readable, and passes all tests
		  in qspec_verifier.py
	'''
	def __init__(self,quiz_spec):
		# import quiz_spec_file
		if not re.match("^[a-zA-Z0-9_/]*$",quiz_spec):
			errorlog.write("bad quiz name passed in URL: "+quiz_spec)
			raise IOError
		quiz_dir,quiz_name = os.path.split(quiz_spec)
		sys.path.append(os.path.abspath(os.path.join("../quizzes",
		 quiz_dir)))
		quiz_spec_file = __import__(quiz_name)

		for i in ['practice_mode','standalone','logged','log_dir']:
			setattr(self,i,getattr(quiz_spec_file,i))
		
		self.log_name = ''
		self.question_list = []
		self.answer_list = []
		self.message_list = []
		self.mark_list = []
		self.question_lib_path = "../question_library/"
		if 'question_library' in dir(quiz_spec_file):
			self.question_lib_path = quiz_spec_file.question_library

		for q in get_questions(quiz_spec_file.question_list,self.question_lib_path):
			config_file = os.path.join(self.question_lib_path,q[1],'cqg_config.py')
			try:
				config = file_util.dynamic_import(config_file)
				# construct question object
				exec('import question.'+config.product_family)
				exec('question_obj = question.'+config.product_family+'.'+config.question_type+'(self.question_lib_path,q[1])')
			except:
				trace = traceback.format_exc()
				errorlog.write("fatal: quiz spec OK, but question "+str(q)+" is problematic; full trace:\n"+trace)
			self.question_list.append(question_obj)
			blank_answer = {}
			for k in question_obj.get_input_element_ids():
				blank_answer[k] = None
			self.answer_list.append(blank_answer)
			self.message_list.append('')
			self.mark_list.append(q[0])

	'''
	Exposure
		public
	Purpose
		sets logging name for a marked quiz and initializes the log
		file by populating it with 'unanswered' entries for each
		question
	Precondition
		name is a string of chars [a-zA-Z0-9_]
	'''
	def initialize_log(self,name):
		self.log_name = name

		# initialize log file
		for i in range(len(self.question_list)):
			# log question path relative to question library
			log.write(
				self.log_dir,
				self.log_name,
				i,
				self.question_list[i].get_question_path(),
				0, # mark
				'', # answer
				0 # time
			)
		
	'''
	Exposure
		private
	'''
	def get_question_number(self,rv):
		if 'currqn' in rv:
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
		if 'but' in rv.keys():
			self.process_answer(q_num,rv)

		# submit button
		html = html_base.replace('$SUBMIT',gen_submit_button_html(
			self.practice_mode)) #qs_vars, qs_practice

		if ('get_css' in dir(self.question_list[q_num])):
			html = html.replace('$CSS',
				self.question_list[q_num].get_css(self.answer_list[q_num]))
		else:
			html = html.replace('$CSS','')
		html = html.replace('$QUESTION',
			self.question_list[q_num].get_html(self.answer_list[q_num]))
			#q_num in range, self.question_list, self.answer_list initialized
			#and same length > 0 (see constructor)

		# navi buttons
		if not self.standalone:
			html = html.replace('$Q_LINKS',
				self.gen_question_links())
		else:
			html = html.replace('$Q_LINKS','')
		
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
		#	EVENTUALLY: log this event
		contains_all = True
		for input_element_id in self.answer_list[q_num].keys():
			if not rv.has_key(input_element_id):
				contains_all = False
				break

		if contains_all:
			for input_element_id in self.answer_list[q_num].keys():
				self.answer_list[q_num][input_element_id] = \
				 rv[input_element_id]
			answer_correct = \
			 question.check_answer(self.answer_list[q_num])
		else:
			answer_correct = False

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
				question.get_question_path(), 
				int(answer_correct) * self.mark_list[q_num],
				dict(self.answer_list[q_num]),
				int(time.time()) - self.timer
			)
			self.message_list[q_num] = 'Answer recorded'

	def gen_question_links(self):
		links = ''
		for i in range(len(self.message_list)):
			if self.message_list[i] in \
			 ['Correct','Answer recorded']:
				colour = 'green'
			else:
				colour = 'white'
			links += '\t<a class="%s" href="?currqn=%i">%i</a>\n'%(
			 colour,i,i+1)

		return q_links_html.replace('$LINK_LIST',links)


#end of class; below here are private static utility methods and data

html_base = '''
<html>
<head>
	<style type="text/css">
		pre {
			padding-left: 3px;
		}
		#main {
			width:776px;
		}
		#question_cell {
			height:563px;
			overflow:hidden;
			padding:0px;
			text-align:center;
		}
		.quiz_outer_border {
			border:1px solid black;
		}
		#question_chooser {
			width:766px;
			text-align:left;
		}
		#question_chooser a {
			display: inline-block;
			text-align: center;
			width:18px;
			padding:2px 5px;
			margin:2px 0px;
			font:bold 14px sans-serif;
			text-decoration:none;
			color:black;
		}
		#question_chooser a.white {
			background-color:white;
		}
		#question_chooser a.green {
			background-color:#66cc33;
		}
		#submit_button_cell {
			padding:2px;
		}
		#message {
			margin-left:3px;
		}
$CSS
	</style>
</head>
<body>
<form method="get">
<table cellspacing="0" bgcolor="lightgrey" id="main" class="quiz_outer_border">
  <tr><td colspan="3" id="question_cell">$QUESTION</td>
  </tr>
$Q_LINKS
  <tr>
    <th align="left" bgcolor="white" width="33%" class="quiz_outer_border">
      <font color="$FONTCOLOR"><span id="message">$MESSAGE</span></font>
    </th>
    <td align="center" width="33%" class="quiz_outer_border" id="submit_button_cell">
    $SUBMIT
    </td>
    $INFO
  </tr>
</table>
<input type="hidden" name="currqn" value="$Q_NUM">
</form>
</body>
</html>'''

q_links_html = '''
  <tr><td align="center" colspan="3" class="quiz_outer_border">
  <div id="question_chooser">
$LINK_LIST &nbsp;
  </div>
  </td></tr>
'''

'''
Exposure
	private
'''
def gen_submit_button_html(practice_mode):
	value = 'Check answer'
	if not practice_mode:
		value = 'Submit answer'
	return html_util.get_submit('but',value)

'''
Exposure
	private
'''
def gen_info_html(q_num,total,mark):
	#q_num + 1 is for display only; everywhere else, q_num is an array index
	return '<td align="right" class="quiz_outer_border">Question '+str(q_num+1)+\
	 ' of '+str(total)+' ('+str(mark)+' Marks)</td>'

def get_question_dirs(question_library,subdirectory):
	'''
	purpose
		return all question directories in question_library/sub_dir
		result is equivalent to the command line:
		cd question_library; find -name cqg_config.py | sed 's/cqg_config.py$//'
	precondition
		question_library is a readable directory 
		subdirectory is a readable directory below question_library,
		 or the empty string
	'''
	all_questions = []
	L = os.listdir(os.path.join(question_library,subdirectory))
	for d in L:
		p = os.path.join(subdirectory,d)

		# if p is a file, it cannot be a question dir; ignore it
		if not os.path.isdir(os.path.join(question_library,p)):
			continue

		t = os.path.join(question_library,p,'cqg_config.py')
		if os.path.isfile(t):
			# p is a question
			all_questions.append(p)
		else:
			# p is a non-question subdir; may contain more questions
			all_questions += get_question_dirs(question_library,p)

	return all_questions

'''
Exposure
	private
Precondition
	- question_list consists of 3-tuples of (int,int,list of strings/string)
	  that have passed qspec_verifier.py
'''
def get_questions(question_list,qlib_path):
	all_questions = get_question_dirs(qlib_path,'')
	questions = []
	for question in question_list:
		mark = question[0]
		count = question[1]

		sources = []
		if type(question[2]) == list:
			for p in question[2]:
				sources.append(p)
		else:
			for p in all_questions:
				if re.search(question[2],p) != None:
					sources.append(p)

		# trim count to avoid random.sample exception
		if count > len(sources):
			count = len(sources)

		# select from question list: randomly selection/order
		L = random.sample(sources,count)
		for source in L:
			questions.append((mark,source))

	return questions
