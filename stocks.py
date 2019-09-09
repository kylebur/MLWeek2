import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import yfinance as yf
yf.pdr_override()

#start = datetime.datetime(2018, 10, 1)
#end = datetime.datetime(2019, 9, 8)
start = "2018-09-07"
end = "2019-09-07"


df = web.get_data_yahoo("TSLA", start, end)
df.tail()
print(df)
