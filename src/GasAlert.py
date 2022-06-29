# This is the GasAlert app to create and send alerts when gas price alert for GTA is issued in twitter

import os
import sys
from datetime import date, datetime
from emailClient import sendEmail
from twitterRequest import requestTwitter
from emailClient import sendEmail

def findTodaysUpdate(tweets):
    isUpdatedToday = False
    emailContent = {
        "title": "GasAlert: ",
        "message": ""
    }
    firstTweet = tweets["data"][0]
    print("[DEBUG] First tweet is: ", firstTweet)
    createdAt = firstTweet["created_at"]
    tweet = firstTweet["text"]
    tweet = tweet[:tweet.find("\n")]
    isoCreatedAt = date.fromisoformat(createdAt[:createdAt.find("T")])
    today = date.today()

    if isoCreatedAt == today:
        if tweet.find("increase") != -1:
            emailContent["title"] += tweet[0:1] + " Gas price increase @" + str(today)
            emailContent["message"] = tweet
            isUpdatedToday = True
        elif tweet.find("drop") != -1:
            emailContent["title"] += tweet[0:1] + " Gas price drop @" + str(today)
            emailContent["message"] = tweet
            isUpdatedToday = True

    return isUpdatedToday, emailContent

try:
    twitterRes = requestTwitter()
    # print('[DEBUG] Get response from calling twitterRequest: ', twitterRes)
    isUpdatedToday, emailContent = findTodaysUpdate(twitterRes)
    if isUpdatedToday:
        print("[INFO] Gas price changed, sending email")
        sendEmail(emailContent)
except:
    print("[ERROR] Calling module exception", sys.exc_info())