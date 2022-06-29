## This module makes Twitter API request to the @GTAhasgas and extracts its tweets

import os
from dotenv import load_dotenv
import sys
import requests

def requestTwitter():

    load_dotenv()

    bearer_token=os.getenv('BEARER_TOKEN')

    url="https://api.twitter.com/2/users/317436248/tweets?tweet.fields=created_at,text"

    try:
        print("[INFO] Start getting tweets")
        headers = {"Authorization": "Bearer " + bearer_token}
        r = requests.get(url, headers=headers)
        statCode = r.status_code
        jsonRes = r.json()

        if statCode >= 200 and statCode < 299 and not("errors" in jsonRes):
            print('[INFO] Get tweet details successful')
            return jsonRes
        else: 
            print("[DEBUG] Non 2XX response received: ", r.text)
            r.raise_for_status()
    except ConnectionError as err:
        print("[ERROR] Twitter API Connection error: ", err)
    except:
        print("[ERROR] Error while calling Twitter API: ", sys.exc_info())