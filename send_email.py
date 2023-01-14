import smtplib
from email.mime.text import MIMEText
def send_email(email,height, average_height,count):
    smt_obj=smtplib.SMTP('smtp.gmail.com',587)
    smt_obj.ehlo()
    smt_obj.starttls()
    
    from_email='atakishizadesehruz@gmail.com'
    to_email=email
    pwd='pwofymthrcaioxxe'
    subject='Height Collector'
    message=f'Thank you {email} for request, your height is {height}. according to {count} users, average height is {average_height} cm'
    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    smt_obj.login(from_email,pwd)

    smt_obj.send_message(msg)
