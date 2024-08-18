import requests
import dotenv
import os

dotenv.load_dotenv()

# API configuration
client_id = os.environ.get("client_id")
access_token = os.environ.get("token")
base_url = 'https://api.igdb.com/v4'


print(client_id, access_token)
payload = 'f *;where id = 380;'
print(type(client_id), type(access_token))
response = requests.post(
    'https://api.igdb.com/v4/platform_logos',
    **{
        'headers': {'Client-ID': f'{client_id}', 'Authorization': f'Bearer {access_token}'},
        'data': payload
    }
)
print ("response: %s" % str(response.json()))
