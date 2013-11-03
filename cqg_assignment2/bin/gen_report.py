#!/usr/bin/python

'''
command line args
1. login_list
2. quiz_spec
3. log_dir
'''

import sys
import os

# check command line args
if len(sys.argv) != 4:
	print 'Usage: '+sys.argv[0]+' LOGIN_LIST QUIZ_SPEC LOG_DIR'
	sys.exit(-1)

# import quiz_spec
path = os.path.split(sys.argv[2])
if path[0] != '':
	sys.path.append(path[0])
try:
	spec = __import__(path[1].replace('.py',''))
except:
	print 'Can not import '+sys.argv[2]
	sys.exit(-2)

# check if log_dir exists
if not os.path.isdir(sys.argv[3]):
	print sys.argv[3]+' does not exist'
	sys.exit(-3)

# generate the output data file in csv format
# get all logins form input
fpin = open(sys.argv[1],'r')
inputs = fpin.readlines()
fpin.close()
# init temp file
temp = 'question_let_mark.csv'
fpout = open(temp,'w')
for line in inputs:
	fpout.write(line)
fpout.close()

# remember quesiton_let and count and calculate total_mark
total_mark = 0
question_lets = {}
for q in spec.question_list:
	question_lets[q[2][0]] = q[1]
	total_mark += q[1]*q[0]
# get mark for each question_let
L = question_lets.keys()
for q in L:
	cmd = 'python extract_quiz_mark.py '+sys.argv[3]+' '+q+' '+\
	 temp+' '+temp+' '+str(question_lets[q])
	os.system(cmd)

# open and load question_let_mark.csv
fpin = open(temp,'r')
lines = fpin.readlines()
fpin.close()
inputs = []
for line in lines:
	inputs.append(line.strip().split(','))

# generate data file for ploting
output = 'qlet_mark.csv'
fpout = open(output,'w')
for k in L:
	total = 0
	correct = 0
	index = L.index(k)
	for s in inputs:
		total += question_lets[k]
		correct += int(s[index*2+3])
	rate = round(float(correct)/float(total),2)
	fpout.write(k+'\t,'+str(rate)+'\n')
fpout.close()

# delete temp file
os.system('rm -f question_let_mark.csv')

# plot the question let distribution
print 'ploting question_let mark distribution'
rscript = '''\
#!/usr/bin/Rscript
args <- commandArgs(trailingOnly = TRUE)

data<-read.csv(file=args[1],sep=",",head=FALSE)
postscript(file=args[2])

barplot(data$V2,main="question cluster correct rate", xlab="Question clusters",
ylab="Correct rate",density=c($DENSITY),ylim=c(0,1.3),legend.text=TRUE)
legend("topright",c($XLABELS),density=c($DENSITY))
'''
# replace the $XLABELS
xlabels = ''
for k in L:
	xlabels += '"'+k+'",'
rscript = rscript.replace('$XLABELS',xlabels[:-1])
# replace the $DENSITY
den = ''
for i in range(len(L)):
	den += str((i+1)*7)+','
rscript = rscript.replace('$DENSITY',den[:-1])

rs = open('barchart.r','w')
rs.write(rscript)
rs.close()
cmd = 'chmod +x barchart.r'
os.system(cmd)
cmd = './barchart.r qlet_mark.csv qlet.eps'
os.system(cmd)
print 'question_let correct ratio is plotted in qlet.eps'

# total mark
cmd = './mark_connex.py '+sys.argv[1]+' '+sys.argv[3]+' > grades.csv'
os.system(cmd)
print 'total mark in calculated in grades.csv'

# plot total mark distribution
cmd = './distribution.r grades.csv 3 total_mark_dist.eps '+str(total_mark+5)+\
' "Total quiz mark distribution" mark'
print cmd
os.system(cmd)
print 'total mark distribution is plotted in total_mark_dist.eps'

