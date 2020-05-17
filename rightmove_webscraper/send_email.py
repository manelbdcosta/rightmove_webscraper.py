from rightmove_webscraper.static.email_credentials import SENDER_EMAIL_ADDRESS, PASSWORD
from rightmove_webscraper.static.receivers import LIST_OF_RECEIVERS
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   

def send_email(path_to_csv, filename):

    for toaddr in LIST_OF_RECEIVERS:
            
        # instance of MIMEMultipart 
        msg = MIMEMultipart() 
        
        # storing the senders email address   
        msg['From'] = SENDER_EMAIL_ADDRESS 
        
        # storing the receivers email address  
        msg['To'] = toaddr 
        
        # storing the subject  
        msg['Subject'] = "Subject of the Mail"
        
        # string to store the body of the mail 
        body = "Body_of_the_mail"
        
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 
        
        # open the file to be sent  
        attachment = open(path_to_csv, "rb") 
        
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
        
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
        
        # encode into base64 
        encoders.encode_base64(p) 
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
        
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login(SENDER_EMAIL_ADDRESS, PASSWORD) 
        
        # Converts the Multipart msg into a string 
        text = msg.as_string() 
        
        # sending the mail 
        s.sendmail(SENDER_EMAIL_ADDRESS, toaddr, text) 
        
        # terminating the session 
        s.quit() 