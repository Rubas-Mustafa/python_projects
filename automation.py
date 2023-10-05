# text builder   sending of messages
# schedule    when the message is to be sent 

import requests
import schedule
import time

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        'phone' : "03085210500",
        'message' : "Hello I am Dead!!!!",
        'key' : 'textbelt',
    })
    print(resp.json()) 

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
    
