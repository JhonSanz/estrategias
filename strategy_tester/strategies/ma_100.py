# def open_position(row):
#     if (str(row.name) == '0'):
#         return None
#     previous = df.loc[int(row.name) - 1]    
#     condition = (
#         (row.close < row.MA_100 and previous.type == 'buy') 
#         or
#         (row.close > row.MA_100 and previous.type == 'sell')
#     )
#     return row.close if condition else None

# def close_position(row):
#     if (str(row.name) == '0'):
#         return None
#     previous = df.loc[int(row.name) - 1]    
#     condition = (
#         (row.close < row.MA_100 and previous.type == 'buy') 
#         or
#         (row.close > row.MA_100 and previous.type == 'sell')
#     )
#     return row.close if condition else None

# def position_type(row):
#     return 'sell' if row['close'] < row['MA_100'] else 'buy'

def positions_table(x):
    return {"jeje": "hola"}