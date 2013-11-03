import string
import os
import sys
import tuple_converter

'''
purpose
	create types.py
	write game_type and parameters into types.py
precondition
	path is a directory with write access
	game_type is a legal python string
	parameters is a dictionary of dictionaries of parameter-type pairs
'''
def gen_types(path,game_type,parameters):
	output = open(os.path.join(path,'types.py'),'w')
	if game_type == 'input_output':
		game_type_string = 'Input/output'
	elif game_type == 'bullseye':
		game_type_string = 'Bullseye'
	elif game_type == 'liar_liar':
		game_type_string = 'Liar-liar'
	elif game_type == 'find_the_failure':
		game_type_string = 'Find the failure'
	elif game_type == 'shell':
		game_type_string = 'Shell'
	output.write("game_type = '"+game_type_string+"'\n")
	output.write('parameter_types = '+str(parameters)+'\n')
	output.close()

'''
purpose
	create argvs.txt in dir path
	write argv to argvs.txt
precondition
	path is the path to a directory with write access
	argvs is a legal python string
'''
def gen_argvs(path,argvs,tuple):
	if 'argvs' in tuple.keys():
		for k in tuple['argvs'].keys():
			if tuple['argvs'][k] != None:
				argvs = argvs.replace(k,tuple['argvs'][k])
		cmd_argvs = open(os.path.join(path,'argvs.txt'),'w')
		cmd_argvs.write(argvs)

'''
purpose
	replace parameters in template(stdin or stdout) and write to fp 
precondition
	fp is a file object opened with option 'w'
	template is a legal python string
	parameters is a dictionary of dictionaries of parameter-value pairs
	key is a legal python string
'''
def gen_template(fp,template,parameters,key):
	if key in parameters.keys():
		for param in parameters[key].keys():
			if parameters[key][param] != None:
				template = template.replace(param,
					str(parameters[key][param]))
	fp.write(template)
            
'''
purpose
	write global variable declaration in run and faulty(in find_the_failure)
	substitute each parameter in template with values in parameters
	substitute each parameter in template with corresponding global variable
	write lines marked with 'd' to display
	write lines marked with 'x' to run
	write lines markes with 'X' to faulty in game find_the_failure
precondition
	template is a legal python string
	display and run are file objects created with option 'w'
	game_type is a legal python string
	values is a dictionary of dictionaries of parameter-value pairs 
	 of code template
	types is a dictionary of dictionaries of parameter-type pairs
	values and types are containing the same set of keys
	faulty is a file object created with option 'w' if game_type is 
		find_the_failure otherwise is None
	targets is a list of strings
	target_values is a list of booleans(bullseye) or strings(liar-liar)
'''
def parse_global(template,display,run,faulty,values,types,game_type,
		targets,target_values):
	# declare a global variable per code template parameter
	global_vars = ''
	if 'code' in types.keys():
		arg_count = 1
		L = types['code'].keys()
		L.sort()
		for k in L:
			if values['code'][k] != None:
				continue
			var_type = ''
			if types['code'][k] == 'string':
				var_type = 'char*'
			else:
				var_type = types['code'][k]
			global_vars += var_type+' cdoku_argv_'+\
			 str(arg_count)+';\n'
			arg_count += 1

	# declare a global variable per target
	if game_type == 'bullseye':
		arg_count = 0
		for i in range(len(targets)):
			if target_values[i]:
				global_vars += 'int cdoku_target_'+\
					str(arg_count)+';\n'
				arg_count += 1

	# declare a global variable per assert
	if game_type == 'liar_liar':
		arg_count = 0
		for i in range(len(targets)):
			if target_values[i] != '':
				global_vars += 'int cdoku_assert_'+\
					str(arg_count)+';\n'
				arg_count += 1
	run.write(global_vars)
	if game_type == 'find_the_failure':
		faulty.write(global_vars)

	# write the implementation of cdoku_assert()
	if game_type == 'liar_liar':
		run.write(gen_cdoku_assert(target_values))


	for line in template.split('\n'):
		# find the line prefix
		prefix = ''
		for n in range(len(line)):
			if line[n] in string.whitespace:
				prefix = line[:n]
				break
		if prefix == '':
			prefix = line
		line = line[n+1:]
		# substitute values with values
		if 'code' in values.keys():
			for k in values['code'].keys():
				line = line.replace(k,
				 str(values['code'][k]))

		# write the line to display
		if 'd' in prefix:
			if game_type == 'bullseye':
				display.write(set_bullseye(line,targets,
					target_values,True)+'\n')
			elif game_type == 'liar_liar':
				display.write(set_assert(line,targets,
					target_values,True)+'\n')
			else:
				display.write(line+'\n')

		# substitue parameters with global variables
		if 'code' in types.keys():
			arg_count = 1
			for k in L:
				if values['code'][k] == None:
					continue
				line = line.replace(k,
				 'cdoku_argv_'+str(arg_count))
				arg_count += 1
		
		# set targets
		if game_type == 'bullseye': 
			line = set_bullseye(line,targets,target_values,False)
		if game_type == 'liar_liar':
			line = set_assert(line,targets,target_values,False)

		# write line to run and faulty
		if 'x' in prefix:
			run.write(line+'\n')
		if 'X' in prefix and game_type == 'find_the_failure':
			faulty.write(line+'\n')
        
