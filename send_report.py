import base64
import sys
import os
from os import listdir
from os.path import isfile,join
from pprint import pprint
import requests
import json


# PATH="C:/Users/colvir_user/Desktop/25.10/tests/SDH/API/delivery"
# os.system(f'C:/Users/colvir_user/anaconda3/python.exe python  pytest -rxXspP  {PATH}   --alluredir=reports')
result={
  "results": []
}
PROJECT="sdh-api-local"
ROOT_DIR='reports'
URL_ALLURE="http://1.1.5.62:5050"
filepath = f"{ROOT_DIR}"
for f in listdir(filepath):
    path=join(filepath, f)
    if  isfile(path):
        with open(path, 'rb') as filejson:
           data = filejson.read()
           enc=base64.encodebytes(data)
           result["results"].append({"file_name": f,"content_base64": enc.decode("utf-8")})
url=f"{URL_ALLURE}/allure-docker-service/send-results?project_id={PROJECT}&force_project_creation=true"
data=json.dumps(result)
headers={'Content-Type': 'application/json'}
response = requests.request(method="POST",url=url, headers=headers ,data=data)
pprint(response.status_code)           
if response.ok:
  url=f"{URL_ALLURE}/allure-docker-service/generate-report?project_id={PROJECT}"
  response = requests.request(method="GET",url=url )  
  pprint(response.status_code) 
  if response.ok:
    for f in listdir(filepath):
        path=join(filepath, f)
        os.remove(path)

        