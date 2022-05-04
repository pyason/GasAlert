# This is the GasAlert app to create and send alerts when gas price alert for GTA is issued in twitter

import time
import requests

bearer_token=""

url="https://api.twitter.com/2/users/317436248/tweets?tweet.fields=created_at,text"

try:
    headers = {"Authorization": "Bearer " + bearer_token}
    r = requests.get(url, headers=headers)
    jsonRes = r.json()
    print(jsonRes)
except ConnectionError as err:
    print("Connection error:", err)
except:
    print("Other requests error occurred")