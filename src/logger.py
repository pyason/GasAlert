# Logging level: 0 = ERROR, 1 = INFO, 2 = DEBUG
import os

try:
    logLevel = os.environ['LOG_LEVEL']
except:
    logLevel = 2
print(logLevel)

def error(msg, trace):
    print("[ERROR]", msg, trace)

def info(msg):
    if logLevel > 0:
        print("[INFO]", msg)

def debug(msg, log):
    if logLevel > 1:
        print("[DEBUG]", msg, log)