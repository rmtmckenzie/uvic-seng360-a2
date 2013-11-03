import os
import file_util
import html_util
import hamming_util

# table properties
BORDER = 1
MIN_CELL_WIDTH = 36
MIN_CELL_HEIGHT = 16

# superclass for our two question types
class hamming:
	def __init__(self,question_library_path,question_path):
		self.question_library_path = question_library_path
		self.question_path = question_path
		config = file_util.dynamic_import(os.path.join(
		 question_library_path,question_path,'cqg_config.py'))

		self.parity = config.parity
		self.code_word = list(
		 hamming_util.generate_code_word(config.message,config.parity))
		self.code_word_indexes = config.code_word_indexes

	def get_question_library_path(self):
		return self.question_library_path
	
	def get_question_path(self):
		return self.question_path
	
	def get_css(self,answer):
		return ('#hamming_table td { '
		 'text-align:center;'
		 'width:%i; height:%i; }'%(MIN_CELL_WIDTH,MIN_CELL_HEIGHT)
		 + html_util.make_css_borders(BORDER,'hamming_table'))

class fill(hamming):
	def __init__(self,question_library_path,question_path):
		hamming.__init__(self,question_library_path,question_path)
		# replace code_word hotspots with None
		for i in self.code_word_indexes:
			self.code_word[i-1] = None

	def get_html(self,answer):
		# generate question description
		if self.parity == 0:
			parity_string = 'even'
		else:
			parity_string = 'odd'
		html = "<p>Fill in the bits for a valid Hamming code " + \
		 'using <b>' + parity_string  + '</b> parity:</p>'

		# generate a list of selects with bits specified by answer
		# bits = list of len(code_word) items where bits[i]:
		#	code_word[i] if code_word[i] in [0,1]
		#	a select box if code_word[i] is None
		indexes = range(1,len(self.code_word)+1) # one-relative
		bits = []
		for i,bit in enumerate(self.code_word,1):
			if bit == None:
				name = 'bit_' + str(i)
				bit = html_util.get_select(
				 name,['','0','1'],answer[name])
			bits.append(bit)

		# generate table containing select lists
		html += '<center>'
		html += html_util.get_table([indexes,bits],'id="hamming_table"')
		html += '</center>'

		return html

	def get_input_element_ids(self):
		ids = []
		for i,code in enumerate(self.code_word,1):
			if code == None:
				ids.append('bit_' + str(i))
		return ids

	def check_answer(self,answer):
		# fill code_word with bits specified by answer
		new_code_word = ''
		for i,bit in enumerate(self.code_word,1):
			if bit == None:
				bit = answer['bit_' + str(i)]

				# every input must be binary
				if bit not in ['0','1']:
					return False
			new_code_word += bit

		# check correctness of new_code_word
		return hamming_util.check_code_word(
		 new_code_word,self.parity) == 0

class find_error(hamming):
	def __init__(self,question_library_path,question_path):
		hamming.__init__(self,question_library_path,question_path)

		# flip bit specified by code_word_indexes
		if self.code_word[self.code_word_indexes-1] == '0':
			self.code_word[self.code_word_indexes-1] = '1'
		else:
			self.code_word[self.code_word_indexes-1] = '0'

	def get_html(self,answer):
		# generate question description
		if self.parity == 0:
			parity_string = 'even'
		else:
			parity_string = 'odd'
		html = '<p>Assume exactly one bit is incorrect.</p>' + \
		 'Indicate the incorrect bit ' + \
		 'using <b>' + parity_string  + '</b> parity:'

		# generate list of radio buttons with
		# the bit specified by answer set
		indexes = range(1,len(self.code_word)+1) # one-relative
		radio_buttons = []
		for i in indexes:
			is_set = answer['incorrect_bit'] == str(i)
			radio_buttons.append(html_util.get_radio_button(
			 'incorrect_bit',str(i),is_set))

		# generate table containing radio buttons
		html += '<center>'
		html += html_util.get_table(
		 [indexes,self.code_word,radio_buttons],'id="hamming_table"')
		html += '</center>'

		return html

	def get_input_element_ids(self):
		return ['incorrect_bit']

	def check_answer(self,answer):
		if not (answer['incorrect_bit'] != None and
		 answer['incorrect_bit'].isdigit()):
			return False

		code_word_string = ''
		for code in self.code_word:
			code_word_string += code
		return int(answer['incorrect_bit']) == \
		 hamming_util.check_code_word(code_word_string,self.parity)
