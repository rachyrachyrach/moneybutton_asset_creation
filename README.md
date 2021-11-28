# moneybutton_asset_creation
Create tokens using python!
<br />
More to be added soon. 

Nov. 27 2021: This code will take you only to creating token until I add more. I got up to eat ;)
<br />
You will need to set up your Client ID and Client Secret from Moneybutton's app. Screenshot below shows app location in your Moneybutton account. 
![browser](docs/images/mb_apps.jpg)
<br />
1. createassets.py 
<br />
This is missing the client id and secret. I created:
```
    export CLIENT_SECRET="Your_client_secret_number_here"
    export CLIENT_ID="Your_client_ID_number_here"
```
2. For lines 6 & 7 I added os.environ
```
client_id = os.environ.get('CLIENT_ID')# insert Moneybutton
client id by export CLIENT_ID local file
client_secret = os.environ.get('CLIENT_SECRET')# insert MB client secret by using export CLIENT_SECRET local file
```
