import smtplib, ssl
import secretsEmail

smtp_server = "smtp.gmail.com"
port = 587  

sender_email = "sarvasva_g@cs.iitr.ac.in"
password = secretsEmail.password

context = ssl.create_default_context()

message = '''\
Subject: Summarix
from: Form submitted successfully

Your form has been successfully submitted.
Thank you.
'''
def transfer(email):
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) 
        server.login(sender_email, password)
        server.sendmail(sender_email,email,message)
    except Exception as e:
        print(e)
    finally:
        server.quit()