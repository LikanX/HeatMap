import csv
import pandas as pd
import string
import operator
import folium
from folium import plugins
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

import sqlite3
from os import path
import sqlalchemy 
import psycopg2
from config import config

#pip install psycopg2-binary
#pip install sqlalchemy
#lesa inn gögn
df_data = pd.read_csv('Data.csv',sep=',')
df_data['TIMESTAMP'] = pd.to_datetime(df_data.TIMESTAMP)
df_data['END_FLIGHT_DEP_TIME'] = pd.to_datetime(df_data.END_FLIGHT_DEP_TIME)





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
engine = sqlalchemy.create_engine("postgresql://postgres:Jakkih17@localhost/likanx")
con = engine.connect()
df_people.to_sql('people', con)
con.close()
# Verify that there are no existing tables
print(engine.table_names())



# að fá info til baka frá database sql
engine_string = "postgresql+psycopg2://{postgres}:{Jakkih17}@{localhost}:{5432}/{likanx}".format(
    user = 'postgres',
    password = 'Jakkih17',
    host = 'localhost',
    port = '5432',
    database = 'likanx',
)

# create sqlalchemy engine
engine = create_engine(engine_string)

# read a table from database into pandas dataframe, replace "tablename" with your table name
df = pd.read_sql_table('likanx',engine)






conn = psycopg2.connect(host="localhost", port = 5432, database="likanx", user="postgres", password="Jakkih17")

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""SELECT personid FROM people""")
query_results = cur.fetchall()
print(query_results)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()