#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails


def report_email(error):
  #generate an email if CPU USage is over  80%
  print(error)
  sender = ""
  recipent = ""
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  mail = emails.generate_email(sender,recipent,subject,body)
  emails.send_email(mail)

#check CPU usage not over 80%

cpu_usage = psutil.cpu_percent()
print("1", cpu_usage)
if cpu_usage > 80:
  report_email("Error - CPU usage is over 80%")

#Check Disk Space not lower than 20%
disk_usage = shutil.disk_usage("/")
disk_space = disk_usage.free / disk_usage.total * 100
print("2", disk_usage)
if disk_space > 80:
  report_email("Error - Available disk space is less than 20%")

#Check Available memory is less than 500MB
memory = psutil.virtual_memory()
print(memory)
THRESHOLD = 500 * 1024 * 1024 #500MB
if memory.available <= THRESHOLD:
  report_email("Error - Available memory is less than 500MB")

# Check hostname "local_host" 

host_name = socket.gethostbyname('localhost')
if host_name != "127.0.0.1":
  report_email("Error - localhost cannot be resolved to 127.0.0.1")
