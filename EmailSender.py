from datetime import datetime
import smtplib
import sys

recipient=sys.argv[1]
#recipient='diego.mechelynck@gmail.com'


gmail_user = 'agilyticdemo@gmail.com'
gmail_password = 'Rigidytic'

sent_from = gmail_user
to = [recipient]
subject = 'Airflow message'

email_text="Hello folksssss"


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()
print ('Email sent!')