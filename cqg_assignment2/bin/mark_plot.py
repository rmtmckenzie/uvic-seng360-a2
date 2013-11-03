#!/usr/bin/python

import os
import sys
sys.path.append('./codeAct')
import log_analysis

def create_plot(login_mark_dict,quiz_name):
	'''
	Purpose
		Create the following files by using login_mark_dict:
			quiz_name_mark.txt:	a quiz mark summary
			quiz_name_mark.p:	a R script
			quiz_name_mark.pdf:	a quiz mark plot
	Precondition
		login_mark_dict is a dictionary where the keys are logins and
		 the values are quiz marks.
		quiz_name is a string.
	'''
	# create data file
	data_file = quiz_name + '_mark.txt'
	file_handle = open(data_file,'w')
	file_handle.write('login\tmark\n')
	for login in sorted( login_mark_dict.keys() ):
		file_handle.write('%s\t%d\n' % (login,login_mark_dict[login]))
	file_handle.close()

	# calculate mean quiz mark
	mean_mark = 0.0
	for mark in login_mark_dict.values():
		mean_mark += float(mark) / float( len(login_mark_dict.keys()) )

	# calculate max quiz mark
	max_quiz_mark = log_analysis.get_max_quiz_mark(quiz_name)

	# prepare script
	plot_file = quiz_name + '_mark.pdf'
	script = '''
r=read.table("%s",sep="\t",header=TRUE)

pdf(file="%s")

hist(r$mark,breaks=c(seq(0,%d,1)),col="red",
 main=NULL,xlab="Question Mark (Mean = %.2f)",ylab="Number of Students")

dev.off()
'''
	script = script % (data_file,plot_file,max_quiz_mark,mean_mark)

	# create script file
	script_file = quiz_name + '_mark.r'
	file_handle = open(script_file,'w')
	file_handle.write(script)
	file_handle.close()

	# run gnuplot on script file
	os.system('R CMD BATCH ' + script_file)

	# clean data and script files
	os.system('rm -f ' + data_file)
	os.system('rm -f ' + script_file)
	os.system('rm -f ' + script_file + '.Rout')

if __name__ == '__main__':
	# check number of command arguments
	if len(sys.argv) != 2:
		print 'Usage: ./mark_plot.py <quiz_dir>'
		sys.exit(-1)

	# create path to quiz dir
	quiz_dir = sys.argv[1]

	# exit if quiz dir doesn't exist
	if not os.path.exists(quiz_dir):
		print "Quiz dir '" + quiz_dir + "' not exist"
		sys.exit(-1)

	# get login to quiz mark dictionary
	login_mark_dict = log_analysis.get_login_mark_dict(quiz_dir)

	# extract quiz name from quiz dir
	dirs = quiz_dir.split('/')
	dirs.reverse()
	for dir in dirs:
		if dir != '':
			quiz_name = dir
			break

	# generate plot
	create_plot(login_mark_dict,quiz_name)
