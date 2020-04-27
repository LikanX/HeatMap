import csv
import pandas as pd
import string
import operator
import folium
from folium import plugins
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from matplotlib import cm
import sqlite3
from os import path
import sqlalchemy 
import psycopg2
from config import Config
from scipy import stats
#pip install psycopg2-binary
#pip install sqlalchemy
#lesa inn gögn
df_data = pd.read_csv('Data.csv',sep=',')
df_data['TIMESTAMP'] = pd.to_datetime(df_data.TIMESTAMP)
df_data['END_FLIGHT_DEP_TIME'] = pd.to_datetime(df_data.END_FLIGHT_DEP_TIME)

df_flights = pd.read_csv('flight_number.csv',sep=',')



#bý til dataframe sem er með most important info
df_people = pd.DataFrame()
df_people['personid']=df_data.USER_FK
df_people['area'] = df_data.AREA
df_people['timestamp'] = df_data.TIMESTAMP
df_people['entertime'] = df_data.START_ROUTE_ENTERTIME
df_people['leavetime'] = df_data.END_FLIGHT_DEP_TIME
df_people['totaltime'] = df_data.DWELL_TIME
df_people['flightname'] = df_data.END_FLIGHT_GATE

#terminal -> psql -> create database likanx
#password = password sem þú notar fyrir sql
#Færa allt database yfir í SQL = profit (lol þeir sem gera for loops)
#engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/likanx")
#con = engine.connect()
#df_people.to_sql('people', con)
#con.close()
# Verify that there are no existing tables
#print(engine.table_names())




# hér fyrir neðan er allt sem þarf til þess að sækja úr database. ATH þarf að hafa database.ini file líka í sömu möppu
#database.ini
#[postgresql]
#host=localhost
#database=people
#user=postgres
#password=ykkar password
#
# from configparser import ConfigParser
 
# def config(filename='database.ini', section='postgresql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
 
