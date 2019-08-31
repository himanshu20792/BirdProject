import geopy
from geopy.distance import VincentyDistance
from geopy.distance import distance
from functions_file import get_jsondata
import requests
# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

dest= []
origin = geopy.Point(38.899600,-77.04882)

for i in range(1,6):
    for j in range(1,6):
        destination = VincentyDistance(miles=j).destination(origin, 180)
        lat2, lon2 = destination.latitude, destination.longitude
        dest.append((lat2,lon2))
    origin_horizontal = VincentyDistance(miles=i).destination(origin, 90)
    destination = VincentyDistance(miles=i).destination(origin, 180)
    origin_horizontal_lat, origin_horizontal_lon = origin_horizontal.latitude, origin_horizontal.longitude
    origin = (origin_horizontal_lat,origin_horizontal_lon)
    


def get_birds(dest):
    for idx,c in enumerate(dest):
        latitude = c[0]
        longitude = c[1]
        json_data99 = get_jsondata(latitude,longitude)
        radius = []
        #To add Date, Time, Distance from origin, Origin-LOC
        for x,i in enumerate(json_data99['birds']):
            d = json_data99['birds'][x]['location']
            b = tuple(d.values())
            r = distance(gwu,b).mi
            radius.append(r)
            i.update({'Origin_Dist':r})
            i.update({'Date':date.today().strftime('%Y-%m-%d')})
            i.update({'Time':datetime.now().strftime('%H-%M-%S')})
            """i.update({'Origin_Loc':'DC-GWU'})"""
        #To convert it to a dataframe
        df3 = pd.DataFrame.from_dict(json_data99['birds'], orient = 'columns')
        df3 = pd.concat([df3.drop(['location'],axis=1), df3['location'].apply(pd.Series)],axis=1)
        #Export to CSV
        df3.to_csv(r'/Users/himanshuagarwal/BirdProject/BirdData-Test-5coor.csv', index = None, mode = 'a', header=True) #Don't forget to add '.csv' at the end of the path
        if idx==5:
            break
