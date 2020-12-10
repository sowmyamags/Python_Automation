#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes 
import smtplib
import os.path
import getpass

def generate_email(sender,recipent,subject,body,attachment_path = None):
#  print(sender,recipent,subject, body, attachment_path)

  message = EmailMessage()
  message['From'] = sender
  message['To'] = recipent
  message['Subject'] = subject
  message.set_content(body)
  
  if attachment_path != None:
    attachment_filename = os.path.basename(attachment_path) 
    mime_type, _ =  mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(),
                            maintype = mime_type, 
                            subtype=mime_subtype,
                            filename=attachment_filename)
  return message

def send_email(message_pdf):
  mail_server = smtplib.SMTP('localhost')

#  mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
#  mail_server.set_debuglevel(1)
#  mail_pass = getpass.getpass('Password? ')
#  mail_server.login(sender, mail_pass)

  mail_server.send_message(message_pdf)
  mail_server.quit()


    

