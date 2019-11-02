from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import datetime
import uuid
import matplotlib.pyplot as plt
import matplotlib
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import contextily as ctx
from sklearn.cluster import KMeans

engine = create_engine('postgresql://himanshuagarwal:@localhost/scooterapi')

df  = pd.read_sql_query('select * FROM birds_dc',con=engine)
df['date_time'] = df['Date'].astype(str) + ' ' + df['Time'].astype(str)
df['date_time'] = pd.to_datetime(df.date_time)


df_10_1 = df.loc[((df['date_time']>= '2019-10-1 07:00:00')&(df['date_time']<= '2019-10-1 07:15:00')) | ((df['date_time']>= '2019-10-1 23:45:00')&(df['date_time']<= '2019-10-1 23:59:00'))]
df_10_1 = df_10_1.reset_index(drop=True)


##Fetching scooter data in the morning between 7 to 7.15am and in the night between 11.45 to 11.59pm
df_10_1_morning = df.loc[((df['date_time']>= '2019-10-1 07:00:00')&(df['date_time']<= '2019-10-1 07:15:00'))]
df_10_1_evening = df.loc[((df['date_time']>= '2019-10-1 23:45:00')&(df['date_time']<= '2019-10-1 23:59:00'))]
df_10_1_morning = df_10_1_morning.reset_index(drop=True)
df_10_1_evening = df_10_1_evening.reset_index(drop=True)
##Totscoots is all the unique scooter ids present in the above timeframe
TotScootsUUID = []; TotScootsUUID= df_10_1_morning['id'].unique().tolist()
##To convert the format of ids from UUID in TotScootsUUID to strings in TotScoots
TotScoots = []
for i,n in enumerate(TotScootsUUID):
    a = TotScootsUUID[i].urn.split(':')
    TotScoots.append(a[2])
##Converting latitude and longitude columns to tuples
df_10_1_morning['lats_tups'] = list(zip(df_10_1_morning['latitude'],df_10_1_morning['longitude']))
df_10_1_evening['lats_tups'] = list(zip(df_10_1_evening['latitude'],df_10_1_evening['longitude']))
#To make a dataframe 'lats' containing information of scooter ids and if had the
#same coordinate throughout the day.
df_10_1_morning['id'] = df_10_1_morning['id'].astype(str)
df_10_1_evening['id'] = df_10_1_evening['id'].astype(str)
lats = pd.DataFrame(columns=['id','Count of lats'])
lens = []
for i,n in enumerate(TotScoots):
    lens.append(n)
    lens.append(df_10_1_evening.loc[(df_10_1_evening['id']== n,'lats_tups')].nunique())
    lats = lats.append({'id':lens[0],'Count of lats':lens[1]},ignore_index=True)
    lens = []
#No. of stationary scooters for 10/1:
print(len(lats[lats['Count of lats']==1]))
StatScoots = pd.DataFrame(columns=['id'])
StatScootsList = lats.loc[(lats['Count of lats']==1,'id')].tolist()
StatScoots = StatScoots.append([{'id': i} for i in StatScootsList],ignore_index=True)

#Plotting on a map
"""import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon"""



street_map = gpd.read_file('/Users/himanshuagarwal/BirdProject/Street_Centerlines/Street_Centerlines.shp')
gdf = gpd.GeoDataFrame(df_10_1_morning, geometry=gpd.points_from_xy(df_10_1_morning.longitude, df_10_1_morning.latitude))
fig, ax = plt.subplots(figsize = (15,15))
street_map.plot(ax = ax, alpha = 0.4, color="grey")
gdf.plot(ax=ax,markersize=20,color="blue",marker="o")
plt.show()

StatScootsFinal = df_10_1_morning.merge(StatScoots, how = 'inner', on='id')
StatScootsFinal.drop_duplicates(subset='id',keep='first',inplace=True)
StatScootsFinal['geometry'].nunique()
gdf = gpd.GeoDataFrame(StatScootsFinal)
fig, ax = plt.subplots(figsize = (15,15))
street_map.plot(ax = ax, alpha = 0.4, color="grey")
gdf.plot(ax=ax,markersize=20,color="blue",marker="o")
plt.show()

street_map2 = street_map.to_crs({'init':'epsg:3857'})
ax = street_map2.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax)

