import requests
import os

CLIENT_ID = os.getenv("5b6407c1-b781-491f-ab1c-9340609b4965")
CLIENT_SECRET = os.getenv("3d1a4220df266ca964ae360c343a3d201d4e17df41706dc746dc241380dd4133T")

def get_whoop_access_token():
    url = 'https://api.whoop.com/oauth/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(url, data=payload)
    token_data = response.json()
    print("Access Token:", token_data['access_token'])
    return token_data['access_token']

def fetch_recovery_data(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(
        'https://api.whoop.com/recovery',
        headers=headers,
        params={'start': '2025-03-20T00:00:00.000Z', 'end': '2025-03-23T00:00:00.000Z'}
    )
    print("Recovery Data:", response.json())

# Run the flow
token = get_whoop_access_token()
fetch_recovery_data(token)
