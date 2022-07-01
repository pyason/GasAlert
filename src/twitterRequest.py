## This module makes Twitter API request to the @GTAhasgas and extracts its tweets

import os
from dotenv import load_dotenv
import sys
import requests
import logger

def requestTwitter():

    load_dotenv()

    bearer_token=os.getenv('BEARER_TOKEN')

    url="https://api.twitter.com/2/users/317436248/tweets?tweet.fields=created_at,text"

    try:
        logger.info("Start getting tweets")
        headers = {"Authorization": "Bearer " + bearer_token}
        r = requests.get(url, headers=headers)
        statCode = r.status_code
        jsonRes = r.json()

        if statCode >= 200 and statCode < 299 and not("errors" in jsonRes):
            logger.info('Get tweet details successful')
            return jsonRes
        else: 
            logger.debug("Non 2XX response received: ", r.text)
            r.raise_for_status()
    except ConnectionError as err:
        logger.error("Twitter API Connection error: ", err)
        raise Exception(err)
    except:
        logger.error("Error while calling Twitter API: ", sys.exc_info())
        raise Exception(sys.exc_info())