import os
import sys

'''
global preconditions:
	parameters named...
		position are in range(len(self.get_question_list()))
		*_dir are strings
'''
class model:
	def __init__(self):
		# quiz variables
		self.practice_mode = True
		self.standalone = False
		self.logged = False
		self.log_dir = ''

		# nested list holds (mark, count, [dirs]) for each group
		self.question_list = [] 

	#getters & setters
	def get_practice_mode(self):
		return self.practice_mode

	def set_practice_mode(self,value):
		self.practice_mode = value

	def get_standalone(self):
		return self.standalone

	def set_standalone(self,value):
		self.standalone = value

	def get_logged(self):
		return self.logged

	def set_logged(self,value):
		self.logged = value

	def get_log_dir(self):
		return self.log_dir

	def set_log_dir(self,value):
		self.log_dir = value

	#returns a (deep) copy of the question list
	def get_question_list(self):
		copy = []
		for i in range(len(self.question_list)):
			group = copy_group(self.question_list[i])
			copy.append(group)
		return copy
	
	#returns a copy of the directories list for group at position
	def get_dir_list(self,position):
		copy = copy_group(self.question_list[position])
		return copy[2]

	'''
	precondition
		group is None or a list of the form
			[int,int,[<zero or more str>]]
	'''
	def insert_group(self,position,group,is_list):
		if group is None:
			if is_list:
				group = [1,1,[]]
			else:
				group = [1,1,'']
		copy = copy_group(group)
		self.question_list.insert(position,copy)

	'''
	precondition
		mark_count is 0 or 1
	'''
	def update_group(self,position,mark_count,new_value):
		try:
			self.question_list[position][mark_count] = \
				int(new_value)
		except:
			# don't care if new_value is not an int -- we'll just
			# keep the old one.
			pass

	def group_update_dir(self,position,new_list):
		self.question_list[position][2] = new_list
	
	def group_add_dir(self,position,new_dir):
		self.question_list[position][2].append(new_dir)

	def group_remove_dir(self,position,remove_dir):
		try:
			self.question_list[position][2].remove(remove_dir)
		except:
			# ignore not-in-list errors (can happen if more than
			# one remove window is active for the same group)
			pass

	# removes the question group at position, and returns it
	def remove_group(self,position):
		return self.question_list.pop(position)

	'''
	precondition
		filename is a readable, valid quiz spec file
	'''
	def load(self,filename):
		# import is less likely than exec() to mess up the program
		# state on a bad file. this is the same routine we use when we
		# load a quiz spec on a running cqg server.
		filename = os.path.split(filename)
		path = filename[0]
		filename = filename[1]
		# FIXME: this should be a regexp; will fail on "test.py-foo.py"
		module = filename.replace('.py','')
		sys.path.insert(0,path) 
		loaded = reload(__import__(module))
		sys.path.pop(0)

		self.practice_mode = loaded.practice_mode
		self.standalone = loaded.standalone
		self.logged = loaded.logged
		self.log_dir = loaded.log_dir
		self.question_list = []
		for group in loaded.question_list:
			# list() cast is for compatibility with older (tuple)
			# format quiz specs:
			group = list(group)
			# append a boolean indicate weather it is pattern
			self.question_list.append(group)

	'''
	purpose
		write this quiz spec object to the named file
	precondition
		filename is the path to a writeable file
	'''
	def save(self,filename):
		f = open(filename,'w')
		qlist = list(self.question_list)
		f.write('question_list = '+str(qlist)+'\n')
		f.write('practice_mode = '+str(self.practice_mode)+'\n')
		f.write('standalone = '+str(self.standalone)+'\n')
		f.write('logged = '+str(self.logged)+'\n')
		#log dir is a string, so it needs quoting:
		f.write("log_dir = '"+self.log_dir+"'\n")
		f.close()
	
'''
purpose
	returns a copy of the referenced question group
precondition
	group is a nested list of the form [int,int,[str,str,...]]
'''
def copy_group(group):
	copy = []
	#mark
	copy.append(group[0])
	#count
	copy.append(group[1])
	#directories (list slice of whole list creates a copy)
	if type(group[2]) == str:
		copy.append(group[2])
	else:
		copy.append(group[2][:])
	return copy
