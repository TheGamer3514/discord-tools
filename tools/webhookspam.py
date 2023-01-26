import os
import string
import random
import time
import requests
import json
import colorama
from colorama import Fore
#load config
with open('config/webhookspam.json') as f:
  data = json.load(f)
  for c in data['Config']:
        print('Loading...')
webhook = c['webhook'] #modify this in config/webhookspam.json
message = c['message'] #modify this in config/webhookspam.json
colorama.init()
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f'Sent MSG "{msg}"')
        except:
            print(Fore.RED + "Bad Webhook : " + webhook)
            time.sleep(5)
            exit()

x = 3514
while x == 3514:
    spam(message, webhook)
