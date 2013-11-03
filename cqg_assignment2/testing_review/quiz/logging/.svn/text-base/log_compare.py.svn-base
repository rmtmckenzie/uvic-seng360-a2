#!/usr/bin/python

import sys
import os
import re

#change to testing/logging directory
logtestdir = os.path.split(sys.argv[0])[0]
os.chdir(logtestdir)

diff = os.popen("diff gold_log.xml ../../../quiz_log/cqg_tester.xml | grep '^[<>]'").readlines()

for line in diff:
	m = re.search("<time>(.*)</time>",line)
	if m and int(m.group(1)) > 3:
		print "Logfile diff fails; time field value too large"
		exit()
	elif m: #minor variations in time are OK
		pass
	else:
		print "Logfile diff fails; run"
		goldfile = os.path.relpath(
			os.path.join(logtestdir,"gold_log.xml"))
		logfile = os.path.relpath(
			os.path.join(logtestdir,"../../../quiz_log/cqg_tester.xml"))
		print "   vimdiff '"+goldfile+"' '"+logfile+"'"
		print "to see differences."
		exit()