'''
purpose
	replace parameters with their values and write to display
	replace parameters with argv[N] and write to run
	replace parameters with argv[N] and write to faulty in game find the 
		failure
	add starting and end of main
precondition
	template is a legal python string
	display and run are file objects opened with option 'w'
	faulty is a file object created with option 'w' if game_type is 
		find_the_failure otherwise is None
	values is a dictionary of dictionaries of parameter-value pairs 
	 of code template
	types is a dictionary of dictionaries of parameter-type pairs
	values and types are containing the same set of keys
	targets is a list of strings
	target_values is a list of booleans(bullseye) or strings(liar-liar)
'''
def parse_main(template,display,run,faulty,values,types,game_type,targets,
	target_values):
	# write the beginning of main
	display.write('int main(int argc, char* argv[])\n{\n')
	run.write('int main(int argc, char* argv[])\n{\n')
	if game_type == 'find_the_failure':
		faulty.write('int main(int argc, char* argv[])\n{\n')

	main = template
	M = {}
	if 'code' in values.keys():
		# replace parameters with their values
		for param in values['code'].keys():
			if values['code'][param] != None:
				main = main.replace(param,
				 str(values['code'][param]))

		# assign the value of argv[N] to corresponding global variable
		arg_count = 0
		L = types['code'].keys()
		L.sort()
		s = ''
		for k in L:
			if values['code'][k] != None:
				continue
			if types['code'][k] == 'int':
				s += '\tcdoku_argv_'+str(arg_count+1)\
				 +' = atoi(argv['+'argc-'+\
				 str(len(values['code'].keys()))+\
				 '+'+str(arg_count)+']);\n'
			elif types['code'][k] == 'float':
				s += '\tcdoku_argv_'+str(arg_count+1)+\
				 ' = atof(argv['+'argc-'+\
				 str(len(values['code'].keys()))+\
				 '+'+str(arg_count)+']);\n'
			else:
				s += '\tcdoku_argv_'+str(arg_count+1)+\
				 ' = argv[argc-'+\
				 str(len(values['code'].keys()))+\
				 '+'+str(arg_count)+'];\n'
			M[k] = 'cdoku_argv_'+str(arg_count+1)
			arg_count += 1
		run.write(s)
		if game_type == 'find_the_failure':
			faulty.write(s)

	# loop through each line
	for line in main.split('\n'):
		# find the line prefix
		prefix = ''
		for n in range(len(line)):
			if line[n] in string.whitespace:
				prefix = line[:n]
				break
		if prefix == '':
			prefix = line
		line = line[n:]

		if 'd' in prefix:
			if game_type == 'bullseye':
				display.write(set_bullseye(line,targets,
					target_values,True)+'\n')
			elif game_type == 'liar_liar':
				display.write(set_assert(line,targets,
					target_values,True)+'\n')
			else:
				display.write(line+'\n')
		# substitute parameter with global variable
		if 'code' in values.keys():
			for k in M.keys():
				line = line.replace(k,M[k])
		# set targets
		if game_type == 'bullseye': 
			line = set_bullseye(line,targets,target_values,False)
		if game_type == 'liar_liar':
			line = set_assert(line,targets,target_values,False)

		if 'x' in prefix:
			run.write(line+'\n')
		if 'X' in prefix:
			faulty.write(line+'\n')

	# add flag checking code for bullseye
	if game_type == 'bullseye' or game_type == 'liar_liar':
		run.write(check_targets(target_values,game_type))

	# write return 0 
	display.write('\treturn 0;\n}\n')
	run.write('\treturn 0;\n}\n')
	if game_type == 'find_the_failure':
		faulty.write('\treturn 0;\n}\n')

