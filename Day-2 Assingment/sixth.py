import requests as req
import pandas as pd
import time


url = "http://api.open-notify.org/iss-now.json"

csvFilename = "Location-Data.csv"

min_records = 100

data = []

recordsCollected = 0

while recordsCollected < min_records:
    try:
       
        response = req.get(url)
        
        response.raise_for_status()
        
        jsonData = response.json()
        
        timestamp = jsonData['timestamp']
        latitude = jsonData['iss_position']['latitude']
        longitude = jsonData['iss_position']['longitude']
        
        data.append({
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude
        })
        
        recordsCollected += 1
        
        print(f"Record {recordsCollected}: Timestamp: {timestamp} , Latitude: {latitude}, Longitude: {longitude}")
        
        time.sleep(1)
        
    except req.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        break

df = pd.DataFrame(data)

df.to_csv(csvFilename, index=False)

print(f"Data collection complete. {recordsCollected} records save to '{csvFilename}'.")
