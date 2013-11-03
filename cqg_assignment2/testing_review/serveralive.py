import os

#who should get warning e-mails
recipients = ['Felix <niteling@uvic.ca>','niteling@csc.uvic.ca']
#recipients = ['niteling@uvic.ca','luming@uvic.ca','dhoffman@cs.uvic.ca']

#try twice to fetch min_io_alone quiz with 1.5 second timeout
#and look for the text 'printf' in the response (should be present
#regardless of any formatting changes we make)
result = os.popen("wget -q --tries=2 --timeout=1.5 -O - 'http://localhost:8080/cqg/quiz?spec=c_min_io_alone' | grep printf").readlines()
if len(result):
	#everything is fine
	exit()

#otherwise, send e-mail:

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Create a text/plain message
msg = MIMEText("CQG failed to display the min_io_alone quiz; please check on it.")

msg['From'] = 'Graffiti CQG Server <noreply@graffiti.cs.uvic.ca>'
msg['Reply-To'] = 'Felix <niteling@uvic.ca>'
msg['To'] = ", ".join(recipients)
msg['Subject'] = 'Graffiti: CQG server is down'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.uvic.ca')
s.sendmail(msg['From'], recipients, msg.as_string())
s.quit()
