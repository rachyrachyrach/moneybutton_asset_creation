# moneybutton_asset_creation
Create tokens using python!
---------------------------
We are following the [Create Assett doc](https://docs.moneybutton.com/docs/api/v2/api-v2-asset-create.html#example-request) from Moneybutton and [Authencation Overview](https://docs.moneybutton.com/docs/api/auth/api-auth-overview.html#application-access).
You will need to set up your Client ID and Client Secret from Moneybutton's app. Screenshot below shows app location in your Moneybutton account. 

![browser](docs/images/mb_apps.jpg)
![browser](docs/images/mb_clientsecrets.jpg)
1. [createassets.py](createassets.py) Is the file with the code. This is missing the client id and secret. This is to keep the secrets safe and not have to worry about removing it later when sharing. Run these 2 commands in your terminal. This creates a local hidden file with the password.

````
export CLIENT_SECRET="Your_client_secret_number_here"
export CLIENT_ID="Your_client_ID_number_here"
````
2. os.environ is added in [createassets.py](createassets.py). This pulls the secrets from your local environment.
```
client_id = os.environ.get('CLIENT_ID')# insert Moneybutton
client id by export CLIENT_ID local file
client_secret = os.environ.get('CLIENT_SECRET')# insert MB client secret by using export CLIENT_SECRET local file
```
3. Create token to talk to server. The token is time sensitive and you may need to get a new one. 
```
python createasset.py 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjMyMjQ4M2VmMDczMjVkZjQ2ODY3NDJhNDM2NmIxZSIsImV4cCI6MTY0MjMxMDQzNiwic2NvcGUiOiJhcHBsaWNhdGlvbl9hY2Nlc3M6d3JpdGUifQ.RJ_v6csjT3tk_TJC6CmlOiXrtCzkTVmQ2_8FpfZIk7U
```
4. Now we use the "Bearer" to show who is holding the access token that we generated from step 3. This comes from ["api oauth overview"](https://docs.moneybutton.com/docs/api/auth/api-auth-overview.html) section of the Moneybutton docs. 
```
curl --request GET \
  --url 'https://www.moneybutton.com/api/v1/auth/user_identity' \
  --header 'authorization: Bearer <YOUR_ACCESS_TOKEN>'
```
5. We now add data into the python file similar to the Example Request. I also add the url to the image.
![browser](docs/images/mollymatch_paw.png)
```
{
  "protocol": "SFP",
  "name": "My First Token",
  "initialSupply": 1000000,
  "description": "My first token description",
  "avatar": "https://mywebsite.com/token-avatar.png",
  "url": "https://mywebsite.com"
}
```
Here is our code inside the createasset.py file. 
```
#Creating asset
response = requests.post(
    'https://www.moneybutton.com/api/v2/me/assets',
    headers={'Authorization': b'Bearer ' + access_token},
    data={
        "protocol": "SFP",
        "name": "My First Token",
        "initialSupply": 1000000,
        "description": "My first token description",
        "avatar": "https://mywebsite.com/token-avatar.png",
        "url": "https://mywebsite.com"})
```
6. We run python createasset.py and expect a return. This is what we receive
```
python createasset.py
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjMyMjQ4M2VmMDczMjVkZjQ2ODY3NDJhNDM2NmIxZSIsImV4cCI6MTY0MjMxMzA5MCwic2NvcGUiOiJhcHBsaWNhdGlvbl9hY2Nlc3M6d3JpdGUifQ.h0asLNlpShyQM1wGIKcS2qGfy6X_eHiau-1jVfQfpSA
{'errors': [{'id': 'd5b63cd0-7689-11ec-a6c5-750e05e34470', 'status': 500, 'title': 'Server Error', 'detail': 'An unexpected error has ocurred. Please, try again in a few minutes. Error ID d5b63cd0-7689-11ec-a6c5-750e05e34470.'}], 'jsonapi': {'version': '1.0'}}
(.venv) mollymatch@Rachaels-MacBook-Pro moneybutton_assets % 
```
7. We created getasset.py to see if we can read the tokens from my wallet. This is the response. 
```
python getasset.py 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYjMyMjQ4M2VmMDczMjVkZjQ2ODY3NDJhNDM2NmIxZSIsImV4cCI6MTY0MjMxMzYxOCwic2NvcGUiOiJhcHBsaWNhdGlvbl9hY2Nlc3M6d3JpdGUifQ.gJAUjlenqEjwx0QO7AJ5PL-MZwopquveZzSxTlf1otg
{'errors': [{'id': '1116a070-768b-11ec-a6c5-750e05e34470', 'status': 500, 'title': 'Server Error', 'detail': 'An unexpected error has ocurred. Please, try again in a few minutes. Error ID 1116a070-768b-11ec-a6c5-750e05e34470.'}], 'jsonapi': {'version': '1.0'}}
```