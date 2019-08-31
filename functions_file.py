
def get_jsondata(lat,lon):
    import requests
    URL_get = f"https://api.birdapp.com/bird/nearby?latitude={lat}&longitude={lon}&radius=0.00001"
    loc = {"latitude":lat,"longitude":lon,"altitude":500,"accuracy":100,"speed":-1,"heading":-1}
    headers_get = {
    "Authorization": "Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjVlYWQ2M2UyLWFiNGItNDZiYy1hNjZlLTI5N2NmNTJkM2VkMSIsImRldmljZV9pZCI6IjU0MjUzNjg1LTQ5YTAtNDhlMC1hMjM5LTc1OWU3NzYzOTUwNiIsImV4cCI6MTU5NzM2OTk2N30.hVSnrrx_adyrS2ecIyRba5E8Q-3RoylZ8WwBbqo15GY",
    "Device-id": "54253685-49a0-48e0-a239-759e77639506",
    "App-Version": "4.41.0",
    "Location":  '{"latitude":'+str(lat)+',"longitude":'+str(lon)+',"altitude":500,"accuracy":100,"speed":-1,"heading":-1}'
    }
    rget = requests.get(URL_get, headers = headers_get, params = loc)
    json_data = rget.json()
    return json_data
