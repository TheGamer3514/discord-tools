#Check If Installed
try: 
    import os
    import requests  
except ImportError: 
    print("Requests Not Found...\nInstalling...")
    os.system("pip install requests")
    print("Requests Installed")
#import
import random
import string
import time
import os
import requests
import json
#load config
with open('config/autosend.json') as f:
  data = json.load(f)
  for c in data['Config']:
        print('Loading...')
web = c['web'] #modify this in config/nitrogen.json
print("Gen Started. Enjoy!")
#gen codes
def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(19))

class Generator:
    def __init__(self):
        self.codes = []
        self.check()

    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if data["message"] == 'Unknown Gift Code':
                print("Invalid: " + code)
            elif data["message"] == 'The resource is being rate limited.' or 'You are being rate limited.':
                print('Rate Limited: ' + code)
                print('Waiting For Rate Limit To Go Away...')
                print(data)
                time.sleep(int(data['retry_after'])/1000)
            else:
                print("Working: " + code)
                file = open("workedcodes.txt", "a+")
                file.write("\n" + code)
#Keep Alive
if web == "True" or web == "true":
    from keepalive import keep_alive
    keep_alive()
else:
    print("Web Server Disabled")
Generator()