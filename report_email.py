#!/usr/bin/env python3

import os, datetime
import reports
import emails
from datetime import date

date = date.today()
today_date = date.strftime("%B, %d, %Y")

def pdf_data(path):
  #generate a pdf of fruitdata
  pdf_data = "" 
  path_file = os.listdir(path)
  for file in path_file:
    if file.endswith('.txt'):
      with open(path+file, "r") as text:
        data = text.readlines()
        name = data[0].strip()
        weight = data[1].strip()
        pdf_data += "name: " + name + "<br/>" + "weight: " + weight + "<br/>" + "<br/>"
        print(pdf_data)
  return pdf_data
  

if __name__ == "__main__":
  path = "suppliers-data/descriptions/"
  generated_pdf = pdf_data(path)
  
  title = "Processed Update on " + today_date
  print(title) 
  #generate a report of pdf of fruit data for attachment
  # calling generate_report method from reports
  reports.generate_report("/mnt/c/users/sowmya/pythonscripts/Automation/processed.pdf", title, generated_pdf)

  #generate email
  sender = "sowmyamaguluri@gmail.com"
  recipent = "sowmyamaguluri@gmail.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/mnt/c/users/sowmya/pythonscripts/Automation/processed.pdf"
  
  message = emails.generate_email(sender,recipent,subject,body,attachment)
  emails.send_email(message)


