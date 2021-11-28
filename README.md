# moneybutton_asset_creation
Create tokens using python!
---------------------------
We are following the [Create Assett doc](https://docs.moneybutton.com/docs/api/v2/api-v2-asset-create.html#example-request) from Moneybutton and [Authencation Overview](https://docs.moneybutton.com/docs/api/auth/api-auth-overview.html#application-access).
You will need to set up your Client ID and Client Secret from Moneybutton's app. Screenshot below shows app location in your Moneybutton account. 
![browser](docs/images/mb_apps.jpg)
1. [createassets.py](createassets.py) Is the file with the code. This is missing the client id and secret. This is to keep the secrets safe and not have to worry about removing it later when sharing. Run these 2 commands in your terminal. This creates a local hidden file with the password.

````
export CLIENT_SECRET="Your_client_secret_number_here"
export CLIENT_ID="Your_client_ID_number_here"
````
2. os.environ is added in [createassets.py](createassets.py). This pulls the secrets from your local directory.
```
client_id = os.environ.get('CLIENT_ID')# insert Moneybutton
client id by export CLIENT_ID local file
client_secret = os.environ.get('CLIENT_SECRET')# insert MB client secret by using export CLIENT_SECRET local file
```
