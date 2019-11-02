from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import datetime
import uuid
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

engine = create_engine('postgresql://himanshuagarwal:@localhost/scooterapi')

df  = pd.read_sql_query('select * from birds_dc',con=engine)
df4  = pd.read_sql_query('select * from birds_dc',con=engine, parse_dates = ['Date','Time'])

df.head()
df.describe()
df.dtypes
df_scootsbydate = df.groupby('Date')['id'].nunique()
df_scootsbydate.mean()
df['date_time'] = df['Date'].astype(str) + ' ' + df['Time'].astype(str)
df['date_time'] = pd.to_datetime(df.date_time)
df_scootsbydayofwk2['Avg.'] = df.groupby(df['date_time'].dt.weekday_name,sort=False).id.nunique().mean()
df['id'].nunique()

#Identify "stationary" scooters for a day.
df_10_1 = df.loc[(df['date_time']>= '2019-10-1 00:00:00')&(df['date_time']<= '2019-10-2 00:00:00')]
df_10_1 = df_10_1.reset_index(drop=True)
df_10_1['id'].nunique()
unqscoots = []
unqscoots = df_10_1['id'].unique().tolist()
unqscoots_hex = []
unqscoots_hex = [unqscoots[u].hex for u,j in enumerate(unqscoots)]
unqscoots1 = []
for i,n in enumerate(unqscoots):
    a = unqscoots[i].urn.split(':')
    unqscoots1.append(a[2])

#To make a dataframe 'lats' containing information of scooter ids and if had the
#same coordinate throughout the day.
df_10_1.loc[(df_10_1['id']== unqscoots1[0],tuple('latitude','longitude'))]
df_10_1['lats_tups'] = list(zip(df_10_1['latitude'],df_10_1['longitude']))
lats = pd.DataFrame(columns=['id','Count of lats'])
lens = []
for i,n in enumerate(unqscoots1):
    lens.append(n)
    lens.append(df_10_1.loc[(df_10_1['id']== n,'lats_tups')].nunique())
    lats = lats.append({'id':lens[0],'Count of lats':lens[1]},ignore_index=True)
    lens = []
print(len(lats[lats['Count of lats']==1]))
#Dataframe of stationary scooters
df_statscoots = 

df_10_1.head()
df_10_1.columns



b[~b.isin(a)].dropna()

a = pd.DataFrame()
b = pd.DataFrame()