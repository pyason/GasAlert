#Use redmail and ms outlook account to send email
import os
import sys
from dotenv import load_dotenv

from redmail import gmail

def sendEmail():
    load_dotenv()
    pwd = os.getenv('GMAIL_APP_PWD')

    gmail.username = 'imaurmuthr@gmail.com'
    gmail.password = pwd

    try:
        # Send to mail!
        gmail.send(
            subject="Test email from ima gmail from GasAlert",
            receivers=['paul.yason@gmail.com'],
            text="Yo, this is sent from a new gmail account!"
        )
        print("[INFO] Email sent successful")
    except:
        print("[ERROR] Error while trying to send email: ", sys.exc_info())