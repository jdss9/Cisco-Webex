import requests
import json
from dotenv import load_dotenv
import os

url = "https://webexapis.com/v1/rooms"

load_dotenv()

webex_token = os.getenv("WEBEX_BOT_TOKEN")

payload = {}
headers = {
  'Authorization': 'Bearer ' + webex_token
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
print(json.dumps(data, indent=4))