'''
purpose
	substitute each parameter in code with values in parameters
	write lines marked with 'd' to display.txt
	write lines marked with 'x' to execute.txt
precondition
	code is a leagal python string
	name is the absolute path of the question directory
	tuple is a dictionary of dictionaries of parameter-value paris
'''
def parse_shell_code(code,name,tuple):
	# substitute parameters with their values
	if 'code' in tuple:
		for k in tuple['code'].keys():
			if tuple['code'][k] != None:
				code = code.replace(k,tuple['code'][k])

	# write line to display.txt/execute.txt base on line prefix
	display = open(os.path.join(name,'display.txt'),'w')
	execute = open(os.path.join(name,'execute.txt'),'w')
	for line in code.split('\n'):
		# find the line prefix
		prefix = ''
		for n in range(len(line)):
			if line[n] in string.whitespace:
				prefix = line[:n]
				break
		if prefix == '':
			prefix = line
		line = line[n+1:]
		# write the line to file
		if 'd' in prefix:
			display.write(line+'\n')
		if 'x' in prefix:
			execute.write(line+'\n')
	display.close()
	execute.close()

'''
purpose
	return a copy of code with
		is_display True:
			target_values[N] is True
				targets[N] change to 'cdoku_highlight'
		is_display False:
			target_values[N] is True
				targets[N] change to 'cdoku_target_N++'
		target_values[N] is False
			targets[N] change to ''
precondition
	code is a legal python strings
	targets is a list of strings
	target_values is a list of booleans
	targets and target_values are in the same length
	is_display is a boolean

'''
def set_bullseye(code,targets,target_values,is_display):
	count = 0
	for i in range(len(targets)):
		if target_values[i]:
			if is_display:
				code = code.replace(targets[i],
				 'cdoku_highlight')
			else:
				code = code.replace(targets[i],'cdoku_target_'+\
					str(count)+'++;')
				count += 1
		else:
			code = code.replace(targets[i],'')
	return code

'''
purpose
	return a copy of code with
		is_display True:
			target_values[N] is not None
				targets[N] change to 
				'cdoku_highlightassert(target_value[N]);'
		is_display False:
			target_values[N] is not None
				targets[N] change to 'cdoku_assert(N,expr);'
		target_values[N] is ''
			targets[N] change to ''
precondition
	code is a legal python strings
	targets is a list of strings
	target_values is a list of strings
	targets and target_values are in the same length
	is_display is a boolean
'''
def set_assert(code,targets,target_values,is_display):
	count = 0
	for i in range(len(targets)):
		if target_values[i] != '':
			if is_display:
				code = code.replace(targets[i],
					'cdoku_highlightassert('+\
					 target_values[i]+');')
			else:
				code = code.replace(targets[i],'cdoku_assert('+\
					str(count)+','+target_values[i]+');')
				count += 1
		else:
			code = code.replace(targets[i],'')
	return code

'''
purpose
	return a string which contain the C code of function cdoku_assert
	this C function increases cdoku_assert_N by 1 if target_value[i]
	is true
precondition
	target_values is a list of strings
'''
def gen_cdoku_assert(target_values):
	count = 0
	s = 'void cdoku_assert(int n,int expr) {\n\tif (!expr) {\n'
	for i in range(len(target_values)):
		if target_values[i] != '':
			s += '\t\tif (n == '+str(count)+\
			 ')\n\t\t\tcdoku_assert_'+str(count)+'++;\n'
			count += 1
	s += '\t}\n}\n'
	return s

