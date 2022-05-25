from numpy import append
import pandas as pd
import pandas_ta as ta

df = pd.read_csv(
    'syp_1m2 copy.csv',
    names=['date', 'open', 'high', 'low', 'close', 'volume', 'unknown']
)
df = df[['date', 'open', 'high', 'low', 'close']]
df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')
df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)

# Calculate Returns and append to the df DataFrame
# df.ta.log_return(cumulative=True, append=True)
# df.ta.percent_return(cumulative=True, append=True)

# print(df.tail())
# print(df.ta.indicators())
# help(ta.psar)

# print(ta.sma(df['close'], length=100))
# df.ta.sma(length=100, append=True)


getattr(df.ta, 'psar')(append=True)
'''
Index(['date', 'open', 'high', 'low', 'close', 'PSARl_0.02_0.2',
       'PSARs_0.02_0.2', 'PSARaf_0.02_0.2', 'PSARr_0.02_0.2'],
      dtype='object')
'''
print(df[['close', 'PSARl_0.02_0.2', 'PSARs_0.02_0.2', 'PSARaf_0.02_0.2', 'PSARr_0.02_0.2']].tail(10))

