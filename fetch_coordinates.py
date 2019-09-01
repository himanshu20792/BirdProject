import geopy
from geopy.distance import VincentyDistance
from geopy.distance import distance
import requests
# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

dest= []
origin = geopy.Point(38.95026, -77.09355)

for i in range(1,8):
    for j in range(1,8):
        destination = VincentyDistance(miles=j).destination(origin, 180)
        lat2, lon2 = destination.latitude, destination.longitude
        dest.append((lat2,lon2))
    origin_horizontal = VincentyDistance(miles=1).destination(origin, 90)
    """destination = VincentyDistance(miles=i).destination(origin, 180)"""
    origin_horizontal_lat, origin_horizontal_lon = origin_horizontal.latitude, origin_horizontal.longitude
    origin = (origin_horizontal_lat,origin_horizontal_lon)
   
    

def get_birds(dest):
    df4 = []
    for idx,c in enumerate(dest):
        latitude = c[0]
        longitude = c[1]
        print(idx, '\n')
        json_data99 = get_jsondata(latitude,longitude)
        radius = []
        #To add Date, Time, Distance from origin, Origin-LOC
        for x,i in enumerate(json_data99['birds']):
            print(i)
            d = json_data99['birds'][x]['location']
            b = tuple(d.values())
            r = distance(c,b).mi
            radius.append(r)
            i.update({'Origin_Dist':r})
            i.update({'Date':date.today().strftime('%Y-%m-%d')})
            i.update({'Time':datetime.now().strftime('%H:%M:%S')})
            """i.update({'Origin_Loc':'DC-GWU'})"""
        #To convert it to a dataframe
        df3 = pd.DataFrame.from_dict(json_data99['birds'], orient = 'columns')
        df3 = pd.concat([df3.drop(['location'],axis=1), df3['location'].apply(pd.Series)],axis=1)
        df4.append(df3)
        df99 = pd.concat(df4,ignore_index=True)
        
    #Export to CSV
    df99.to_csv(r'/Users/himanshuagarwal/BirdProject/BirdData-Test4-49coor.csv', index = None, mode = 'a', header=True) #Don't forget to add '.csv' at the end of the path
