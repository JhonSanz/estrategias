# ESTRATEGIA
def close_operation(df):
    return (
        (df.open > df.MA_100) & (df.MA_100 > df.close)
        |
        (df.open < df.MA_100) & (df.MA_100 < df.close)
    )

def close_operation(df):
    return (
        (df.open > df.MA_100) & (df.MA_100 > df.close)
        |
        (df.open < df.MA_100) & (df.MA_100 < df.close)
    )

def operation_type(df):
    return df['close'] < df['MA_100']


df['OP_O'] = np.where(close_operation(df), df.close, None)
df['OP_C'] = np.where(close_operation(df), df.close, None)
df['type'] = np.where(operation_type(df), 'sell', 'buy')
df.loc[215:230]