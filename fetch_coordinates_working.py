#Packages to be imported
import requests
import pandas as pd
import math
import numpy as np
import geopy
from geopy.distance import distance
from geopy.distance import VincentyDistance
import json
from datetime import date, datetime, timedelta
import datetime as dt
import time
from functions_file import get_jsondata

#Loop to get all coordinate points
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


#Function to get data for a coordinate, add date and time values and then export it. 

start_date= dt.date(2019,9,2)
start_date_string = start_date.strftime("%m-%d-%Y")

def get_birds(dest,z2):
    global start_date, start_date_string
    df4 = []
    for idx,c in enumerate(dest):
        latitude = c[0]
        longitude = c[1]
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
    df99 = df99.drop_duplicates(subset='id')
    today = date.today().strftime("%m-%d-%Y")
    if today == start_date_string:
        df99.to_csv(r'/Users/himanshuagarwal/BirdProject/BirdData-Test4-49coor-'+str(start_date_string)+'.csv', index = None, mode = 'a', header=True) #Don't forget to add '.csv' at the end of the path
    elif today > start_date_string:
        start_date = start_date + timedelta(days=1)
        start_date_string = start_date.strftime("%m-%d-%Y")
        df99.to_csv(r'/Users/himanshuagarwal/BirdProject/BirdData-Test4-49coor-'+str(start_date_string)+'.csv', index = None, mode = 'a', header=True) #Don't forget to add '.csv' at the end of the pat

#Automation of data extraction
for z in range(1,3):
    get_birds(dest,z)
    time.sleep(30)
    
json_data889 = get_jsondata(38.95026, -77.09355)
for x,i in enumerate(json_data889['birds']):
            d = json_data889['birds'][x]['location']
            b = tuple(d.values())
            r = distance((38.95026, -77.09355),b).mi
            i.update({'Origin_Dist':r})
            i.update({'Date':date.today().strftime('%Y-%m-%d')})
            i.update({'Time':datetime.now().strftime('%H:%M:%S')})
            """i.update({'Origin_Loc':'DC-GWU'})"""

#One solution
json_data889
df889 = pd.DataFrame.from_dict(json_data889['birds'], orient = 'columns')
df889 = df889[['id','code','model','captive','nest_id','battery_level','estimated_range','Origin_Dist','Date','Time','location']]
df889 = pd.concat([df889.drop(['location'],axis=1), df889['location'].apply(pd.Series)],axis=1)

#Second solution
from collections import OrderedDict
json_data890 = OrderedDict(json_data889)
df890 = pd.DataFrame.from_dict(json_data890['birds'], orient = 'columns')
df889 = df889[['id','code','model','captive','nest_id','battery_level','estimated_range','Origin_Dist','Date','Time','location']]
df889 = pd.concat([df889.drop(['location'],axis=1), df889['location'].apply(pd.Series)],axis=1)


df889.head(25)