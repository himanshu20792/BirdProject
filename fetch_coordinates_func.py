#Import all necessary packages
import geopy
from geopy.distance import VincentyDistance
import math
from geopy.distance import distance
import numpy as np

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

dest= []
origin = geopy.Point(38.95026, -77.09355)
 
 
def get_coordinates(origin,nmbr_sqrt,dist): 
    for i in np.arange(1,nmbr_sqrt):
        for j in np.arange(1,nmbr_sqrt):
            destination = VincentyDistance(miles=dist*j).destination(origin, 180)
            lat2, lon2 = destination.latitude, destination.longitude
            dest.append((lat2,lon2))
        origin_horizontal = VincentyDistance(miles=dist*i).destination(origin, 90)
        origin_horizontal_lat, origin_horizontal_lon = origin_horizontal.latitude, origin_horizontal.longitude
        origin = (origin_horizontal_lat,origin_horizontal_lon)

def input_details():    
    origin_lat = input("Enter the latitude coordinates of the origin point:")
    origin_lon = input("Enter the longitude coordinates of the origin point:")
    orig = (origin_lat,origin_lon)
    no_req = input("Enter the number of coordinates required (In whole squares):")
    no_req_sqrt = math.sqrt(int(no_req))
    dis_bet_coor = input("Enter the miles between each coordinate:")
    get_coordinates(orig,no_req_sqrt,int(dis_bet_coor))

input_details()

