from datetime import datetime
import smtplib

print("Hello, here is the time: "+str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))


gmail_user = 'agilyticdemo@gmail.com'
gmail_password = 'Rigidytic'

sent_from = gmail_user
to = ['diego.mechelynck@gmail.com']
subject = 'Airflow message'

email_text="Hello Diegoo this is airflowww"


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()
print ('Email sent!')