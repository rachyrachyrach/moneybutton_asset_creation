#!/usr/bin/env python3
import os
import requests
import base64

client_id = os.environ.get('CLIENT_ID')# insert Moneybutton client id by export CLIENT_ID local file
client_secret = os.environ.get('CLIENT_SECRET')# insert MB client secret by using export CLIENT_SECRET local file

#Getting access token

cred64 = base64.b64encode(client_id.encode() + b":" + client_secret.encode())


response = requests.post(
    'https://www.moneybutton.com/oauth/v1/token',
    headers={'content-type': 'application/x-www-form-urlencoded',
             'Authorization': b'Basic ' + cred64},
    data={'grant_type' : 'client_credentials',
          'scope' : 'application_access:write'}
)
resp_json = response.json()
access_token = resp_json["access_token"]
print(access_token)

#Creating asset
response = requests.post(
    'https://www.moneybutton.com/api/v2/me/assets',
    headers={'Authorization': 'Bearer ' + access_token},
    data={
        "protocol": "SFP",
        "name": "Molly Match Token",
        "initialSupply": 1000000,
        "description": "This is for the GitHub repository on asset creation using Python.",
        "avatar": "https://github.com/rachyrachyrach/moneybutton_asset_creation/blob/master/docs/images/mollymatch_paw.png",
        "url": "https://github.com/rachyrachyrach/moneybutton_asset_creation"})

resp_json = response.json()
print(resp_json)