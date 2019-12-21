# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 07:29:40 2019

@author: Tejas
"""

import datetime as dt
from datetime import date
import pandas as pd
import pandas_datareader.data as web

today = date.today()

tdy = (today.strftime('%Y,%m,%d')).split(',')

start = dt.datetime(2000,1,1)
end = dt.datetime(int(tdy[0]),int(tdy[1]),int(tdy[2]))

df = web.DataReader('ADANIPOWER.NS' , 'yahoo' , start , end)

latest_data = ((df['Adj Close'].tail(1).to_string(index=False)).split('\n'))[1]
latest_data = float(latest_data)

print(latest_data)