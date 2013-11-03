import os

def write(log_dir,login,index,path,result,answer,time):
	'''
	Purpose
		Append a <question> element to log_dir/login.xml.
		A <question> element consists of index, path, result, answer,
		and time.
	Precondition
		log_dir is a valid path.
		login and path are strings.
		index and result are integers.
	'''
	# open log file for appending
	file_handle = open(os.path.join(log_dir,login+'.xml'),'a')

	# write <question> element to file
	file_handle.write('<question>\n')
	file_handle.write('\t<index>'+str(index)+'</index>\n')
	file_handle.write('\t<path>'+path+'</path>\n')
	file_handle.write('\t<result>'+str(result)+'</result>\n')
	file_handle.write('\t<answer>'+str(answer)+'</answer>\n')
	file_handle.write('\t<time>'+str(time)+'</time>\n')
	file_handle.write('</question>\n')

	# close log file
	file_handle.close()
