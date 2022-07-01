# This is the GasAlert app to create and send alerts when gas price alert for GTA is issued in twitter

import sys
from datetime import date
from emailClient import sendEmail
from twitterRequest import requestTwitter
from emailClient import sendEmail
import logger

def findTodaysUpdate(tweets):
    isUpdatedToday = False
    emailContent = {
        "title": "GasAlert: ",
        "message": ""
    }
    firstTweet = tweets["data"][0]
    logger.debug("First tweet is: ", firstTweet)
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


def lambda_handler(event, context):
    print("[INFO] Event handler received event")
    try:
        twitterRes = requestTwitter()
        # print('[DEBUG] Get response from calling twitterRequest: ', twitterRes)
        isUpdatedToday, emailContent = findTodaysUpdate(twitterRes)
        if isUpdatedToday:
            logger.info("Gas price changed, sending email")
            sendEmail(emailContent)
        else: logger.info("No change in today's gas price")
    except:
        logger.error("Calling module exception: ", sys.exc_info())