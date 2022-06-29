## This module Use redmail and gmail account to send email

import os
import sys
from dotenv import load_dotenv

from redmail import gmail

def sendEmail(emailContent):
    load_dotenv()
    pwd = os.getenv('GMAIL_APP_PWD')

    gmail.username = 'imaurmuthr@gmail.com'
    gmail.password = pwd

    try:
        # Send to mail!
        gmail.send(
            subject=emailContent["title"],
            receivers=['paul.yason@gmail.com'],
            text=emailContent["message"]
        )
        print("[INFO] Email sent successful")
    except:
        print("[ERROR] Error while trying to send email: ", sys.exc_info())