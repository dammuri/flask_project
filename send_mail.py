import smtplib
from email.mime.text import MIMEText

def send_mail(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '04e95ee69bc9e4'
    passwd = 'bda6d90a431ebf'
    message =f"<h3> New Submission</h3><ul><li>customer : {customer}</li><li>dealer: {dealer}</li><li>rating : {rating}</li><li>commets :{comments}</li></ul>"
    
    sender_mail ="email1@example.com"
    receiver_mail = 'email2@example.com'
    message_mail = MIMEText(message,'html')
    message_mail['Subject'] = 'Feedback Car Dealer'
    message_mail['From'] = sender_mail
    message_mail['To'] = receiver_mail

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login,passwd)
        server.sendmail(sender_mail,receiver_mail,message_mail.as_string())