#     # get section, default to postgresql
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             db[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
#     return db


# params = config()
conn = psycopg2.connect(host="localhost", port = 5432, database="likanx", user="postgres", password="postgres")

# Connect to the PostgreSQL database
#conn = psycopg2.connect(**params)
# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def create_pandas_table(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table
  
# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable
people_info = create_pandas_table("SELECT * FROM people")
people_info.head()

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()



df_people['X'] = 0
df_people['Y'] = 0


df_people.loc[(df_people.area == 'Total Journey'), 'X'] = 25
df_people.loc[(df_people.area == 'Total Journey'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Air Bridge'), 'X'] = 13
df_people.loc[(df_people.area == 'Area: Air Bridge'), 'Y'] = 11

df_people.loc[(df_people.area == 'Area: Pier A'), 'X'] = 19
df_people.loc[(df_people.area == 'Area: Pier A'), 'Y'] = 11

df_people.loc[(df_people.area == 'Area: IMM/EMI'), 'X'] = 20
df_people.loc[(df_people.area == 'Area: IMM/EMI'), 'Y'] = 5

df_people.loc[(df_people.area == 'Area: Pier C East'), 'X'] = 21
df_people.loc[(df_people.area == 'Area: Pier C East'), 'Y'] = 3

df_people.loc[(df_people.area == 'Area: Pier C West'), 'X'] = 17
df_people.loc[(df_people.area == 'Area: Pier C West'), 'Y'] = 3

df_people.loc[(df_people.area == 'Area: Gate C/D31'), 'X'] = 10
df_people.loc[(df_people.area == 'Area: Gate C/D31'), 'Y'] = 1

df_people.loc[(df_people.area == 'C/D33, C/D36'), 'X'] = 10
df_people.loc[(df_people.area == 'C/D33, C/D36'), 'Y'] = 5

df_people.loc[(df_people.area == 'Area: Food Area'), 'X'] = 9
df_people.loc[(df_people.area == 'Area: Food Area'), 'Y'] = 3

df_people.loc[(df_people.area == 'Area: Gate C/D24-29, C, E'), 'X'] = 4
df_people.loc[(df_people.area == 'Area: Gate C/D24-29, C, E'), 'Y'] = 2
#
df_people.loc[(df_people.area == 'Area: Pier D West'), 'X'] = 6.5
df_people.loc[(df_people.area == 'Area: Pier D West'), 'Y'] = 2.5
#
df_people.loc[(df_people.area == 'Area: Check-in Total'), 'X'] = 13
df_people.loc[(df_people.area == 'Area: Check-in Total'), 'Y'] = 17
#
df_people.loc[(df_people.area == 'Area: Check-in B-C'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Check-in B-C'), 'Y'] = 17.5
#
df_people.loc[(df_people.area == 'Area: Joe & The Juice'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Joe & The Juice'), 'Y'] = 18.5

df_people.loc[(df_people.area == 'Area: Arrival Pick-up'), 'X'] = 9.5
df_people.loc[(df_people.area == 'Area: Arrival Pick-up'), 'Y'] = 17.5

df_people.loc[(df_people.area == 'Area: Security'), 'X'] = 18.5
df_people.loc[(df_people.area == 'Area: Security'), 'Y'] = 18

df_people.loc[(df_people.area == 'Area: Departing Duty Free'), 'X'] = 20
df_people.loc[(df_people.area == 'Area: Departing Duty Free'), 'Y'] = 17

df_people.loc[(df_people.area == 'Area: Lounge'), 'X'] = 19
df_people.loc[(df_people.area == 'Area: Lounge'), 'Y'] = 15

df_people.loc[(df_people.area == 'Area: Check-in Kiosk'), 'X'] = 6.5
df_people.loc[(df_people.area == 'Area: Check-in Kiosk'), 'Y'] = 18.5

df_people.loc[(df_people.area == 'Area: Check-in A'), 'X'] = 6
df_people.loc[(df_people.area == 'Area: Check-in A'), 'Y'] = 17

df_people.loc[(df_people.area == 'Area: Baggage Reclaim'), 'X'] = 9
df_people.loc[(df_people.area == 'Area: Baggage Reclaim'), 'Y'] = 15

df_people.loc[(df_people.area == 'Area: Non-Schengen Duty Free'), 'X'] = 8.5
df_people.loc[(df_people.area == 'Area: Non-Schengen Duty Free'), 'Y'] = 4

df_people.loc[(df_people.area == 'Area: Pier D East'), 'X'] = 8.5
df_people.loc[(df_people.area == 'Area: Pier D East'), 'Y'] = 2.5

df_people.loc[(df_people.area == 'Area: Transfer Security'), 'X'] = 4
df_people.loc[(df_people.area == 'Area: Transfer Security'), 'Y'] = 5

df_people.loc[(df_people.area == 'Area: Tax Refund'), 'X'] = 10
df_people.loc[(df_people.area == 'Area: Tax Refund'), 'Y'] = 18.5

df_people.loc[(df_people.area == 'Area: Pier D North'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier D North'), 'Y'] = 7

df_people.loc[(df_people.area == 'Area: Arriving Duty Free'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Arriving Duty Free'), 'Y'] = 16

df_people.loc[(df_people.area == 'Area: Gate A1-2'), 'X'] = 22.5
df_people.loc[(df_people.area == 'Area: Gate A1-2'), 'Y'] = 14.5



import matplotlib.image as mpimg 
map_img = mpimg.imread('isavia_map.png') 

hmax = sns.kdeplot(df_people["X"],df_people["Y"], cmap="Blues", n_levels=5, shade=True, bw=0.1)
hmax.collections[0].set_alpha(0)

plt.imshow(map_img, zorder=0, extent=[0, 25.0, 0, 20])
plt.show()




#-------- annað plot test

hmax =sns.kdeplot(df_people["X"],df_people["Y"])
plt.show()



#------------------- annað plot test


LH = df_people.loc[df_people.flightname == "LH0869"]
FI = df_people.loc[df_people.flightname == "FI0216"]
ax = sns.kdeplot(LH.X, LH.Y, cmap="Reds", shade=True, shade_lowest=False, bw=0.15)
ax.collections[0].set_alpha(0)
ax = sns.kdeplot(FI.X, FI.Y, cmap="Blues", shade=True, shade_lowest =False, bw=0.15)
ax.collections[0].set_alpha(0)
plt.imshow(map_img, zorder=0, extent=[0, 25.0, 0, 18.5])
plt.show()











fig, ax = plt.subplots()
fig.set_size_inches(14,4)

#Plot one - include shade

sns.kdeplot(df_people["X"],df_people["Y"], shade="True")

#Plot two - no shade, lines only
plt.subplot(122)
sns.kdeplot(df_people["X"],df_people["Y"])
plt.show()

fig, ax = plt.subplots()
fig.set_size_inches(14,4)

#Plot One - distinct areas with few lines
plt.subplot(121)
sns.kdeplot(df_people["X"],df_people["Y"], shade="True", n_levels=5)

#Plot Two - fade lines with more of them
plt.subplot(122)
sns.kdeplot(df_people["X"],df_people["Y"], shade="True", n_levels=1)

plt.show()



#-------------------------------
data = df_people.X, df_people.entertime
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)


# hér fyrir neðan ætla ég að búa til consumption dæmi eins og sjá má a link 
# https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/

sns.distplot(x, kde=False, fit=stats.gamma);
sns.kdeplot(x, shade=True);
sns.pairplot(iris, hue="species");
sns.lineplot(data=data, palette="tab10", linewidth=2.5)





unique_areas = df_people.area.unique()

dat = pd.DataFrame()
dat = pd.DataFrame(dat, columns = [i for i in unique_areas])

unique_flights = df_people.flightname.unique()

unique_people = df_people.personid.unique()

# add the data to the unique 


for i in unique_flights:
    df_people.loc[df_people.personid == i]


for i in unique_people:
    df_people.loc[df_people.personid == i]
    for j in unique_areas:
        if df_people.loc[df_people.personid == i].loc[df_people.area == j].shape[0] != 0:
            dat[j] = df_people.loc[df_people.personid == i].loc[df_people.area == j].totaltime





start_datetime = df_people['entertime'].min()
end_datetime = df_people['entertime'].max()
ax.set_xlim(start_datetime, end_datetime)

df_people.loc[df_people.flightname == 'LH0869'].loc[df_people.area == 'Area: Air Bridge'].totaltime


(df['time_delta'].astype('timedelta64[s]') / 60).plot.hist()

sns.distplot(df_people.loc[df_people.flightname == 'LH0869'].loc[df_people.area == 'Area: Air Bridge'].entertime.astype('timedelta64[s]'), kde = False)
ax = plt.gca()
# get current xtick labels
xticks = ax.get_xticks()
# convert all xtick labels to selected format from ms timestamp
ax.set_xticklabels([pd.to_datetime(tm, unit='s').strftime('%Y-%m-%d\n %H:%M:%S') for tm in xticks],
 rotation=50)

plt.show()






# -------------------------- gefur mjög flotta mynd sem sýnir tíðni --------------------------

sns.distplot(df_people.loc[df_people.area == 'Area: Baggage Reclaim'].entertime.astype('timedelta64[s]'), kde = False, bins=100, axlabel= 'Area: Baggage Reclaim - Entertime')
ax = plt.gca()

# get current xtick labels
xticks = ax.get_xticks()

ax.set_xlim(min(xticks), max(xticks))
#xticks = np.arange(min(xticks), max(xticks), 10)
# convert all xtick labels to selected format from ms timestamp
ax.set_xticklabels([pd.to_datetime(tm, unit='s').strftime('%Y-%m-%d\n %H:%M:%S') for tm in xticks],
 rotation=50)

plt.show()

# --------------------------------------------------------------------------------------------------------


# -------------------------- Bæta við airport og city og country og airline á df_people2 --------------------------

engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/likanx")
con = engine.connect()
df_flights.to_sql('flights', con)
con.close()

#get the new table 



# Verify that there are no existing tables
print(engine.table_names())


from configparser import ConfigParser
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db


params = config()
conn = psycopg2.connect(host="localhost", port = 5432, database="likanx", user="postgres", password="postgres")

# Connect to the PostgreSQL database
#conn = psycopg2.connect(**params)
# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def create_pandas_table(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table
  
# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable
df_people2 = create_pandas_table("SELECT p.personid, p.area, p.timestamp, p.entertime, p.leavetime, p.totaltime, p.realleavetime, p.flightname AS flightnumber, f.Airport, f.city, f.country, f.airline FROM people p, flights f WHERE f.flightnumber = p.flightname")


# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()

# það breyttist allt í ehv bull þannig ég þurfti að gera þetta hérna aftur
df_people2['entertime'] = pd.to_datetime(df_people2.entertime)
df_people2['leavetime'] = pd.to_datetime(df_people2.leavetime)
df_people2['totaltime'] = pd.to_datetime(df_people2.totaltime)
df_people2['realleavetime'] = pd.to_datetime(df_people2.realleavetime)

df_people2['entertime'] = pd.to_timedelta(df_people2.entertime)
df_people2['totaltime'] = pd.to_timedelta(df_people2.totaltime)
#
# -------------------------- gefur mjög flotta mynd sem sýnir tíðni --------------------------
sns.distplot(df_people2.loc[df_people2.airline == 'WizzAir'].loc[df_people2.area == 'Area: Security'].totaltime.astype('timedelta64[s]'), kde = False, bins = 100, axlabel= 'Area: Security - Totaltime - People travelling /w WizzAir')
#sns.distplot(df_people.loc[df_people.area == 'Area: Baggage Reclaim'].entertime.astype('timedelta64[s]'), kde = False, bins=100, axlabel= 'Area: Baggage Reclaim - Entertime')
ax = plt.gca()

# get current xtick labels
xticks = ax.get_xticks()

ax.set_xlim(min(xticks), max(xticks))
#xticks = np.arange(min(xticks), max(xticks), 10)
# convert all xtick labels to selected format from ms timestamp
ax.set_xticklabels([pd.to_datetime(tm, unit='s').strftime('%Y-%m-%d\n %H:%M:%S') for tm in xticks],
 rotation=50)

plt.show()

# --------------------------------------------------------------------------------------------------------
