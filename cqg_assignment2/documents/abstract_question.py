# specification for question class of type T

class T:
	def __init__(self,question_library_path,question_path):
		'''
		purpose
			retrieve the question specified by path
		preconditions
			question_library_path,question_path are strings
		'''
		pass
	
	def get_question_library_path(self):
		'''
		purpose
			return question_library_path passed in constructor
		preconditions
			None
		'''
		pass
	
	def get_question_path(self):
		'''
		purpose
			return question_path passed in constructor
		preconditions
			None
		'''
		pass

	def get_css(self,answer):
		'''
		purpose
			return a CSS string which will be placed in the
			HTML <head> tag
		preconditions
			for each key K in get_input_element_ids():
				K is also in answer
				if K was not in submitted answer
					answer[K] == None
		'''
		pass
		
	def get_html(self,answer):
		'''
		purpose
			return a string containing the html to be displayed
			by abstract_question, including answers
		preconditions
			for each key K in get_input_element_ids():
				K is also in answer
				if K was not in submitted answer
					answer[K] == None
		'''
		pass
	
	def get_input_element_ids(self):
		'''
		purpose
			return a list containing the names of the HTML
			input elements returned by get_html()
		preconditions
			None
		'''
		pass
	
	def check_answer(self,answer):
		'''
		purpose
			return True iff answer is correct
		preconditions
			for each key K in get_input_element_ids():
				K is also in answer
				if K was not in submitted answer
					answer[K] == None
		'''
		pass
