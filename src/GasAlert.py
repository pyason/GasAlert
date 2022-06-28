# This is the GasAlert app to create and send alerts when gas price alert for GTA is issued in twitter

import os
import sys
from datetime import date, datetime
from emailClient import sendEmail
from twitterRequest import requestTwitter
from emailClient import sendEmail

def findTodaysUpdate(tweets):
    isUpdatedToday = False
    firstTweet = tweets["data"][0]
    print("[DEBUG] First tweet is: ", firstTweet)
    createdAt = firstTweet["created_at"]
    isoCreatedAt = date.fromisoformat(createdAt[:createdAt.find("T")])
    today = date.today()

    print("Today: ", today)
    print("createdAt: ", isoCreatedAt)
    print("CreatedAt is today: ", isoCreatedAt == today)
    return isUpdatedToday, ""

try:
    twitterRes = requestTwitter()
    # print('[DEBUG] Get response from calling twitterRequest: ', twitterRes)
    isUpdatedToday, emailContent = findTodaysUpdate(twitterRes)
    # sendEmail(emailContent)
except:
    print("[ERROR] Calling module exception", sys.exc_info())