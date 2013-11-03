import sys
import os
import subprocess

preconditions = '''
Preconditions:

- The web2py directory is in stock form, i.e.,
  it is the result of 'unzip web2py_src.zip' where
  web2py_src.zip was downloaded from http://web2py.com/

- The web2py directory is version 1.95.1, extracted from
  web2py_src.zip with md5sum c213d8aab32a3faa01c409fecb7dea81
'''

if len(sys.argv) != 2:
	print "Usage: python "+sys.argv[0]+" /path/to/web2py"
	exit()

#canonicalize full path to the web2py dir argument
srcdir = os.path.realpath(sys.argv[1])

#change to cqg base dir
basedir = os.path.dirname(sys.argv[0])
if len(basedir):
	os.chdir(basedir)

if not (
		os.path.isdir(srcdir) and
		os.access(srcdir,os.R_OK) and
		os.access(srcdir,os.X_OK)
	):
	print "Cannot read specified web2py source directory."
	print preconditions
	exit()

if not os.access(os.path.join(srcdir,"web2py.py"),os.R_OK):
	print srcdir+"\ndoes not look like a web2py source directory."
	exit()

# FIXME: I have not found a practical, portable way to perfectly escape
# arguments to a shell command from python, and still preserve the ability
# to glob filenames. But who uses " in filenames? This should be fine.
if '"' in srcdir:
	print 'Path to web2py directory cannot contain double quote (") chars, sorry.'
	exit()

if not os.path.isdir("web2py/applications/cqg"):
	print "Cannot extract here; cqg base directory doesn't look right."
	print "(Try re-extracting cqg base, cd into it, then run "+os.path.split(sys.argv[0])[1]+")"
	print preconditions
	exit()

subprocess.call('cp -an "'+srcdir+'"/* "web2py/"',shell=True)

done_message = '''

All done.

To populate the question library:
bash "BASEDIRbin/generate_all.sh"

To generate the test suites:
python "BASEDIRtesting_review/code_activator/generate_tests.py"

To start the cqg server:
bash "BASEDIRweb2py/start.sh"

To see the cqg splash page, visit:
http://localhost:8080/cqg

'''

print done_message.replace("BASEDIR",os.path.join(basedir,""))
