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
        headers = {"Authorization": "Bearer " + bearer_token}
        r = requests.get(url, headers=headers)
        statCode = r.status_code
        jsonRes = r.json()

        if statCode >= 200 and statCode < 299 and not("errors" in jsonRes):
            print('Get tweet details successful')
            # print(jsonRes["data"][0]["text"][:1])
            return jsonRes
        else: print("Twitter API returned " + str(statCode) + " error: ", r.text)
    except ConnectionError as err:
        print("Twitter API Connection error: ", err)
    except:
        print("Other Twitter API error occurred: ", sys.exc_info())