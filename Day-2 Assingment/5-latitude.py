import requests as req

url = "http://api.open-notify.org/iss-now.json"

response = req.get(url)

if response.status_code == 200:
   
    jsonData = response.json()
    
  
    latitude = jsonData["iss_position"]["latitude"]
    longitude = jsonData["iss_position"]["longitude"]
    timestamp = jsonData["timestamp"]
    

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
