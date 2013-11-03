import os
import datetime

def write(message):
	file_handle = open('cqg_errors.log','a')
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	file_handle.write("["+timestamp+"] "+message+"\n")
	file_handle.close()
