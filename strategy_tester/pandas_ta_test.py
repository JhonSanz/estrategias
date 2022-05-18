from numpy import append
import pandas as pd
import pandas_ta as ta

df = pd.read_csv(
    'datos2.csv',
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
# help(ta.rsi)

# print(ta.sma(df['close'], length=100))
getattr(df.ta, 'rsi')(length=14, append=True)
# df.ta.sma(length=100, append=True)
print(df.iloc[0:20])
