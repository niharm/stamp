################################################
# stamp.py
# Nihar Madhavan
# November 2013
#
# Searches specified folder in email. When 
# new email is found in folder, runs function on 
# email and then sends email. 
#
################################################
# UPDATE THESE VARIABLES

# Account Info
gmail_user = "me@domain.com"
gmail_pwd = "password"

# Who to send the email to (must be a list)
TO = ['recipient@domain.com, other_recipient@domain.com'] 
SUBJECT = "Subject of email!"

# Folder in email to search in
folder = 'email_folder'

################################################

import cmd, getpass, webbrowser
import re
import urllib
from bs4 import BeautifulSoup
from pygmail import *
import smtplib

#logs into email    
def do_login():
    
    emails = ['']
    
    self.accounts = []

    print "Authenticating account..."
    
    g = pygmail()

    g.login(email,password)
    self.accounts.append(g)
    
    print "Done"

    return g


# return first message
def get_message(g):
        
    messages = g.fetchUnreadMessages(folder)

    if len(messages) > 0:
        return messages[0]

    else :
        return "none"

# sends email using SMTP
def sendemail(text):
    TEXT = text
    FROM = gmail_user
  
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
  
    try:
       #server = smtplib.SMTP(SERVER) 
       server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
       server.ehlo()
       server.starttls()
       server.login(gmail_user, gmail_pwd)
       server.sendmail(FROM, TO, message)
       #server.quit()
       server.close()
       print 'successfully sent the mail'
    except:
       print "failed to send mail"
  
# writes email to be sent based on message
def write_email(msg):

    # example -- get sender
    msgFromArray = email.utils.parseaddr(msg['From'])
    email body = "Hi" + sender + ",\n"
    email_body += "\n Here is my message!"
    email_body += "\nLove, \nNihar"
    return email_body


#####################
# START OF PROGRAM
#####################

#login
g = do_login()

#check for unread message in folder
msg = get_message(g)

# keep count
count = 1

# repeat while there are no links
while links == "none":
    msg = get_message(g)
    print "Checked " + str(count) + " times"
    count += 1

# if there is a message, write and send email
email_body = write_email(msg)
sendemail(email_body);

print("All done!")