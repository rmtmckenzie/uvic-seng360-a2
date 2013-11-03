import os
import sys

def check_directory(s,readable):
	'''
	purpose:
		if readable
			return: s is a readable directory
		else
			return: s is a readable and writeable directory
	preconditions:
		s is a string
	'''
	if readable:
		return os.path.isdir(s) and os.access(s,os.R_OK|os.X_OK)
	else:
		return os.path.isdir(s) and os.access(s,os.R_OK|os.W_OK|os.X_OK)

def dynamic_import(path):
	'''
	purpose:
		import and return a reference to the module specified in path
	preconditions:
		path is a string
	exceptions:
		throw ImportError if path cannot be imported
	'''
	# parse the path
	(path_prefix,file_name) = os.path.split(path)
	(module_name,extension) = os.path.splitext(file_name)

	# add to the module path: in front to avoid Python modules
	sys.path.insert(0,path_prefix)

	# if a module named M has been imported then 
	# 	an import of a module named M from a different path
	# 	will be ignored: reload is needed
	if module_name in sys.modules:
		m = sys.modules[module_name] # get module reference
		reload(m)
	else:
		m =  __import__(module_name)

	# remove path_prefix so caller is not affected
	sys.path.pop(0)

	return m

def write_string(path,s):
	'''
	purpose
		write the string s to path
	precondition
		path describes a filename in a writeable directory
		s is a string
	'''
	f = open(path,'w')
	f.write(s)
	f.close()
