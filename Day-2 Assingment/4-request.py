import requests as req
import json

url = "http://api.open-notify.org/iss-now.json"

res= req.get(url)
jsonData = res.json()

print(json.dumps(jsonData, indent=6))
