import csv
import pandas as pd 
import string
import operator
import datetime


df_BPV = pd.read_csv('BPV.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
top_BPV = df_BPV.head()
top_BPV


df_Retail = pd.read_csv('Retail.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
top_retail = df_Retail.head()
top_retail


df_SSSS = pd.read_csv('SSSS.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
top_SSSS = df_SSSS.head()
top_SSSS


df_test = pd.DataFrame()
df_test['Date'] = df_Retail['TimeStamp']
unique_retailers = df_test.Position.unique()


df_test.loc[(df_test.Position == 'Veitingastadur1'), 'X'] = 5
df_test.loc[(df_test.Position == 'Veitingastadur1'), 'Y'] = 4

df_test.loc[(df_test.Position == 'Verslun1Vestur'), 'X'] = 1
df_test.loc[(df_test.Position == 'Verslun1Vestur'), 'Y'] = 3

df_test.loc[(df_test.Position == 'Verslun2Vestur'), 'X'] = 6
df_test.loc[(df_test.Position == 'Verslun2Vestur'), 'Y'] = 7

df_test.loc[(df_test.Position == 'Verslun1Austur'), 'X'] = 8
df_test.loc[(df_test.Position == 'Verslun1Austur'), 'Y'] = 8

df_test.loc[(df_test.Position == 'Verslun2Austur'), 'X'] = 9
df_test.loc[(df_test.Position == 'Verslun2Austur'), 'Y'] = 9

# df_Retail['TimeStamp'] = pd.to_datetime(df_Retail['TimeStamp'])


# new = df_Retail['TimeStamp'].str.split(" ", n = 1, expand = True) 

# df_Retail['Date'] = new[0]
# df_Retail['Time'] = new[1]

# df_Retail['Date']= pd.to_datetime(df_Retail['Date']) 
# df_Retail['year']= pd.to_datetime(df_Retail['year']) 
# df_Retail['Time']= pd.to_datetime(df_Retail['Time']) 

# df_Retail.info()
