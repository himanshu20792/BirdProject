#POST request to get authentication token
import requests
URL = "https://api.birdapp.com/user/login"
email = {"email": "himanshu.agarwal20792@gmail.com"}
headers = {"User-Agent": "Bird/4.41.0 (co.bird.Ride; build:37; iOS 12.3.1) Alamofire/4.41.0",
           "Device-Id": "54253685-49a0-48e0-a239-759e77639506",
           "Platform": "ios",
           "App-Version": "4.41.0",
           "Content-Type": "application/json"}
r = requests.post(URL, json= email, headers = headers)
r.status_code
print(r.text)

#GET request to fetch the data

"""New York - Upper east side"""
URL_get = "https://api.birdapp.com/bird/nearby?latitude=40.784652&longitude=-73.948462&radius=5000"
loc = {"latitude":40.784652,"longitude":-73.948462,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
headers_get = {
"Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjVlYWQ2M2UyLWFiNGItNDZiYy1hNjZlLTI5N2NmNTJkM2VkMSIsImRldmljZV9pZCI6IjU0MjUzNjg1LTQ5YTAtNDhlMC1hMjM5LTc1OWU3NzYzOTUwNiIsImV4cCI6MTU5NzM2OTk2N30.hVSnrrx_adyrS2ecIyRba5E8Q-3RoylZ8WwBbqo15GY",
"Device-id": "54253685-49a0-48e0-a239-759e77639506",
"App-Version": "4.41.0",
"Location":  '{"latitude":40.784652,"longitude":-73.948462,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}'
}
rget = requests.get(URL_get, headers = headers_get, params = loc)
rget.status_code
rget.text
json_data = rget.json()



"""New York - Pine street(Block from Wall street)"""
URL_get2 = "https://api.birdapp.com/bird/nearby?latitude=40.706398&longitude=-74.008065&radius=5000"
loc2 = {"latitude":40.706398,"longitude":-74.008065,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
headers_get2 = {
"Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjVlYWQ2M2UyLWFiNGItNDZiYy1hNjZlLTI5N2NmNTJkM2VkMSIsImRldmljZV9pZCI6IjU0MjUzNjg1LTQ5YTAtNDhlMC1hMjM5LTc1OWU3NzYzOTUwNiIsImV4cCI6MTU5NzM2OTk2N30.hVSnrrx_adyrS2ecIyRba5E8Q-3RoylZ8WwBbqo15GY",
"Device-id": "54253685-49a0-48e0-a239-759e77639506",
"App-Version": "4.41.0",
"Location":  '{"latitude":40.706398,"longitude":-74.008065,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}'
}
rget2 = requests.get(URL_get2, headers = headers_get2, params = loc2)
rget2.status_code
rget2.text
json_data2 = rget2.json()



"""Washington D.C. - George Washington University"""
URL_get3 = "https://api.birdapp.com/bird/nearby?latitude=38.899600&longitude=-77.048820&radius=0.00001"
loc3 = {"latitude":38.899600,"longitude":-77.04882,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
headers_get3 = {
"Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjVlYWQ2M2UyLWFiNGItNDZiYy1hNjZlLTI5N2NmNTJkM2VkMSIsImRldmljZV9pZCI6IjU0MjUzNjg1LTQ5YTAtNDhlMC1hMjM5LTc1OWU3NzYzOTUwNiIsImV4cCI6MTU5NzM2OTk2N30.hVSnrrx_adyrS2ecIyRba5E8Q-3RoylZ8WwBbqo15GY",
"Device-id": "54253685-49a0-48e0-a239-759e77639506",
"App-Version": "4.41.0",
"Location":  '{"latitude":38.899600,"longitude":-77.048820,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}'
}
rget3 = requests.get(URL_get3, headers = headers_get3, params = loc3)
rget3.status_code
rget3.text
json_data3[ = rget3.json()


""""To get configuration settings"""
URL_get4 = "https://api.birdapp.com/config/location?latitude=42.3140089&longitude=-71.2490943"
"""
loc3 = {"latitude":38.922368,"longitude":-77.019448,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
"""
headers_get4 = {
"App-Version": "4.41.0"
}
rget4 = requests.get(URL_get4, headers = headers_get4)
rget4.status_code
rget4.text
json_data4 = rget4.json()


#Putting birds values as a dataframe    
import pandas as pd
df3 = pd.DataFrame.from_dict(json_data3['birds'], orient = 'columns')
df4 = pd.concat([df3.drop(['location'],axis=1), df3['location'].apply(pd.Series)],axis=1)


import gmaps
gmaps.configure(api_key="AIzaSyDsWngN6Fn0rVOMClQqE21kkmhEG_z0vgM")
locations = df4[['latitude','longitude']]
fig = gmaps.figure()
washington_coordinates = (38.899600,-77.04882)




"""Arlington"""
URL_get5 = "https://api.birdapp.com/bird/nearby?latitude=38.883694&longitude=-77.168652&radius=0.00001"
loc5 = {"latitude":38.883694,"longitude":-77.168652,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
headers_get5 = {
"Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjVlYWQ2M2UyLWFiNGItNDZiYy1hNjZlLTI5N2NmNTJkM2VkMSIsImRldmljZV9pZCI6IjU0MjUzNjg1LTQ5YTAtNDhlMC1hMjM5LTc1OWU3NzYzOTUwNiIsImV4cCI6MTU5NzM2OTk2N30.hVSnrrx_adyrS2ecIyRba5E8Q-3RoylZ8WwBbqo15GY",
"Device-id": "54253685-49a0-48e0-a239-759e77639506",
"App-Version": "4.41.0",
"Location":  '{"latitude":38.883694,"longitude":-77.168652,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}'
}
rget5 = requests.get(URL_get5, headers = headers_get5, params = loc5)
rget5.status_code
rget5.text
json_data5 = rget5.json()
#Putting birds values as a dataframe    
import pandas as pd
df5 = pd.DataFrame.from_dict(json_data5['birds'], orient = 'columns')
df5 = pd.concat([df5.drop(['location'],axis=1), df5['location'].apply(pd.Series)],axis=1)


"""Washington DC -2"""
URL_get6 = "https://api.birdapp.com/bird/nearby?latitude=38.910456&longitude=-76.987568&radius=0.00001"
loc6 = {"latitude":38.910456,"longitude":-76.987568,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
headers_get6 = {
"Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjVlYWQ2M2UyLWFiNGItNDZiYy1hNjZlLTI5N2NmNTJkM2VkMSIsImRldmljZV9pZCI6IjU0MjUzNjg1LTQ5YTAtNDhlMC1hMjM5LTc1OWU3NzYzOTUwNiIsImV4cCI6MTU5NzM2OTk2N30.hVSnrrx_adyrS2ecIyRba5E8Q-3RoylZ8WwBbqo15GY",
"Device-id": "54253685-49a0-48e0-a239-759e77639506",
"App-Version": "4.41.0",
"Location":  '{"latitude":38.910456,"longitude":-76.987568,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}'
}
rget6 = requests.get(URL_get6, headers = headers_get6, params = loc6)
rget6.status_code
rget6.text
json_data6 = rget6.json()
#Putting birds values as a dataframe    
import pandas as pd
df6 = pd.DataFrame.from_dict(json_data6['birds'], orient = 'columns')
df6 = pd.concat([df6.drop(['location'],axis=1), df6['location'].apply(pd.Series)],axis=1)

import geopy
from geopy.distance import distance
json_data3.birds.items()
import pandas as pd
df3 = pd.DataFrame.from_dict(json_data3['birds'], orient = 'columns')
print(df3['location'].items())

origin = (38.899600,-77.04882)
for loc, coord in df3['location'].items():
    d = distance(origin,coord)
    print(d)

import json
with open("sample_json.json","w") as write_file:
    json.dump(json_data3, write_file, indent = 4)

#Finding maximum radius of bikes

#George Washington Univ
from geopy.distance import distance
print(json_data3['birds'][0]['location'])
x=0
radius = []
gwu = (38.899600,-77.04882)
for i in json_data3['birds']:
    d = json_data3['birds'][x]['location']
    b = tuple(d.values())
    r = distance(gwu,b).mi
    radius.append(r)
    x = x+1
    i.update({'Origin_Dist':r})
    
print(max(radius))

#Washington-DC 2

def get_data(origin):
    x2=0
    radius2 = []
    dc2 = (38.910456,-76.987568)
    for i in json_data6['birds']:
        d2 = json_data6['birds'][x2]['location']
        b2 = tuple(d2.values())
        r = distance(dc2,b2).mi
        radius2.append(r)
        x2 = x2+1
        i.update({'Origin Dist':r})
        i.update({'Date':date.today().strftime('%Y-%m-%d')})
        i.update({'Time':datetime.now().strftime('%H-%M-%S')})

print(max(radius2))


#Arlington
x3=0
test_radius3 = []
dc3 = (38.883694,-77.168652)
for i in json_data5['birds']:
    d3 = json_data5['birds'][x3]['location']
    b3 = tuple(d3.values())
    print("Bike loc before append: ", b3)
    test_radius3.append(distance(dc3,b3).mi)
    print("Origin is: ",dc3)
    print("Bike loc after append is: ",b3)
    print("Radius list is: ",test_radius3)
    x3 = x3+1
    print("x3 = ", x3)
    if x3==4:
        break

print(max(radius3))

from datetime import date
today = date.today()
print("Today's date:", today)

from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("Trying to append json data sdasdasdasd")