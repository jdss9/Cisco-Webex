import requests

url = "https://webexapis.com/v1/rooms"

payload = {}
headers = {
  'Authorization': 'Bearer MWU4ZjI3YTMtMDRhZS00YTNkLWFlMjQtNjY0MTBiYTE5YjJlYjUxYjgzZGYtM2Fj_P0A1_aa83f64c-d5cb-4c26-a953-d22659e4c23a'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)