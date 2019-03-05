import pandas as pd          
import numpy as np          # For mathematical calculations
import matplotlib.pyplot as plt  # For plotting graphs
from datetime import datetime    # To access datetime
from pandas import Series        # To work on series
import matplotlib
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")

df = pd.read_excel('WaterData.xls')
df['Water Shed'].value_counts()
df = df[    (df['Water Shed'] == 'Barton Creek') 
        | (df['Water Shed'] == 'Bull Creek')
        | (df['Water Shed'] == 'Lady Bird Lake')]

df[df['Water Shed'] == 'Bull Creek']['Site Name'].value_counts()

drop_list = ['Site Name', 'UNIT', 'UNIT.1', 'CHEMICAL OXYGEN DEMAND (0.025N K2CR207)', 'UNIT.2',
       'CHEMICAL OXYGEN DEMAND (0.25N K2CR2O7)', 'UNIT.3',
       'BIOCHEMICAL OXYGEN DEMAND (5 DAY 20 DEG C)', 'UNIT.4',
       'UNIT.5', 'UNIT.6', 'UNIT.7',  'UNIT.8', 'CALCIUM', 'UNIT.9',
       'CHLORINE', 'UNIT.10', 'MAGNESIUM', 'UNIT.11', 'BICARBONATE (AS HCO3)', 'UNIT.12']

df = df.drop(drop_list, axis = 1)    #drop the irrelevant columns

#df['MAGNESIUM'].isna().sum()
#
#df[df['Water Shed'] == 'Lady Bird Lake']['TOTAL SUSPENDED SOLIDS'].isna().sum()
#
#df[df['Water Shed'] == 'Lady Bird Lake'].count()

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15,8

df.dtypes

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M')

df1 = df

#Index Sorting
plt.plot(df1['PH'])
df1 = df1.set_index(df1['Date'])
df1 = df1.sort_index()
plt.plot(df1['PH'])

#Plotting
plot_cols = ['PH', 'DISSOLVED OXYGEN', 'WATER TEMPERATURE',
       'TURBIDITY', 'CONDUCTIVITY', 'TOTAL SUSPENDED SOLIDS']

j=0

for i in plot_cols:
    plt.figure(j)
    plt.plot(df1[i])
    plt.title(i+' PLOT')
    j = j + 1
    
df1 = df1['2000':'2016']

#Prepping
def PH_norm(row):
    return round(row, 1)

df1['PH'] = df1['PH'].apply(PH_norm)

import math
def DO_norm(row):
    if(math.isnan(row)):
        return np.nan
    else:
        return round(row * 2)/2

df1['DISSOLVED OXYGEN'] = df1['DISSOLVED OXYGEN'].apply(DO_norm)

def TEMP_norm(row):
    if(math.isnan(row)):
        return np.nan
    if(row>100):
        return np.nan
    else:
        return round(row)

df1['WATER TEMPERATURE'] = df1['WATER TEMPERATURE'].apply(TEMP_norm)

def TURB_norm(row):
    if(math.isnan(row)):
        return np.nan
    if(row>100):
        return np.nan
    else:
        return round(row)

df1['TURBIDITY'] = df1['TURBIDITY'].apply(TURB_norm)

def COND_norm(row):
    if(math.isnan(row)):
        return np.nan
    if(row <100):
        return np.nan
    else:
        return round(row, -2)

df1['CONDUCTIVITY'] = df1['CONDUCTIVITY'].apply(COND_norm)

def TSS_norm(row):
    if(math.isnan(row)):
        return np.nan
#    if(row <100):
#        return np.nan
    else:
        return 2.5*round(row/2.5)

df1['TOTAL SUSPENDED SOLIDS'] = df1['TOTAL SUSPENDED SOLIDS'].apply(TSS_norm)


#Bivariate Analysis
plt.figure(j)
ph_cross = pd.crosstab(df1['Water Shed'], df1['PH'])
ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.title('Water Shed and PH', fontsize = 14)

j=j+1


plt.figure(j)
ph_cross = pd.crosstab(df1['Water Shed'], df1['DISSOLVED OXYGEN'])
ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.title('Water Shed and DISSOLVED OXYGEN', fontsize = 14)

j=j+1

plt.figure(j)
ph_cross = pd.crosstab(df1['Water Shed'], df1['WATER TEMPERATURE'])
ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.title('Water Shed and WATER TEMPERATURE', fontsize = 14)

j=j+1

plt.figure(j)
ph_cross = pd.crosstab(df1['Water Shed'], df1['TURBIDITY'])
ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.title('Water Shed and TURBIDITY', fontsize = 14)

j=j+1


plt.figure(j)
ph_cross = pd.crosstab(df1['Water Shed'], df1['CONDUCTIVITY'])
ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.title('Water Shed and CONDUCTIVITY', fontsize = 14)

j=j+1

plt.figure(j)
ph_cross = pd.crosstab(df1['Water Shed'], df1['TOTAL SUSPENDED SOLIDS'])
ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.title('Water Shed and TOTAL SUSPENDED SOLIDS', fontsize = 14)

j=j+1

