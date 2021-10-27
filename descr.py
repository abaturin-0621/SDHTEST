import json
import requests
from random import choice
from string import ascii_uppercase,ascii_lowercase


def get_valid_string(size=5):
    return ''.join(choice(ascii_lowercase) for i in range(size))


DTRING=get_valid_string(50)   

# URL="http://1.1.0.169:8080/api"
# ERR_INVALID_RESPONSE="Invalid response"
# PATH="delivery"
# METHOD="PUT"

# headers={'Content-Type': 'application/json'}
# body={
# "name": "test_name",
# "interval": "test_interval"
# }
# url=f"{URL}/schedule/"
# response = requests.request(method="POST",url=url,headers=headers,json=body)
# print(response.status_code)

f,g=5,6