from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import datetime
import uuid
pd.set_option('display.max_columns', None)

engine = create_engine('postgresql://himanshuagarwal:@localhost/scooterapi')

df  = pd.read_sql_query('select * FROM birds_dc',con=engine)
df['date_time'] = df['Date'].astype(str) + ' ' + df['Time'].astype(str)
df['date_time'] = pd.to_datetime(df.date_time)

#Identify "stationary" scooters for a day.

##Fetching scooter data in the morning between 7 to 7.15am and in the night between 11.45 to 11.59pm
df_10_1 = df.loc[((df['date_time']>= '2019-10-1 07:00:00')&(df['date_time']<= '2019-10-1 07:15:00')) | ((df['date_time']>= '2019-10-1 23:45:00')&(df['date_time']<= '2019-10-1 23:49:00'))]
df_10_1 = df_10_1.reset_index(drop=True)
##Totscoots is all the unique scooter ids present in the above timeframe
TotScootsUUID = []; TotScootsUUID= df_10_1['id'].unique().tolist()
##To convert the format of ids from UUID in TotScootsUUID to strings in TotScoots
TotScoots = []
for i,n in enumerate(TotScootsUUID):
    a = TotScootsUUID[i].urn.split(':')
    TotScoots.append(a[2])
##Converting latitude and longitude columns to tuples
df_10_1['lats_tups'] = list(zip(df_10_1['latitude'],df_10_1['longitude']))
#To make a dataframe 'lats' containing information of scooter ids and if had the
#same coordinate throughout the day.
df_10_1['id'] = df_10_1['id'].astype(str)
lats = pd.DataFrame(columns=['id','Count of lats'])
lens = []
for i,n in enumerate(TotScoots):
    lens.append(n)
    lens.append(df_10_1.loc[(df_10_1['id']== n,'lats_tups')].nunique())
    lats = lats.append({'id':lens[0],'Count of lats':lens[1]},ignore_index=True)
    lens = []
print(len(lats[lats['Count of lats']==1]))



df_10_1.to_csv('/Users/himanshuagarwal/BirdProject/Playground/Staa.csv')
