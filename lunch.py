import os
import sys
import requests
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

SLACK_URL_PROFILE = "https://slack.com/api/users.profile.set"
TOKENS = [
    #os.getenv("TOKEN_1"),
    #os.getenv("TOKEN_2"),
    os.getenv("TOKEN_3")
]

def set_profile_status(text, icon_text, minutes):
    if minutes == 0:
        expiration_sec = 0
    else:
        expiration_dt = datetime.now() - timedelta(minutes = minutes)
        expiration_sec = int(time.mktime(expiration_dt.timetuple()))

    for token in TOKENS:
        headers = {
            "Authorization": "Bearer {}".format(token)
        }

        data = {
            "profile": {
                "status_text": text,
                "status_emoji": icon_text,
                "status_expiration": expiration_sec
            }
        }
        
        r = requests.post(SLACK_URL_PROFILE, headers=headers, json=data)
        print('-----------------------------------------------')
        print(r.text)
    
def start_lunch():
    set_profile_status("almorzando", ":pizza:", 60)

def finish_lunch():
    set_profile_status("", "", 0)

if len(sys.argv) <= 1:
    start_lunch()
elif sys.argv[1] == "start":
    start_lunch()
elif sys.argv[1] == "finish":
    finish_lunch()
else:
    print("Invalid argument!!")
