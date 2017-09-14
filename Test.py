import requests
import json
response = requests.get("http://api.open-notify.org/iss-now.json")
data=response.json()
print(response.status_code)
print(data.keys())
print(data["timestamp"])
myD=data["iss_position"]
print(myD["latitude"])
