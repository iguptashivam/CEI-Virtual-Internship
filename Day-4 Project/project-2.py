import requests
import pandas as pd
import json
from datetime import  datetime, timedelta

header={
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "JSESSIONID=3717E05AF94B70D384CF3E653C5D3191; _ga=GA1.1.2114324755.1720621304; __gads=ID=3f89df532a057908:T=1720621304:RT=1720621304:S=ALNI_MbRrxVHDdMPQTbhFNQwQtih-krJug; __gpi=UID=00000e8ad96a21f2:T=1720621304:RT=1720621304:S=ALNI_MatZKks6JruQdo-sCnLPS2hv3j5bg; __eoi=ID=9456d205e8e1bbd7:T=1720621304:RT=1720621304:S=AA-AfjZXZuYwphwMP3_yKOshKPoq; _ga_2RYZG7Y4NC=GS1.1.1720621304.1.1.1720621464.0.0.0; FCNEC=%5B%5B%22AKsRol9i6Jn3iyVRBtAlj9JjH4nZ07TI7iz1GiUV9Moy9dKouvwsoP_uq_jkDefZdUjfPj6B83Zsw91GXkncqTILjfPQ58GSK1r93OGgIBtZU0vUTj8s3WfWA0SvML2egx6RMA9T5rgWuAxDYqfdBqPBTmPkKQiFnQ%3D%3D%22%5D%5D",
    "Referer": "https://vegetablemarketprice.com/market/delhi/today",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

url="https://vegetablemarketprice.com/api/dataapi/market/delhi/daywisedata?date=2024-07-09"

resp=requests.get(url,headers=header)
print(resp.text)
js_data=json.loads(resp.text)

date="2024-07-09"

start_date= datetime (2024,5,1)
end_date= datetime (2024,6,30)
data=[]

while start_date < end_date:
    data.append(start_date.strftime("%Y-%m-%d"))
    start_date=start_date + timedelta(days=1)

js_arr=[]
for date in data:

  for api in js_data["data"]:
    print(api)
    vegetable_name=api["vegetablename"]
    state_name= "new delhi"
    wholesale_price=api["price"]
    retail_price=api["retailprice"]
    unit=api["units"]
    mall_price=api["shopingmallprice"]
    Image = api["table"]["table_image_url"]

    new_js= {
        "date":date,
        "state_name": state_name,
        "vegetable_name":vegetable_name,
        "wholesale_price":wholesale_price,
        "retail_price":retail_price,
        "mall_price":mall_price,
        "unit":unit,
        "image":Image 
    }

    js_arr.append(new_js)


df=pd.DataFrame(js_arr)
df.to_csv("output.csv",index=False)  
print("Complete!")