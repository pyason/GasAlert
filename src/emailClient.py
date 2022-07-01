## This module Use redmail and gmail account to send email

import os
import sys
from dotenv import load_dotenv
import logger

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
        logger.info("Email sent successful")
    except:
        logger.error("Error while trying to send email: ", sys.exc_info())
        raise Exception(sys.exc_info())