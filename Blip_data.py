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

#pip install psycopg2-binary
#pip install sqlalchemy
#lesa inn gögn
df_data = pd.read_csv('Data.csv',sep=',')
#bý til dataframe sem er með most important info
df_people = pd.DataFrame()
df_people['personid']=df_data.USER_FK
df_people['area'] = df_data.AREA
df_people['timestamp'] = df_data.TIMESTAMP
df_people['entertime'] = df_data.START_ROUTE_ENTERTIME
df_people['leavetime'] = df_data.END_FLIGHT_DEP_TIME
df_people['totaltime'] = df_data.DWELL_TIME
df_people['flightname'] = df_data.END_FLIGHT_GATE
df_people['flightnumber'] = df_data.END_FLIGHT

#terminal -> psql -> create database likanx
#password = password sem þú notar fyrir sql
#Færa allt database yfir í SQL = profit (lol þeir sem gera for loops)
engine = sqlalchemy.create_engine("postgresql://postgres:PASSWORD@localhost/likanx")
con = engine.connect()
df_people.to_sql('people', con)
con.close()
# Verify that there are no existing tables
print(engine.table_names())


# Skilgreina X og Y hnit
df_people.loc[(df_people.area == 'Total Journey'), 'X'] = 8
df_people.loc[(df_people.area == 'Total Journey'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Air Bridge'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Air Bridge'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Pier A'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier A'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: IMM/EMI '), 'X'] = 8
df_people.loc[(df_people.area == 'Area: IMM/EMI '), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Pier C East'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier C East'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Pier C West'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier C West'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Gate C/D31'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Gate C/D31'), 'Y'] = 8

df_people.loc[(df_people.area == 'C/D33, C/D36'), 'X'] = 8
df_people.loc[(df_people.area == 'C/D33, C/D36'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Food Area'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Food Area'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Gate C/D24-29, C, E'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Gate C/D24-29, C, E'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Pier D West'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier D West'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Check-in Total'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Check-in Total'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Check-in B-C'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Check-in B-C'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Joe & The Juice'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Joe & The Juice'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Arrival Pick-up'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Arrival Pick-up'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Security'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Security'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Departing Duty Free'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Departing Duty Free'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Lounge'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Lounge'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Check-in Kiosk'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Check-in Kiosk'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Check-in A'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Check-in A'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Baggage Reclaim'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Baggage Reclaim'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Non-Schengen Duty Free'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Non-Schengen Duty Free'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Pier D East'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier D East'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Transfer Security'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Transfer Security'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Tax Refund'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Tax Refund'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Pier D North'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Pier D North'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Arriving Duty Free'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Arriving Duty Free'), 'Y'] = 8

df_people.loc[(df_people.area == 'Area: Gate A1-2'), 'X'] = 8
df_people.loc[(df_people.area == 'Area: Gate A1-2'), 'Y'] = 8

