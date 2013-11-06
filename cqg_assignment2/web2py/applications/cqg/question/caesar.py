#A2 DONE

import os
import file_util
import html_util
import caesar_util

# specification for question class of type caesar

class caesar:
	def __init__(self,question_library_path,question_path):
		'''
		purpose
			retrieve the question specified by path
		preconditions
			question_library_path,question_path are strings
		'''

		config = file_util.dynamic_import(
			os.path.join(
				question_library_path, question_path, 'cqg_config.py'))
		self.question_library_path = question_library_path
		self.question_path = question_path

		self.plaintext = config.plaintext
		self.key = config.key
		self.hotspots = config.hotspots

		self.ciphertext = caesar_util.caesar_encrypt(self.plaintext, self.key)

	def get_question_library_path(self):
		'''
		purpose
			return question_library_path passed in constructor
		preconditions
			None
		'''
		return self.question_library_path

	def get_question_path(self):
		'''
		purpose
			return question_path passed in constructor
		preconditions
			None
		'''
		return self.question_path

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
		return style

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
		html = "<div>"
		html += ("<p>Use a <b>caesar</b> cipher with key {0}"\
				" to encrypt the plain text.</p>").format(self.key)

		html += "<table cellspacing='0' cellpadding='3'>\n"

		question_row = "<tr><td>plain text</td>"
		answer_row = "<tr><td>cipher text</td>"
		for index,(plain,cipher) in enumerate(zip(self.plaintext, self.ciphertext)):
			question_row += "<td>{0}</td>".format(plain)
			if index in self.hotspots:
				id = 'hotspot'+str(index)
				if id in answer and answer[id] is not None: ### DR1
					answer_row += '<td><input name="hotspot{0}" value="{1}"></input></td>'.format(index,answer[id]) ###DR2
				else:
					answer_row += '<td><input name="hotspot{0}"></input></td>'.format(index)
			else:
				answer_row += "<td>{0}</td>".format(cipher)
		question_row += "</tr>"
		answer_row += "</tr>"

		html += "{0}\n{1}\n</table>".format(question_row,answer_row)
		return html +  "</div>"

	def get_input_element_ids(self):
		'''
		purpose
			return a list containing the names of the HTML
			input elements returned by get_html()
		preconditions
			None
		'''
		return ["hotspot"+str(i) for i in self.hotspots]

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
		self.TEMP = str(answer)
		for key,value in answer.items():
			ind = int(key.replace('hotspot',''))
			if self.ciphertext[ind] == value: ###DR3
				continue
			else:
				break
		else:
			#this is valid python. This is executed iff
			# the loop finishes without a break.
			return True
		return False

style = '''
	#question_cell div {
		text-align:left;
		margin:auto;
	}
	#question_cell table, #question_cell td {
		border:0px;
	}
	#question_cell {
		border:1px solid black;
	}
	#question_cell input {
		width:2em;
	}
	#question_cell p {
		text-align: center;
	}
	#question_cell table {
		margin: auto;
	}
	td.top {
		vertical-align:top;
	}
	td.left {
		text-align:left;
	}
	#question_cell td {
		border-style: solid;
		border-color: black;
		border-top-width: 1px;
		border-left-width:1px;
		text-align:center;
	}
	#question_cell tr > td:first-child{
		text-align:right;
		border-left-width:0px;
	}
	#question_cell tbody>tr:first-child td{
		border-top-width:0px;
	}
'''
