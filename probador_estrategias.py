import pandas as pd
df = pd.read_csv('datos2.csv', names=['date', 'open', 'high', 'low', 'close', 'volume', 'unknown'])
df = df[['date', 'open', 'high', 'low', 'close']]
df['MA_100'] = df.close.rolling(100).mean()
df['type'] = df.apply(lambda x: 'sell' if x.close < x.MA_100 else 'buy', axis=1)
def open_position(row):
    condition = (
        row.open > row.MA_100 > row.close
        or
        row.open < row.MA_100 < row.close
    )
    return row.close if condition else None

def close_position(row):
    condition = (
        row.open > row.MA_100 > row.close
        or
        row.open < row.MA_100 < row.close
    )
    return row.close if condition else None

df['OP_O'] = df.apply(lambda x: open_position(x), axis=1)
df['OP_C'] = df.apply(lambda x: close_position(x), axis=1)
results = df[['date', 'OP_O', 'OP_C', 'type']]
results = results.dropna().reset_index(drop=True)

def total_minus(x):
    if (str(x.name) == '0'):
        return None
    previous = results.loc[int(x.name) - 1]
    value = x.OP_C - previous.OP_O
    return value * (-1) if previous.type == 'sell' else value

results['total'] = results.apply(lambda x: total_minus(x), axis=1)
results['total_2'] = results.total.cumsum()

import matplotlib.pyplot as plt

plt.plot(results.date, results.total_2)
plt.show()