'''
purpose
	write to string s 
		cdoku_target_0 && cdoku_target_1...cdoku_target_N) return 0;
			where N is the number of True in target_values
		else return 1;
	return s
precondition
	target_values is a list of booleans(bullseye) or strings(liar-liar)
'''
def check_targets(target_values,game_type):
	# decide prefix
	if game_type == 'bullseye':
		prefix = 'cdoku_target_'
	elif game_type == 'liar_liar':
		prefix = 'cdoku_assert_'
		
	# check target_0 ... target_N
	count = 0
	s = '\tif ('
	for i in range(len(target_values)):
		if target_values[i]:
			s += prefix+str(count)+' && '
			count += 1
	s = s[0:-4]+')\n\t\treturn 0;\n'
	s += '\telse\n\t\treturn 1;\n'
	return s	

'''
purpose
	create question directory, types.py, display.txt, execute and stdin.txt
precondition
	name is a legal python string of question dir name
	tp is a imported question template
	tuple is a dictionary of dictionaries of parameter-value pairs
'''
def create_question(name,tp,tuple,parameters):
	#create question dir if not exists
	if not os.path.exists(name):
                os.mkdir(name)

	# generate types.py
        gen_types(name,tp.game_type,parameters)

	# generate argvs.txt
	if 'argv_template' in dir(tp):
		gen_argvs(name,tp.argv_template,tuple)
	else:
		gen_argvs(name,'',tuple)
		

	# generate shell questions
	if tp.game_type == 'shell':
		parse_shell_code(tp.code,name,tuple)
		return

	# generate display.txt and execute
	compiler = 'gcc'
	suffix = 'c'
	if '-cpp' in sys.argv:
		compiler = 'g++'
		suffix = 'cpp'
	faulty = None
	targets = None
	target_values = None
        display = open(os.path.join(name,'display.txt'),'w')
	run = open(os.path.join(name,'execute.'+suffix),'w')
	if tp.game_type == 'find_the_failure':
		faulty = open(os.path.join(name,'faulty.'+suffix),'w')
	if tp.game_type == 'bullseye' or tp.game_type == 'liar_liar':
		targets = tuple['targets']
		target_values = tuple['target_values']
        parse_global(tp.global_code_template,display,run,faulty,tuple,
	 parameters,tp.game_type,targets,target_values)
        parse_main(tp.main_code_template,display,run,faulty,tuple,
	 parameters,tp.game_type,targets,target_values)
        display.close()
        run.close()
        os.system(compiler+' -o '+name+'/execute '+name+'/execute.'+suffix)

	# generate faulty
	if tp.game_type == 'find_the_failure':
		faulty.close()
		os.system(compiler+' -o '+name+'/faulty '+name+'/faulty.'+\
		 suffix)

	# generate stdin.txt
	if tp.game_type != 'shell':
		stdin = open(os.path.join(name,'stdin.txt'),'w')
		gen_template(stdin,tp.stdin_template,tuple,'stdin')
		stdin.close()


# check the number of command line arguments
if len(sys.argv) != 3 and len(sys.argv) != 4:
	print 'Usage: gen_lib.py <template> <codelib> [-cpp]'
	print 'gen_lib will create questions based on template and put them\
	 into codelib'
	sys.exit()

# create dir codelib if not exists
base_dir = os.path.abspath(sys.argv[2])
if not os.path.exists(base_dir):
	os.mkdir(base_dir)

# load question template as a python module
tl = __import__(sys.argv[1].replace('.py',''))
(parameters,tuples) = tuple_converter.convert_tuples(tl)

question_prefix = ''
# create each question based on game_type
for tuple in tuples:
	# determine the question directory name
	if tuple['prefix'] != question_prefix:
		question_prefix = tuple['prefix']
		i = 0
	else:
		i += 1
	question_dir = os.path.join(base_dir,question_prefix+str(i))
	# create question files
	create_question(question_dir,tl,tuple,parameters)

	if tl.game_type == 'input_output':
		# generate stdout.txt
		stdout = open(os.path.join(base_dir,question_dir,
			'stdout.txt'),'w')
		gen_template(stdout,tl.stdout_template,tuple,'stdout')
		stdout.close()
	print 'finished creating '+question_dir
