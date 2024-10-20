import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('covid_19_data.csv')
data.fillna('NA',inplace= True)
data.drop(['SNo','Last_Update'],axis=1,inplace=True)
data.rename(columns={'ObservationDate':'Date','Province_State':'Province','Country_Region':'Country'},inplace=True)
pd.to_datetime(data['Date'])
data = data.groupby(by=['Country','Date'])[['Confirmed','Deaths','Recovered']].sum().reset_index()

countries = data['Country'].unique()

for i in range(0,len(countries)):
    c = data[data['Country']==countries[i]]
    plt.plot(np.arange(0,len(c)),c['Confirmed'],color = 'blue',label = 'Confirmed')
    plt.plot(np.arange(0,len(c)),c['Deaths'],color = 'red',label = 'Deaths')
    plt.plot(np.arange(0,len(c)),c['Recovered'],color = 'green',label = 'Recovered')
    plt.title(countries[i])
    plt.xlabel("Days since first case")
    plt.ylabel("No of cases")
    plt.legend()
    plt.show()