gdf = gpd.GeoDataFrame(df_10_1_morning, geometry=gpd.points_from_xy(df_10_1_morning.longitude, df_10_1_morning.latitude))
gdf.head()
fig= plt.subplots(figsize = (15,15))
ax = street_map2.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax)
street_map2.plot(ax = ax, alpha = 0.4, color="grey")
gdf.plot(ax=ax,markersize=20,color="blue",marker="o")
plt.show()


X = StatScootsFinal[['latitude', 'longitude']].values
kmeans = KMeans(n_clusters=10)
predictions = kmeans.fit_predict(X)

clustered = pd.concat([StatScootsFinal.reset_index(), 
                       pd.DataFrame({'Cluster':predictions})], 
                      axis=1)
clustered.drop('index', axis=1, inplace=True)


fig = plt.figure(figsize=(16,8))
cmap=plt.cm.rainbow
norm = matplotlib.colors.BoundaryNorm(np.arange(0,10,1), cmap.N)
plt.scatter(clustered['latitude'], clustered['longitude'], c=clustered['Cluster'],cmap=cmap, norm=norm, s=150, edgecolor='none')
plt.colorbar(ticks=np.linspace(0,9,10))
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=100, alpha=0.3)
plt.xlim(38.8, 39)
plt.ylim(-77.14, -76.9)
plt.xlabel('Latitude', fontsize=14)
plt.ylabel('Longitude', fontsize=14)
plt.title('k-means clustering results (n_clusters=10)', fontsize=14)
plt.grid()
plt.show()


def get_scoots(date):
    global df_morning
    df_morning, df_evening = pd.DataFrame()
    df_morning = df.loc[((df['date_time']>= ''+str(date)+' 07:00:00')&(df['date_time']<= ''+str(date)+' 07:15:00'))]

df_morning, df_evening = pd.DataFrame()

get_scoots('2019-10-1')


def get_statscoots(date):
    ##Fetching scooter data in the morning between 7 to 7.15am and in the night between 11.45 to 11.59pm
    global df_morning, df_evening, StatScoots
    df_morning = pd.DataFrame()
    df_evening = pd.DataFrame()
    df_morning = df.loc[((df['date_time']>= ''+str(date)+' 07:00:00')&(df['date_time']<= ''+str(date)+' 07:15:00'))]
    df_evening = df.loc[((df['date_time']>= ''+str(date)+' 23:45:00')&(df['date_time']<= ''+str(date)+' 23:59:00'))]
    df_morning = df_morning.reset_index(drop=True)
    df_evening = df_evening.reset_index(drop=True)
    ##Totscoots is all the unique scooter ids present in the above timeframe
    TotScootsUUID = []; TotScootsUUID= df_morning['id'].unique().tolist()
    ##To convert the format of ids from UUID in TotScootsUUID to strings in TotScoots
    TotScoots = []
    for i,n in enumerate(TotScootsUUID):
        a = TotScootsUUID[i].urn.split(':')
        TotScoots.append(a[2])
    ##Converting latitude and longitude columns to tuples
    df_morning['lats_tups'] = list(zip(df_morning['latitude'],df_morning['longitude']))
    df_evening['lats_tups'] = list(zip(df_evening['latitude'],df_evening['longitude']))
    #To make a dataframe 'lats' containing information of scooter ids and if had the
    #same coordinate throughout the day.
    df_morning['id'] = df_morning['id'].astype(str)
    df_evening['id'] = df_evening['id'].astype(str)
    lats = pd.DataFrame(columns=['id','Count of lats'])
    lens = []
    for i,n in enumerate(TotScoots):
        lens.append(n)
        lens.append(df_evening.loc[(df_evening['id']== n,'lats_tups')].nunique())
        lats = lats.append({'id':lens[0],'Count of lats':lens[1]},ignore_index=True)
        lens = []
    #No. of stationary scooters for 10/1:
    StatScoots = pd.DataFrame(columns=['date','id'])
    StatScootsList = lats.loc[(lats['Count of lats']==1,'id')].tolist()
    StatScoots = StatScoots.append([{'id': i, 'date':date} for i in StatScootsList],ignore_index=True)
    StatScoots['date'] = pd.to_datetime(StatScoots.date)

get_statscoots('2019-10-3')
StatScoots['date'] = pd.to_datetime(StatScoots.date)

times = pd.date_range('2012-09-03', periods=289, freq='1440min')
dates = pd.date_range(start='2019-09-03', end='2019-10-19')
dates = dates.strftime('%Y-%m-%d')











