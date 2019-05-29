import pandas as pd          
import numpy as np          # For mathematical calculations
import matplotlib.pyplot as plt  # For plotting graphs
from datetime import datetime    # To access datetime
from pandas import Series        # To work on series
import matplotlib

import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15,8


df = pd.read_excel('WaterData.xls')
df['Water Shed'].value_counts()
df = df[    (df['Water Shed'] == 'Barton Creek') 
        | (df['Water Shed'] == 'Bull Creek')
        | (df['Water Shed'] == 'Lady Bird Lake')]  #considering only top 3

df[df['Water Shed'] == 'Bull Creek']['Site Name'].value_counts()

drop_list = ['Site Name', 'UNIT', 'UNIT.1', 'CHEMICAL OXYGEN DEMAND (0.025N K2CR207)', 'UNIT.2',
       'CHEMICAL OXYGEN DEMAND (0.25N K2CR2O7)', 'UNIT.3',
       'BIOCHEMICAL OXYGEN DEMAND (5 DAY 20 DEG C)', 'UNIT.4',
       'UNIT.5', 'UNIT.6', 'UNIT.7',  'UNIT.8', 'CALCIUM', 'UNIT.9',
       'CHLORINE', 'UNIT.10', 'MAGNESIUM', 'UNIT.11', 'BICARBONATE (AS HCO3)', 'UNIT.12']

df = df.drop(drop_list, axis = 1)    #drop the irrelevant columns

df.dtypes

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M')

df1 = df

#Index Sorting
#plt.plot(df1['PH'])
df1 = df1.set_index(df1['Date'])
df1 = df1.sort_index()
#plt.plot(df1['PH'])

#Plotting
#plot_cols = ['PH', 'DISSOLVED OXYGEN', 'WATER TEMPERATURE',
#       'TURBIDITY', 'CONDUCTIVITY', 'TOTAL SUSPENDED SOLIDS']
#
#j=0
#
#for i in plot_cols:
#    plt.figure(j)
#    plt.plot(df1[i])
#    plt.title(i+' PLOT')
#    j = j + 1
    
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
#plt.figure(j)
#ph_cross = pd.crosstab(df1['Water Shed'], df1['PH'])
#ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
#plt.title('Water Shed and PH', fontsize = 14)
#
#j=j+1
#
#
#plt.figure(j)
#ph_cross = pd.crosstab(df1['Water Shed'], df1['DISSOLVED OXYGEN'])
#ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
#plt.title('Water Shed and DISSOLVED OXYGEN', fontsize = 14)
#
#j=j+1
#
#plt.figure(j)
#ph_cross = pd.crosstab(df1['Water Shed'], df1['WATER TEMPERATURE'])
#ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
#plt.title('Water Shed and WATER TEMPERATURE', fontsize = 14)
#
#j=j+1
#
#plt.figure(j)
#ph_cross = pd.crosstab(df1['Water Shed'], df1['TURBIDITY'])
#ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
#plt.title('Water Shed and TURBIDITY', fontsize = 14)
#
#j=j+1
#
#
#plt.figure(j)
#ph_cross = pd.crosstab(df1['Water Shed'], df1['CONDUCTIVITY'])
#ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
#plt.title('Water Shed and CONDUCTIVITY', fontsize = 14)
#
#j=j+1
#
#plt.figure(j)
#ph_cross = pd.crosstab(df1['Water Shed'], df1['TOTAL SUSPENDED SOLIDS'])
#ph_cross.div(ph_cross.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
#plt.title('Water Shed and TOTAL SUSPENDED SOLIDS', fontsize = 14)
#
#j=j+1


#Forecasting beigns

training_set = df1['2000':'2013']
test_set = df1['2014':'2016']
training_set['Date'] = pd.to_datetime(training_set['Date'],format='%d-%m-%Y %H:%M') 
test_set['Date'] = pd.to_datetime(test_set['Date'],format='%d-%m-%Y %H:%M')
#training_set['month'] = training_set.Date.dt.month
#training_set['day'] = training_set.Date.dt.day


training_set = training_set.drop(['Date','DISSOLVED OXYGEN','TURBIDITY','CONDUCTIVITY','TOTAL SUSPENDED SOLIDS','WATER TEMPERATURE'],axis = 1)
test_set = test_set.drop(['Date','DISSOLVED OXYGEN','TURBIDITY','CONDUCTIVITY','TOTAL SUSPENDED SOLIDS','WATER TEMPERATURE'], axis = 1)


tr_ba = training_set[training_set['Water Shed'] == 'Barton Creek']
#tr_bu = training_set[training_set['Water Shed'] == 'Bull Creek']
#tr_lb = training_set[training_set['Water Shed'] == 'Lady Bird Lake']
te_ba = test_set[test_set['Water Shed'] == 'Barton Creek']
#te_bu = test_set[test_set['Water Shed'] == 'Bull Creek']
#te_lb = test_set[test_set['Water Shed'] == 'Lady Bird Lake']

tr_ba['ds'] = tr_ba.index
te_ba['ds'] = te_ba.index
tr_ba['y'] = tr_ba.PH
te_ba['y'] = te_ba.PH
tr_ba = tr_ba.drop(['Water Shed','PH'],axis = 1)
te_ba = te_ba.drop(['Water Shed','PH'],axis = 1)



#day_frac = training_set.groupby(['day']).mean()/np.sum(training_set.groupby(['day']).mean())
#day_frac.drop(['ID'], axis = 1, inplace = True)
#day_frac.columns = ['fraction']

#month_frac = training_set.groupby(['month']).mean()/np.sum(training_set.groupby(['month']).mean())
#month_frac.drop(['ID'], axis = 1, inplace = True)
#month_frac.columns = ['fraction']


from fbprophet import Prophet
m = Prophet(yearly_seasonality = True, seasonality_prior_scale=0.1)
m.fit(tr_ba)
future = m.make_future_dataframe(periods=600)
forecast = m.predict(future)
m.plot_components(forecast)


# Extract hour, day, month and year from both dataframes to merge
for df in [test, forecast]:
    df['hour'] = df.Datetime.dt.hour
    df['day'] = df.Datetime.dt.day
    df['month'] = df.Datetime.dt.month
    df['year'] = df.Datetime.dt.year

# Merge forecasts with given IDs
test = pd.merge(test,forecast, on=['day','month','year'], how='left')
cols = ['ID','hour','yhat']
test_new = test[cols]

# Merging hourly average fraction to the test data
test_new = pd.merge(test_new, hourly_frac, left_on = ['hour'], right_index=True, how = 'left')
# Convert daily aggregate to hourly traffic
test_new['Count'] = test_new['yhat'] * test_new['fraction']
test_new.drop(['yhat','fraction','hour'],axis = 1, inplace = True)
test_new.to_csv('prophet_sub.csv',index = False)