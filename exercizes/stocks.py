import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import yfinance as yf
#yf.pdr_override()
import tailer

#start = datetime.datetime(2018, 10, 1)
#end = datetime.datetime(2019, 9, 8)
start = "2018-09-07"
end = "2019-09-07"


df = web.get_data_yahoo("TSLA", start, end)
df.tail()
print(type(df))

close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()
print("1")
print(mavg)
close_px.tail()

#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='TSLA')
mavg.plot(label='mavg')
plt.legend()
