# Logging level: 0 = ERROR, 1 = INFO, 2 = DEBUG, 3 = VERBOSE_DEBUG
import os

try:
    logLevel = int(os.environ['LOG_LEVEL'])
except:
    logLevel = 2
print("[INFO] LOG_LEVEL is: ", logLevel)

def error(msg, trace):
    print("[ERROR]", msg, trace)

def info(msg):
    if logLevel > 0:
        print("[INFO]", msg)

def debug(msg, log):
    if logLevel > 1:
        print("[DEBUG]", msg, log)

# This is used for most verbose debug settings, e.g. when you want to log detail steps or whole payload/error
def verboseDebug(msg, log, moreLog = ""):
    if logLevel > 2:
        print("[DEBUG]", msg, log, moreLog)