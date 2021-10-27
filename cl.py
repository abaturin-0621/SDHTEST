import json
import requests
from random import choice
from string import ascii_uppercase,ascii_lowercase


def get_valid_string(size=5):
    return ''.join(choice(ascii_lowercase) for i in range(size))


DTRING=get_valid_string(5)   

URL="http://1.1.0.169:8080/api"
ERR_INVALID_RESPONSE="Invalid response"
PATH="delivery"
METHOD="PUT"
id=3
url=f"{URL}/{PATH}/{id}/"
headers={'Content-Type': 'application/json'}
body={"name": "biqbobjpqhocvobsmpbxvadlfodpdepkefongcxq",
 "dag_id": "sfsfsf",
 "description":DTRING,
  "route": 10,
  "schedle": "sgsgsgsg", 
  "shipment": 6}
response = requests.request(method=METHOD,url=url, headers=headers ,json=body)

# print (response.text)
print (response.status_code)

