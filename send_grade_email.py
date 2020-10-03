import smtplib as smt
import time


from grade_checker import *
from grade_config import *
import grade_email_config

def send_email(subject, msg):
    try: #trying to connect to gmail server
        server = smt.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(grade_email_config.EMAIL_ADDRESS, grade_email_config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(grade_email_config.EMAIL_ADDRESS, grade_email_config.EMAIL_ADDRESS_RECIPIENT, message)
        print("Email sent.")
        server.quit()
    except:
        print("Email failed to send.")


subject = "Grades Update"
msg = """Here are your grades for the following week:

{0}: {1}

{2}: {3}

{4}: {5}

{6}: {7}

{8}: {9}

{10}: {11}

{12}: {13}

{14}: {15}

""".format(grade_list[0], grade_list[1], grade_list[2], grade_list[3], grade_list[4], grade_list[5], grade_list[6], grade_list[7], grade_list[8], grade_list[9], grade_list[10], grade_list[11], grade_list[12], grade_list[13], grade_list[14], grade_list[15])


send_email(subject, msg)
