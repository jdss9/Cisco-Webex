import requests
import json
from dotenv import load_dotenv
import os

url = "https://webexapis.com/v1/messages"

load_dotenv()

webex_token = os.getenv("WEBEX_BOT_TOKEN")
webex_roomid = os.getenv("WEBEX_BOT_ROOMID")

payload = json.dumps({
  "roomId": webex_roomid,
  "text": "Hola soy un BOT de WebEx"
})
headers = {
  'Authorization': 'Bearer '+ webex_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()

print(json.dumps(data,indent=4))