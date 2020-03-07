import csv
import pandas as pd 
import string
import operator
import datetime
import matplotlib.pyplot as plt

# les gogn
df_BPV = pd.read_csv('BPV.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
top_BPV = df_BPV.head()
top_BPV


df_Retail = pd.read_csv('Retail.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
top_retail = df_Retail.head()
top_retail


df_SSSS = pd.read_csv('SSSS.csv', sep=';', error_bad_lines=False, index_col=False, dtype='unicode')
top_SSSS = df_SSSS.head()
top_SSSS


# Byr til nyja toflu
df_test = pd.DataFrame()
df_test['Position'] = df_Retail['ScanningPosition']
df_test['Date'] = df_Retail['TimeStamp']
unique_retailers = df_test.Position.unique()


# Skilgreina verslanir með hnitum
df_test.loc[(df_test.Position == 'Veitingastadur1'), 'X'] = 8
df_test.loc[(df_test.Position == 'Veitingastadur1'), 'Y'] = 8

df_test.loc[(df_test.Position == 'Verslun1Vestur'), 'X'] = 1
df_test.loc[(df_test.Position == 'Verslun1Vestur'), 'Y'] = 7

df_test.loc[(df_test.Position == 'Verslun2Vestur'), 'X'] = 4
df_test.loc[(df_test.Position == 'Verslun2Vestur'), 'Y'] = 6

df_test.loc[(df_test.Position == 'Verslun1Austur'), 'X'] = 8
df_test.loc[(df_test.Position == 'Verslun1Austur'), 'Y'] = 1

df_test.loc[(df_test.Position == 'Verslun2Austur'), 'X'] = 5
df_test.loc[(df_test.Position == 'Verslun2Austur'), 'Y'] = 1


x = df_test['X']
y = df_test['Y']


plt.hist2d(x,y, bins=[np.arange(0,11,1),np.arange(0,11,1)], cmap=plt.cm.jet)
plt.show()

#plottar counter af verlunum
pd.value_counts(df_test['Position']).plot(kind='bar')

