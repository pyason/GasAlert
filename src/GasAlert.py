# This is the GasAlert app to create and send alerts when gas price alert for GTA is issued in twitter

from twitterRequest import requestTwitter
import os
import sys

try:
    twitterRes = requestTwitter()
    print('Get back from calling twitterRequest', twitterRes)
except:
    print("Calling module exception")