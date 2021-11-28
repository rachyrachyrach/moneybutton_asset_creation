#!/usr/bin/env python3
import os
import requests
import base64

client_id = os.environ.get('CLIENT_ID')# insert Moneybutton client id by export CLIENT_ID local file
client_secret = os.environ.get('CLIENT_SECRET')# insert MB client secret by using export CLIENT_SECRET local file

cred64 = base64.b64encode(client_id.encode() + b":" + client_secret.encode())

response = requests.post(
    'https://www.moneybutton.com/oauth/v1/token',
    headers={'content-type': 'application/x-www-form-urlencoded',
             'Authorization': b'Basic ' + cred64},
    data={'grant_type' : 'client_credentials',
          'scope' : 'application_access:write'}
)
resp_json = response.json()
print(resp_json["access_token"])