# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:38:37 2020

@author: kathe
"""


import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
#%%
file = (r'C:\Users\kathe\Downloads')
df = pd.read_csv('GDP.csv', parse_dates=['Date'])
df['lnRGDP']=np.log2(df['RGDP'])
df['lagRGDP']=df.lnRGDP.shift(1)
df['dRGDP']=df.RGDP.pct_change()
df['dlnRGDP']=df.lnRGDP.pct_change()
df['lagdlnRGDP']=df.dlnRGDP.shift(1)
df['year'] = [d.year for d in df.Date]
df.head()

  
plt.plot(df['Date'],df['RGDP']) 
plt.xlabel('Date')
plt.ylabel('RGDP') 
plt.title('RGDP vs Date') 
plt.show() 


plt.plot(df['Date'],df['lnRGDP']) 
plt.xlabel('Date')
plt.ylabel('lnRGDP') 
plt.title('lnRGDP vs Date') 
plt.show() 
