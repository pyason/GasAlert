# This is the GasAlert app to create and send alerts when gas price alert for GTA is issued in twitter

import sys
from datetime import date, timedelta
from emailClient import sendEmail
from twitterRequest import requestTwitter
from emailClient import sendEmail
import logger

def findTodaysUpdate(tweets, eventTime):
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

    # Processing event and tweet's timestamps
    eventTimeTIndex = eventTime.find("T")
    createdAtTIndex = createdAt.find("T")
    eventTimeHour = int(eventTime[eventTimeTIndex+1:eventTimeTIndex+3])
    createdAtHour = int(createdAt[createdAtTIndex+1:createdAtTIndex+3])
    isoCreatedAt = date.fromisoformat(createdAt[:createdAtTIndex])
    today = date.today()

    if isoCreatedAt == today and (eventTimeHour <= 16 or createdAtHour > 16):
        logger.verboseDebug("Time conditions met, inside extracting tweet", "")
        if tweet.find("increase") != -1:
            emailContent["title"] += tweet[0:1] + " Gas price increase @" + str(today + timedelta(days=1))
            emailContent["message"] = tweet
            isUpdatedToday = True
        elif tweet.find("drop") != -1:
            emailContent["title"] += tweet[0:1] + " Gas price drop @" + str(today + timedelta(days=1))
            emailContent["message"] = tweet
            isUpdatedToday = True

    return isUpdatedToday, emailContent

def lambda_handler(event, context):
    logger.info("Event handler received event")
    logger.verboseDebug("Event received: ", event)
    try:
        eventTime = event["time"]
        logger.debug("Event time: ", eventTime)
        twitterRes = requestTwitter()
        logger.verboseDebug("Get response from calling twitterRequest: ", twitterRes)
        isUpdatedToday, emailContent = findTodaysUpdate(twitterRes, eventTime)
        if isUpdatedToday:
            logger.info("Gas price changed, sending email")
            sendEmail(emailContent)
        else: logger.info("No change or no tweeter update in today's gas price")
    except:
        logger.error("Calling module exception: ", sys.exc_info())