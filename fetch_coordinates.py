import geopy
from geopy.distance import VincentyDistance

from geopy.distance import distance

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
    
    
for i in range(1,6):
    for j in range(1,6):
        print(j)
    print(j)
    
 r = distance((38.88510315910802, -77.04882),(38.87060628212457, -77.04882)).mi